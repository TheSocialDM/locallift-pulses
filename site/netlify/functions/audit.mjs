// Audit form intake. Checks the request, then passes it to the delivery step.
const ALLOWED = /^https:\/\/(www\.localliftnow\.com|localliftnow\.com|([a-z0-9-]+--)?locallift-site-preview\.netlify\.app)$/;
const clean = (v, max) => String(v ?? '').replace(/[\r\n\t]+/g, ' ').trim().slice(0, max);
const reply = (status, body) => new Response(JSON.stringify(body), {status, headers: {'content-type': 'application/json'}});

export default async req => {
  if (req.method !== 'POST') return reply(405, {ok: false});
  if (!ALLOWED.test(req.headers.get('origin') || '')) return reply(403, {ok: false});

  let d;
  try { d = await req.json(); } catch { return reply(400, {ok: false}); }

  // Hidden field only automated sign ups fill in. Look successful, send nothing.
  if (clean(d.website, 200)) return reply(200, {ok: true});

  const out = {
    source: 'site',
    business: clean(d.business, 120),
    city: clean(d.city, 80),
    industry: clean(d.industry, 40),
    email: clean(d.email, 160).toLowerCase(),
  };
  if (!out.business || !out.city || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(out.email)) return reply(422, {ok: false});

  try {
    const r = await fetch(process.env.AUDIT_HOOK_URL, {
      method: 'POST',
      headers: {'content-type': 'application/json'},
      body: JSON.stringify(out),
    });
    if (!r.ok) return reply(502, {ok: false});
  } catch {
    return reply(502, {ok: false});
  }
  return reply(200, {ok: true});
};

export const config = {path: '/api/audit'};
