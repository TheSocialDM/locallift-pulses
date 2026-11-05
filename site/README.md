# LocalLift website (private preview)

Rebuild of the approved homepage prototype as a real, multi page static site.

* `src/proto.js` holds the page components (React with htm), shared by the server render and the browser.
* `src/pages.js` holds the industry pages and the page registry.
* `src/meta.mjs` holds page titles, descriptions, schema and FAQs.
* `node build.mjs` renders every page to real HTML in `dist/`, then the browser hydrates it.
* `node check.mjs` checks the copy rules: no dashes, no named data sources or tools, door counter capped at 7,900, audit form collects nothing.

Preview builds are `noindex` (meta tag, `X-Robots-Tag` header and `robots.txt`). Build with `LIVE=1` for the live site (no noindex). The committed dist is the live build.
The audit form is switched off on purpose: it has no action, no field names and a disabled fieldset.
