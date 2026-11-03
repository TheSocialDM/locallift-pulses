# thesocialdm.com move to Netlify (read this first)

Goal: Michael wants the site live on Netlify within about 3 days of Nov 1 2026. Squarespace stays on until renewal (Apr 19 2027). Do the work, brief him after, ask only for his login, card or a live charge. Read memory: /areas/thesocialdm-site.md, /areas/socialdm-brand.md, /areas/lessons-log.md, /preferences.md.

## Build
    cd socialdm-site/tools && python3 build.py ../src ../export/socialdm-blog-export.json ../export/socialdm-blog-images.json ../new-posts ../dist --prod
Without --prod it makes a preview (relative .html links, noindex, Draft badge), for the artifact https://claude.ai/artifact/5P9vknbnA6UCZAMMnaL6Wc . Netlify publishes socialdm-site/dist from branch socialdm-site.

## Done
- All 38 posts at exact old URLs, text compared word for word to the export. Only changes: em and en dashes to commas, byline Victoria Richards to The SocialDM. 74 images are local.
- Carried pages: montage-tigard, pillar-communities, apartment-seo-for-multifamily-communities, apartment-seo-blog-hub/cuvee-apartments-westgate-glendale. Redirects in _redirects. Sitemap, robots, RSS, canonicals, article schema, 404.

