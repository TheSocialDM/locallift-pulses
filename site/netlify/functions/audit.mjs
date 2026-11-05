// Audit form intake. Checks the request, then passes it to the delivery step.
const ALLOWED = /^https:\/\/(www\.localliftnow\.com|localliftnow\.com|([a-z0-9-]+--)?locallift-site-preview\.netlify\.app)$/;
const clean = (v, max) => String(v ?? '').replace(/[\r\n\t]+/g, ' ').trim().slice(0, max);
const reply = (status, body) => new Response(JSON.stringify(body), {status, headers: {'content-type': 'application/json'}});

export default async req => {
  if (req.method !== 'POST') return reply(405, {ok: false});
  if (!ALLOWED.test(req.headers.get('origin') || '')) return reply(403, {ok: false});

  // A browser without JavaScript posts the plain form, so answer it with a plain page.
  const plain = (req.headers.get('content-type') || '').includes('urlencoded');
  const page = text => new Response(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LocalLift</title><p style="font:18px/1.5 Helvetica,Arial,sans-serif;max-width:32em;margin:15vh auto;padding:0 16px">${text} <a href="/">Back to LocalLift</a>.</p>`, {headers: {'content-type': 'text/html; charset=utf-8'}});

  let d;
  try { d = plain ? Object.fromEntries(new URLSearchParams(await req.text())) : await req.json(); } catch { return reply(400, {ok: false}); }

  // Hidden field only automated sign ups fill in. Look successful, send nothing.
  if (clean(d.website, 200)) return plain ? page('Thanks. We have your request.') : reply(200, {ok: true});

  const out = {
    source: 'site',
    business: clean(d.business, 120),
    city: clean(d.city, 80),
    industry: clean(d.industry, 40),
    email: clean(d.email, 160).toLowerCase(),
  };
  if (!out.business || !out.city || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(out.email)) return plain ? page('Please go back and fill in your business, city and email.') : reply(422, {ok: false});

  try {
    const r = await fetch(process.env.AUDIT_HOOK_URL, {
      method: 'POST',
      headers: {'content-type': 'application/json'},
      body: JSON.stringify(out),
    });
    if (!r.ok) throw new Error('delivery');
  } catch {
    return plain ? page('That did not go through. Please email info@thesocialdm.com.') : reply(502, {ok: false});
  }
  return plain ? page('Thanks. We have your request. A real person will reply within one business day.') : reply(200, {ok: true});
};

export const config = {path: '/api/audit'};
