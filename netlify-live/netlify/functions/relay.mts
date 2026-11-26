// LocalLift secure relay. App pages post here instead of straight to Make.
// Make webhook addresses and the relay key live only in Netlify secret env vars.
import type { Config, Context } from "@netlify/functions"

const HOOKS: Record<string, string> = {
  snap: "HOOK_SNAP",       // Snap for Social photos
  vid: "HOOK_VID",         // video upload link + done
  ping: "HOOK_PING",       // app activity alerts
  team: "HOOK_TEAMOPEN",   // team and promo landing page opened
  rep: "HOOK_REP",         // Rep HQ activity
  specials: "HOOK_SPECIALS" // agent page specials sign up
}

const ORIGINS = new Set([
  "https://live.thesocialdm.com",
  "https://thesocialdm.github.io",
  "https://www.thesocialdm.com",
  "https://thesocialdm.com",
  "https://moveinlocal.com",
  "https://www.moveinlocal.com",
])

const MAX = 5_500_000

const cors = (origin: string | null): Record<string, string> =>
  origin && ORIGINS.has(origin)
    ? { "Access-Control-Allow-Origin": origin, "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type", Vary: "Origin" }
    : {}

export default async (req: Request, context: Context) => {
  const origin = req.headers.get("origin")
  const h = cors(origin)
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: h })
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405, headers: h })
  if (!origin || !ORIGINS.has(origin)) return new Response("Forbidden", { status: 403 })

  const name = context.params.hook || ""
  const envKey = HOOKS[name]
  const target = envKey ? Netlify.env.get(envKey) : undefined
  const key = Netlify.env.get("RELAY_KEY")
  if (!target || !key) return new Response("Not found", { status: 404, headers: h })

  const len = Number(req.headers.get("content-length") || "0")
  if (len > MAX) return new Response("Too large", { status: 413, headers: h })

  const type = (req.headers.get("content-type") || "").toLowerCase()
  let body: BodyInit
  const headers: Record<string, string> = {}
  try {
    if (type.includes("multipart/form-data")) {
      const fd = await req.formData()
      fd.append("relay_key", key)
      body = fd
    } else if (type.includes("application/x-www-form-urlencoded")) {
      const p = new URLSearchParams(await req.text())
      p.append("relay_key", key)
      body = p.toString()
      headers["Content-Type"] = "application/x-www-form-urlencoded"
    } else if (type.includes("application/json")) {
      const j = await req.json()
      body = JSON.stringify({ ...(j && typeof j === "object" ? j : { data: j }), relay_key: key })
      headers["Content-Type"] = "application/json"
    } else {
      const p = new URLSearchParams(await req.text())
      p.append("relay_key", key)
      body = p.toString()
      headers["Content-Type"] = "application/x-www-form-urlencoded"
    }
  } catch {
    return new Response("Bad request", { status: 400, headers: h })
  }

  try {
    const r = await fetch(target, { method: "POST", body, headers })
    const out = await r.text()
    return new Response(out, {
      status: r.status,
      headers: { ...h, "Content-Type": r.headers.get("content-type") || "text/plain", "Cache-Control": "no-store" },
    })
  } catch {
    return new Response("Upstream error", { status: 502, headers: h })
  }
}

export const config: Config = {
  path: "/api/r/:hook",
  rateLimit: { action: "rate_limit", aggregateBy: ["ip", "domain"], windowSize: 60, windowLimit: 120 },
}