## Session Nov 2 2026
- Build gate: tools/build.py --prod now skips any new-posts/*.json without "approved": true. Preview builds still show every draft. Set "approved": true only after Michael approves, then rebuild.
- All 5 drafts went through an Editor pass and a fact check (verification was through search results because Google, NAA, Apartment List and LocaliQ hosts are blocked from cloud). Fixes: survey sample wording, 85% wording, concession definition, LocaliQ "nearly 900 campaigns", cut unverifiable HUD 667,000 figure, GBP wording, AI Max link. Still need: image files, Michael's approval, his confirmation of client anecdotes ($2,690/$1,550 report, pages 2 to 6 audit, wrong photo ad, listing site rent errors), Google certifications line, "five states". search-engine-marketing links to /blog/multifamily-google-ads, so publish those together or cut the link.
- Claims: "60 to 90 days" (agency FAQ) replaced with baseline plus weekly reporting wording. "49 point" on home replaced with "Map grid" (no number) until Michael confirms grid size. Old posts untouched: 80% post misapplies Realtor.com Oct 2025 survey (82% of 1,000 US adults use AI for housing market info, not renters); renter surveys show 5% (Apartments.com via NAA, 2026) and 11.5% (SatisFacts 2025). 93% post: Semrush 2025 study is about Google AI Mode sessions only; title says "AI searches". Michael decides.
- Thin pages: Medical, Real Estate, Hospitality, Enterprise each got a "What is included" section, a 3 step start, and 3 FAQs. About got a "Who we are" section. Contact headline is now "Let's get you found before they choose."
- Contact form: Netlify Forms markup (name contact, honeypot, action /thank-you), new thank-you page (noindex, not in sitemap). Make scenario 6868372 "thesocialdm.com contact form to Bird (BCC info@)" with webhook https://hook.us2.make.com/iohhty0efvjr39dni63w6nzco3wqp3t4 sends the submitter a confirmation that echoes their message, BCC and reply to info@thesocialdm.com. INACTIVE until the Netlify site exists. It sends from hello@mail.localliftsignature.com (the only verified Bird domain) with the name The SocialDM; switch to mail.thesocialdm.com once that domain is added in Bird and its DNS records published.
- socialdm-site/netlify.toml added (publish dist, no command). Netlify MCP works from cloud now (team has 12 projects) but cannot link a GitHub repo, so the repo link click is still Michael's.
- DNS (read through Bird audit): MX thesocialdm-com.mail.protection.outlook.com (Microsoft 365). SPF v=spf1 include:spf.em.secureserver.net include:spf.protection.outlook.com -all. No DMARC. Microsoft 365 also needs autodiscover CNAME and DKIM selector1/selector2 CNAMEs if present; read the full zone in the DNS host before moving anything.

- Contact form delivery: Netlify outgoing notification never reached Make, so contact.html now also sends each submission from the browser to the Make webhook with navigator.sendBeacon (production only, skipped when the honeypot is filled). The Make scenario only acts on payloads with source=site, so a Netlify notification, if one exists, cannot send duplicates. Netlify still stores every submission.
- Netlify project "thesocialdm" (id 9d77552d-d658-4c5e-896a-415a32959593) created Nov 2 from branch socialdm-site, base socialdm-site, publish socialdm-site/dist. URL https://thesocialdm.netlify.app, currently behind Netlify team login (SSO, all deploys). Form detection enabled.

- Nov 2: 3 more drafts written (marketing metrics, lease-up, review responses). Michael approved all 8 ("approve all 8") after the review page https://claude.ai/artifact/N4VxgpALBgjhy2MtCvLbRA ; all have "approved": true and are in dist. He did not answer the per-post fact questions individually (client anecdotes, $2,690 report figures, Google certifications line, five states, one to two business day reply time); approval was taken as confirmation, and he was told to flag anything untrue before DNS cutover. 5 of 8 still have no photo; 3 use stand-in photos from src. Blog and articles now use a light "paper" layout (tools/blog.css).

- Contact confirmation now sends from info@thesocialdm.com through Microsoft 365 (Make connection 12095916, module microsoft-email:createAndSendAMessage), branded template in emails/contact-confirmation.html, BCC info@. Bird was dropped for this flow: the Bird plan allows one sending domain, used by mail.localliftsignature.com. End to end tested OK at 13:50 UTC Nov 2 via Bird; the Microsoft 365 version still needs one live test. The M365 mailbox display name is "Lead Designer"; Michael should rename it to The SocialDM.

- Nov 2 article upgrades (tools/build.py): all posts get reading time, "Updated" date when changed, BreadcrumbList schema, wordCount; Person author schema for Michael. New posts also get a hand written Key takeaways box ("takeaways" in each JSON), an H2 table of contents with anchor ids, and an author box. Related posts now score by shared title words. Old title "&nbsp;" display bug fixed. 5 new posts got Pexels photos (ids in "imageCredit"); network now allows images.pexels.com and images.unsplash.com but not their search pages, so find photo ids with WebSearch (allowed_domains pexels.com) and download from images.pexels.com.

- Nov 2 site SEO layer (tools/seo_layer.py, runs in --prod builds): keyword titles and meta descriptions for all static pages, Open Graph tags, Organization schema (address, founder, sameAs, areaServed) on home/about/contact, WebSite on home, Service schema on the 6 service pages, FAQPage from any .faq details block, Article on the 2026 report, a hidden plain link copy of the menu and footer inside #site-header/#site-footer for crawlers that do not run chrome.js (chrome.js replaces it for visitors), /llms.txt, and an IndexNow key file (7c2f9e41b85a4d6e9f03a1d2c4b6e8f0.txt) for Bing pings after launch.

- GA4: the Squarespace site used G-WJ6LRXJV21 (GA4 property "TheSocial DM", Windsor id 429000303). seo_layer.py now adds that tag to every production page, and thank-you fires generate_lead. Search Console has a URL prefix property https://www.thesocialdm.com/ with no meta verification tag in the old HTML, so it is verified by GA, DNS or file; keep GA tag and DNS TXT records. Windsor.ai has GA4, Search Console and GBP (locations/13937784954903437869 "The SocialDM") connected for reads.

- Social proof (tools/proof.py, markers <!--proof:communities--> and <!--proof:testimonials:GROUP--> in src pages): scrolling community name banner (tools/communities.json, names Michael approved; add logo files to tools/logos/ later) on home, multifamily, LocalLift; Google review ticker (tools/testimonials.json, verbatim first sentences of the 4 written Google reviews, 5.0 from 5) on home, multifamily, LocalLift, real estate. Refresh reviews by pulling google_my_business reviews for locations/13937784954903437869 via Windsor and updating testimonials.json. Michael approved: naming Montage in a case study, the community list, using his Google reviews.

- Scheduled publishing: netlify.toml now runs tools/build.py on Netlify (Python 3.12, requirements.txt), verified OK on deploy 6ae8affb. New posts with "approved": true and a future "date" stay hidden until that Phoenix date. Make scenario 6870143 "thesocialdm.com daily rebuild" (daily 05:05, INACTIVE) POSTs a Netlify build hook; Michael must create the hook (Netlify > Project configuration > Build & deploy > Build hooks, branch socialdm-site), paste its URL into the scenario's HTTP module, then activate it.
- Industry sections: posts carry "vertical" (multifamily default; old realtor titles map to real-estate). Topic hubs at /blog/topics/<vertical>, topic chips on /blog, and <!--posts:<vertical>--> "Latest insights" blocks on the industry pages and LocalLift. Writers are drafting 2 posts each for real estate, medical, hospitality, enterprise and 12 more multifamily posts (Nov 2).

- Reels: 9 reels from Dropbox /SocialDM/Website Reels (network allowlist now includes *.dropboxusercontent.com) compressed into src/reels/: <name>-loop.mp4 (432x768, 12s, silent, ~0.5MB) for the home page wheel, <name>.mp4 (720p with sound) for the tap-to-watch player, <name>.jpg poster. fx.js loads and plays loops only while the wheel is on screen and opens the full reel on tap (not on drag). Reduced motion shows posters only.

- The community name banner was replaced (Michael, Nov 2) by a "Trusted nationwide" stat ticker: tools/ticker.json (his 20 lines, e.g. 7,900+ doors, 20+ communities, five states) rendered by proof.ticker() with square stroke icons; same <!--proof:communities--> marker on home, multifamily, LocalLift. communities.json is kept for a future logo strip.

- Nov 2: Solutions menu order is LocalLift, Multifamily, Real Estate, Medical, LocalLift Signature, Hospitality, Enterprise. Medical page redesigned (photo hero, patient journey, animated Maps rank illustration labeled Illustration, Google ranking factors with source, KFF 29% stat, privacy band, medical ticker, LocalLift deliverables for practices, social trust section, 6 FAQs); its two posts are published. Real Estate page rebuilt in gold accents tied to LocalLift Signature: luxury home hero with glass cards, real estate ticker, two paths (individual agents = Signature $199/mo no contract, from Michael's Signature emails; teams and brokerages = custom), animated AI chat phone, fanned weekly post cards, deliverables for agents, reviews, FAQ, CTA. Deliverable tiles carry a LocalLift(TM) label; four descriptions tightened to outcomes so the method is not exposed.

## Still to do, in order
1. New posts: 5 drafts are in new-posts/, written and self checked but NOT yet through Editor or approval, and dist/ does not include them yet. Do not publish until they pass. Each needs an image file and an Editor pass, a fact check of every linked stat, then a separate approval. Real photos only.
2. Thin pages: Medical, Real Estate, Hospitality, Enterprise. About and Contact headline.
3. Claims: 60 to 90 days, 80%, 93%, 49 point. Verify or cut (new copy only; old post URLs stay). The writer found newer surveys showing 5% and 11.5% that undercut the live 80% post; check those sources and tell Michael, do not rewrite the old post without him.
4. Contact form goes live on Netlify Forms, routed through Make to Bird with BCC to info@thesocialdm.com; test end to end before launch. Glowing Ask AI box stays non submitting until the multifamily report delivers automatically.
5. Real work photos replace Pexels stand ins when he sends reel screenshots. Older post images look AI made and show made up dashboard figures; flag replacing them.
6. Netlify: new site from this repo, branch socialdm-site, publish directory socialdm-site/dist, no build command. Cloud cannot reach Netlify hosts, so he clicks this once (give the direct link and exact fields).
7. Before DNS: confirm where thesocialdm.com name servers and MX records live (Squarespace Domains shown), copy every record so info@thesocialdm.com never drops. Then point the domain, verify HTTPS, every old URL returns 200 or 301, submit sitemap in Search Console.
8. Editor plus Approval Assistant on the final site. Then set up the blog schedule (default 3 posts a week), newsletter and drips on Make and Bird, subscriptions on PayPal or Stripe when he is ready.
9. LocalLift Now (localliftnow.com, plan ends Feb 28 2027): RETIRED by Michael on Nov 2 2026 (Semrush: 8 keywords, ~0 organic traffic; renter facing, confused agency prospects). Footer card removed from thesocialdm.com. Before Feb 28 2027: keep the domain registered, inventory its URLs, then 301 every path to https://www.thesocialdm.com/blog (domain alias on a tiny Netlify redirect site with "/* https://www.thesocialdm.com/blog 301!"). Optionally rewrite the best renter guides as operator facing market reports on the blog and point their old URLs at those instead.

## Real estate page, second pass (Nov 2)
- iPhone style AI chat mockup (.iph), Instagram style post cards (avery.homes, sample), sample weekly report section (.mx) with animated line chart and metric tape, deliverables grid filled to 10 tiles (Site Read, Market Survey added).
- New photos (Pexels): p7641899 (+a avatar), p36729675, p8293700, p1669799.

## Med Spa and Hair Salon pages (Nov 2)
- New pages src/med-spa.html (rose accent) and src/hair-salon.html (lilac accent), generated from the real estate layout by scratchpad gen2/make.py (one off). Menu entries after Medical. Contact form has Med Spa and Hair Salon options (Make email switch falls to its default branch for these).
- Tickers ticker-med-spa.json / ticker-salon.json, deliverables-med-spa.json / deliverables-salon.json. proof.py now resolves any <!--proof:ticker:X--> and <!--proof:deliverables:X--> by file name.
- Blog verticals 'med-spa' and 'salon' registered; no posts yet.
- Post card fans on all three pages: float gently, spread with scroll position (--s), lift on hover.

## Hospitality rebuild and Portfolios (Nov 2)
- hospitality.html regenerated by scratchpad gen2/hosp.py (coral accent): AI trip planner iPhone, comp set table (visibility index, 100 = fair share), guest sentiment bars, weekly direct booking report, two paths, deliverables-hospitality.json, ticker-hospitality.json. Sharp photos p28408327 (hero), p1838554 (now 1600px), p16374109.
- enterprise.html rebuilt as Portfolios (teal accent) with animated dashboard; menu label Portfolios; URL unchanged.
- About intro no longer names founder, city or year.
- Reel wheel: play badges, hint pill, one intro flick (fx.js / fx.css).

## Go-live and Squarespace exit (Nov 2 2026)
- DNS for thesocialdm.com is hosted by Squarespace (GoDaddy registrar, nameservers connect1/2.squarespacedns.com). Squarespace Defaults deleted; added A @ 75.2.60.5 and CNAME www thesocialdm.netlify.app (30 min TTL). Email records (MX outlook, TXT NETORGFT..., google-site-verification, SPF) untouched.
- Netlify: www.thesocialdm.com and thesocialdm.com added, DNS verified. Still to do: set www.thesocialdm.com as primary once the certificate is issued (canonicals use www).
- Squarespace website plan for thesocialdm.com set to cancel; it EXPIRES APR 19 2027. BEFORE THEN (target March 2027): recreate all DNS records at GoDaddy, then switch GoDaddy nameservers to GoDaddy default, so email and site keep working.
- LocalLift Now site: set redirects to the new site before its plan ends.
- realestatebrandawareness.com is a Squarespace-registered domain (renews Oct 10 2027); left alone.

## Email signature (paused, Nov 2 2026) - PICK UP HERE
- Goal: replace WiseStamp ($85/yr) with a self-hosted signature that works in Apple Mail (Mac) on the Exchange account info@thesocialdm.com, and on iPhone.
- Hosted files: src/email/ (served at https://www.thesocialdm.com/email/). index.html = copy page; signature.html = current float layout; signature-body.html = table layout (used by the Terminal file method, do NOT reuse that method).
- Lessons: Apple Mail's signature pane strips tables, image sizes and (if "Always match my default message font" is ticked) all styles. Writing the .mailsignature file directly made iPhone show raw MIME; reverted (files unlocked with chflags nouchg). Do not have Michael run Terminal again.
- Next step when Michael returns: he sends WiseStamp's "Copy HTML code" output (as a plain text file). Rebuild our design (full color logo-full.png left, The SocialDM | LocalLift, tagline, gradient bar, website, email, IG/FB/TikTok/YouTube icons, "Free AI visibility check" to /contact) on WiseStamp's proven structure, test, then one paste.
- Open questions: X and LinkedIn URLs for icons (x.png, linkedin.png already made).
- Meanwhile Michael uses WiseStamp's "Apple Mail for Mac" install.

## Nov 3 2026: 4 posts published at Michael's request (2 medical, 2 real estate)
- open-enrollment-new-patients-january, cold-flu-season-same-day-patients (medical); real-estate-agent-marketing-plan-2027, real-estate-short-form-video (real estate). All dated Nov 3, "approved": true (Michael asked directly for them to go live).
- Facts checked through search results only (cms.gov, cdc.gov, nar.realtor, hud.gov and support.google.com are blocked from cloud). NAR referral figures (43% buyers, 66% sellers) come from the Virginia REALTORS summary of the 2025 Profile; confirm against NAR if challenged.
- Links to the Nov 6 (real-estate-agents-ai-search) and Dec 4 (google-business-profile-real-estate-agents) posts were left out because those are not live yet. Add them to real-estate-agent-marketing-plan-2027 after Dec 4 if wanted.
