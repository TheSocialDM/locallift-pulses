# thesocialdm.com move to Netlify (read this first)

Goal: Michael wants the site live on Netlify within about 3 days of Nov 1 2026. Squarespace stays on until renewal (Apr 19 2027). Do the work, brief him after, ask only for his login, card or a live charge. Read memory: /areas/thesocialdm-site.md, /areas/socialdm-brand.md, /areas/lessons-log.md, /preferences.md.

## Build
    cd socialdm-site/tools && python3 build.py ../src ../export/socialdm-blog-export.json ../export/socialdm-blog-images.json ../new-posts ../dist --prod
Without --prod it makes a preview (relative .html links, noindex, Draft badge), for the artifact https://claude.ai/artifact/5P9vknbnA6UCZAMMnaL6Wc . Netlify publishes socialdm-site/dist from branch socialdm-site.

## Done
- All 38 posts at exact old URLs, text compared word for word to the export. Only changes: em and en dashes to commas, byline Victoria Richards to The SocialDM. 74 images are local.
- Carried pages: montage-tigard, pillar-communities, apartment-seo-for-multifamily-communities, apartment-seo-blog-hub/cuvee-apartments-westgate-glendale. Redirects in _redirects. Sitemap, robots, RSS, canonicals, article schema, 404.

## Still to do, in order
1. New posts: JSON files in new-posts/ (first 5 being written). Each needs an image file and an Editor pass, a fact check of every linked stat, then a separate approval. Real photos only.
2. Thin pages: Medical, Real Estate, Hospitality, Enterprise. About and Contact headline.
3. Claims: 60 to 90 days, 80%, 93%, 49 point. Verify or cut (new copy only; old post URLs stay).
4. Contact form goes live on Netlify Forms, routed through Make to Bird with BCC to info@thesocialdm.com; test end to end before launch. Glowing Ask AI box stays non submitting until the multifamily report delivers automatically.
5. Real work photos replace Pexels stand ins when he sends reel screenshots. Older post images look AI made and show made up dashboard figures; flag replacing them.
6. Netlify: new site from this repo, branch socialdm-site, publish directory socialdm-site/dist, no build command. Cloud cannot reach Netlify hosts, so he clicks this once (give the direct link and exact fields).
7. Before DNS: confirm where thesocialdm.com name servers and MX records live (Squarespace Domains shown), copy every record so info@thesocialdm.com never drops. Then point the domain, verify HTTPS, every old URL returns 200 or 301, submit sitemap in Search Console.
8. Editor plus Approval Assistant on the final site. Then set up the blog schedule (default 3 posts a week), newsletter and drips on Make and Bird, subscriptions on PayPal or Stripe when he is ready.
9. LocalLift Now (localliftnow.com, plan ends Feb 28 2027) must be moved before lapsing, keeping its URLs.
