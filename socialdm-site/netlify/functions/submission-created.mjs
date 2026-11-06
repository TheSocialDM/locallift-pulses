// Runs on Netlify ONLY for form submissions that passed Netlify's spam filter (verified).
// Spam that Netlify catches never reaches this function, so it never gets an auto reply.
// Forwards the verified lead to Make, which logs it in Airtable (Leads) and sends the
// confirmation from info@. Extra checks below flag obvious junk so it is logged but not answered.
const HOOK = "https://hook.us2.make.com/iohhty0efvjr39dni63w6nzco3wqp3t4";
const KEY = process.env.MAKE_FORM_SECRET || "d2b37a54193ac6ddab7c09feb321550357c1f1b2";

function flags(d) {
  const f = [];
  const msg = String(d.message || "");
  const all = [d.first_name, d.last_name, d.company, msg].join(" ");
  if ((msg.match(/https?:\/\/|www\./gi) || []).length > 0) f.push("link in message");
  if (/[Ѐ-ӿ一-鿿]/.test(all)) f.push("foreign script");
  if (/seo|backlink|crypto|casino|loan|viagra|guest post|rank your|first page of google|web design services/i.test(msg)) f.push("sales or spam words");
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(d.email || "").trim())) f.push("bad email");
  return f;
}

export const handler = async (event) => {
  try {
    const p = JSON.parse(event.body || "{}").payload || {};
    if (p.form_name !== "contact") return { statusCode: 200, body: "skip" };
    const d = p.data || {};
    const body = new URLSearchParams({
      source: "verified",
      key: KEY,
      first_name: d.first_name || "",
      last_name: d.last_name || "",
      email: d.email || "",
      phone: d.phone || "",
      company: d.company || "",
      interest: d.interest || "",
      message: d.message || "",
      site: p.site_url || "https://www.thesocialdm.com",
      sid: p.id || "",
      received: p.created_at || new Date().toISOString(),
      ip: d.ip || "",
      referrer: d.referrer || "",
      flags: flags(d).join(", ")
    });
    await fetch(HOOK, { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body });
    return { statusCode: 200, body: "ok" };
  } catch (e) {
    console.log("relay error", e && e.message);
    return { statusCode: 200, body: "error logged" };
  }
};
