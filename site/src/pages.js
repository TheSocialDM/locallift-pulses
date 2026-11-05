
/* ---------- industry pages ---------- */
const IND_SLUG={"Multifamily":"multifamily","Build to Rent":"build-to-rent","Medical":"medical","Med Spa":"med-spa","Real Estate":"real-estate","Hair Salons":"hair-salons","Hospitality":"hospitality","Portfolios":"portfolios"};
function indHref(x){return '/industries/'+IND_SLUG[x.t]+'/'}

const IND_COPY={
 "Multifamily":{
  plural:"apartment communities",sample:"Sample community",
  h1:["Renters decide who to tour ","before they call."],
  sub:"LocalLift shows how your communities appear when renters search Google, scan Google Maps and ask AI assistants, then keeps every property visible, accurate and chosen through lease up and beyond.",
  card:"Communities, lease ups and stabilized assets.",
  pains:[["Specials go stale online.","A concession ends on your website but lives on in your Google profile and in AI answers. Renters arrive expecting a price you no longer offer."],
   ["Rank depends on the street.","A community can lead the map from its leasing office and vanish a mile away, right where your next renter works."],
   ["AI builds the shortlist.","Renters ask AI assistants which communities allow large dogs or sit near the office. If you are not named, you are not toured."]],
  does:[["Market Survey","Every Sunday, competitor asking rents, effective rents and specials, side by side with yours."],
   ["Map Reach","Weekly Google Maps rank across the neighborhoods your renters come from, not only from the leasing office."],
   ["AI Shortlist","The renter questions that matter, asked every week, with the communities AI names instead of you."],
   ["Site Read","Checks that your pricing, specials and pet policy read the same on your website, your Google profile and in AI answers."],
   ["Review Desk","Resident review responses in your voice, written with fair housing in mind."],
   ["Daily Presence","A Google post every day about your community, your neighborhood and what is happening this week."]]},
 "Build to Rent":{
  plural:"build to rent communities",sample:"Sample build to rent community",
  h1:["Renters want the yard. ","Help them find yours."],
  sub:"Build to rent is still new to many searchers. LocalLift helps Google and AI assistants explain your community clearly, so renters who want a house without buying one find you.",
  card:"Single family rental communities, from first phase to fully leased.",
  pains:[["The category needs explaining.","Many renters do not search for build to rent by name. They search for homes for rent with a yard, and your community has to show up for that."],
   ["AI answers fill the gap.","When someone asks how build to rent differs from renting a house, the answer shapes who they tour. You want to be the example."],
   ["Lease up moves fast.","New phases, new pricing and new amenities change often. Every listing has to keep up, or renters see last month's story."]],
  does:[["AI Shortlist","Weekly checks on whether AI assistants name your community for the questions renters actually ask."],
   ["Site Read","Makes sure phases, pricing and amenities read the same on your website, your Google profile and in AI answers."],
   ["Map Reach","Google Maps rank across the neighborhoods and commute routes renters care about."],
   ["Daily Presence","Daily Google posts that explain the community, the homes and the neighborhood in plain language."],
   ["Market Survey","What nearby rentals and other communities are offering, every Sunday."],
   ["Weekly Pulse","One page every Friday on what moved and the one next step for your lease up."]]},
 "Medical":{
  plural:"medical practices",sample:"Sample practice",
  h1:["Patients check you ","before they call."],
  sub:"After a referral, many patients search the practice, compare ratings and ask AI who is well reviewed nearby. LocalLift keeps your hours, locations and reputation accurate everywhere they look.",
  card:"Practices, specialists and groups with several locations.",
  pains:[["Details drift across listings.","Old hours, a moved suite or a retired provider can linger on Google and in AI answers, and patients call the wrong place."],
   ["Reviews carry the decision.","Patients read how a practice answers reviews. Silence reads as neglect, and a careless reply can expose private details."],
   ["Specialists compete street by street.","A patient searching from home sees a different list than one searching from the hospital campus."]],
  does:[["Site Read","Checks that hours, locations, providers and services match across your website, your Google profile and AI answers."],
   ["Review Desk","Review responses in your voice that never confirm someone is a patient and never discuss care."],
   ["AI Shortlist","Whether AI assistants name your practice when patients ask who is well reviewed for your specialty nearby."],
   ["Map Reach","Google Maps rank across the neighborhoods your patients drive from."],
   ["Snapshot","Your monthly Google report: searches, views, calls and direction requests."],
   ["Weekly Pulse","One page every Friday, short enough to share with the practice manager."]]},
 "Med Spa":{
  plural:"med spas",sample:"Sample med spa",
  h1:["First time clients read everything. ","Make it worth reading."],
  sub:"Someone choosing a first treatment studies photos, reviews and every answer an AI assistant gives. LocalLift keeps your med spa visible, current and trusted across all of it.",
  card:"Med spas, aesthetics studios and wellness clinics.",
  pains:[["Reputation is the product.","Clients choose the med spa that looks established. Thin photos and unanswered reviews send them to the name that looks busier."],
   ["Offers change monthly.","Seasonal pricing and new treatments need to read the same on your website, your Google profile and in AI answers."],
   ["Near work matters.","Many clients book close to the office, not home. Your map rank needs to hold where they spend the day."]],
  does:[["AI Shortlist","Whether AI assistants name your med spa when people ask who has the best reputation nearby."],
   ["Review Desk","Thoughtful review responses in your voice, written with client privacy in mind."],
   ["Daily Presence","Daily Google posts on treatments, aftercare tips, your team and this month's offer."],
   ["Map Reach","Google Maps rank across the office districts and neighborhoods your clients come from."],
   ["Site Read","Checks that treatments, pricing and offers match everywhere a client looks."],
   ["Snapshot","Your monthly Google report: searches, views, calls and website clicks."]]},
 "Real Estate":{
  plural:"real estate agents",sample:"Sample agent",
  h1:["Sellers pick the agent ","who looks current."],
  sub:"Before a homeowner calls, they search your name, read your reviews and ask AI who knows their part of town. LocalLift helps make sure the answer includes you.",
  card:"Agents, teams and brokerages.",
  pains:[["Activity signals expertise.","A Google profile with no recent posts looks retired, even when your calendar is full."],
   ["Neighborhoods are the battleground.","Sellers want the agent who knows their streets. Your visibility has to hold neighborhood by neighborhood."],
   ["AI names a few agents.","When a homeowner asks who the best listing agent nearby is, a short list forms in seconds."]],
  does:[["AI Shortlist","Whether AI assistants name you when homeowners ask who knows their neighborhood best."],
   ["Map Reach","Google Maps rank across every neighborhood you want listings from."],
   ["Review Desk","Client review responses in your voice, so every reply adds to your reputation."],
   ["Daily Presence","Daily Google posts on listings, sales, market notes and the neighborhoods you serve."],
   ["Snapshot","Your monthly Google report: profile views, calls and website clicks."],
   ["Weekly Pulse","One page every Friday on what moved and the one next step."]]},
 "Hair Salons":{
  plural:"hair salons",sample:"Sample salon",
  h1:["New neighbors need a salon ","by Saturday."],
  sub:"People new to the area search, scan photos and check hours on their phone, then book the salon that looks open and active. LocalLift keeps your salon in that first look.",
  card:"Salons, barbers and independent stylists.",
  pains:[["Hours decide the booking.","If Saturday hours are wrong anywhere, a ready client books somewhere else."],
   ["Photos do the selling.","Searchers judge the work before they read a word. Fresh photos and recent posts show the chairs are full."],
   ["Specialties get asked about.","People ask AI assistants which salon is best with curly hair or color correction nearby. You want to be named for what you do best."]],
  does:[["Map Reach","Google Maps rank across the neighborhoods around your salon, street by street."],
   ["Review Desk","Review responses in your voice, so happy clients feel thanked and new ones see you care."],
   ["Daily Presence","Daily Google posts on cuts, color, your stylists and open appointments."],
   ["Snapshot","Your monthly Google report: searches, calls and direction requests."],
   ["AI Shortlist","Whether AI assistants name your salon for the specialties you are known for."],
   ["Site Read","Checks that hours, services and prices match everywhere."]]},
 "Hospitality":{
  plural:"hotels and stays",sample:"Sample hotel",
  h1:["Travelers plan the trip ","in an AI answer."],
  sub:"Guests ask which stay fits a quiet weekend, check the walk to dinner on Google Maps, then book the place that kept appearing. LocalLift works to keep your property in that answer.",
  card:"Boutique hotels, inns and short stay properties.",
  pains:[["Booking sites own the first click.","Your own Google profile and website need to give travelers a reason to book with you directly."],
   ["Every trip has a reason.","Anniversaries, conferences, game weekends. AI answers match stays to reasons, and you want to match more of them."],
   ["Recent beats beautiful.","Travelers trust recent photos and recent replies over polished pictures from three years ago."]],
  does:[["AI Shortlist","Whether AI assistants recommend your property for the trips travelers describe."],
   ["Review Desk","Guest review responses in your voice, posted while the stay is still fresh."],
   ["Snapshot","Your monthly Google report: searches, views, calls and website clicks."],
   ["Daily Presence","Daily Google posts on rooms, dining, events and what is happening nearby."],
   ["Map Reach","Google Maps rank from the places guests start their search: the station, the stadium, the old town."],
   ["Site Read","Checks that amenities, policies and rates read the same everywhere."]]},
 "Portfolios":{
  plural:"portfolios",sample:"Sample portfolio",
  h1:["One clear read ","on every property."],
  sub:"Owners and operators see every property side by side, on the same measures, with one recommended move for each. LocalLift turns a stack of reports into one decision.",
  card:"Owners, operators and asset managers.",
  pains:[["Every site reports differently.","Different vendors and different measures make properties hard to compare, and the weakest one hides."],
   ["Problems surface late.","A property can slip behind its local competitors for weeks before occupancy or leads show it."],
   ["Attention is limited.","You cannot fix everything at once. You need to know which move counts most this week."]],
  does:[["Lift Score","The same score on every property, so you can see which are getting easier to find and which are slipping."],
   ["Weekly Pulse","One page per property every Friday, with one recommended next step for each."],
   ["Market Survey","Competitor pricing and specials around every property, every Sunday."],
   ["AI Shortlist","Which properties AI assistants name, and which they skip."],
   ["Snapshot","Monthly Google results for every property, in one consistent format."],
   ["ClearView","Monthly social results across the portfolio: what posted, what performed, what changes next."]]},
};

function IndJourney({d}){
  const[ref,seen,vis]=useInView(.15);const labels=d.labels||JLABEL;
  return html`<div ref=${ref}>
      <p className="journey-who">${d.who}</p>
      <div className="journey">
        <div className="track"><span className="traveler"></span></div>
        ${d.s.map((t,k)=>html`<div className="j-step" key=${k}><h3>${labels[k]}</h3><p>${t}</p></div>`)}
      </div>
      <div className="ia">
        <div>
          ${d.doors?html`<div className="ia-city">Multifamily doors we work across</div><div className="ia-big"><i className="live-dot"></i><span><${Doors}/>+</span></div><div className="ia-sub">doors and counting</div>`
            :html`<div className="ia-big"><${Count} to=${+d.big[0]} run=${seen}/></div><div className="ia-sub">${d.big[1]}</div>`}
          ${d.doors?html`<div className="ia-city" style=${{margin:'20px 0 -6px'}}>Sample figures</div>`:null}<div className="ia-stats">${d.stats.map(s=>html`<div key=${s[1]}><strong>${s[0]}</strong><span>${s[1]}</span></div>`)}</div>
        </div>
        <div>
          <div className="ia-city">${d.city}. Fake numbers.</div>
          <div className="viz" style=${{marginTop:0}}>
            <${Pops} items=${d.pops} run=${vis}/>
            <div className="viz-t">${d.metric}</div>
            <${Bars} data=${d.d} labels=${d.labels2||M6} run=${seen} name=${d.metric} height=${210} hi=${d.labels2?d.d.indexOf(Math.max(...d.d)):null}/>
          </div>
        </div>
      </div>
      <div className="sample" style=${{marginTop:'14px'}}>Sample journey, sample place and sample charts. Illustrative only.</div>
  </div>`;
}

function IndTools({d,c}){
  const names=c.does.map(x=>x[0]);const[tool,setTool]=useState(names[0]);
  const T=TOOLS.find(t=>t.n===tool);const mine=c.does.find(x=>x[0]===tool);
  return html`<div className="console" style=${{marginTop:'40px'}}>
      <div className="console-bar"><span>LocalLift Intelligence / ${c.sample}</span><span>Illustrative panels. A separate sample from the chart above.</span></div>
      <div className="console-body">
        <div className="rail" role="group" aria-label="LocalLift tools">
          ${names.map(n=>{const t=TOOLS.find(x=>x.n===n);return html`<button key=${n} aria-pressed=${n===tool} onClick=${()=>setTool(n)}><span>${n}</span><small>${t.c}</small></button>`})}
        </div>
        <div className="panel fade" key=${tool}>
          <div className="panel-head"><h3>${T.n}</h3><span className="sample">${T.c}</span></div>
          <p className="panel-desc">${mine[1]}</p>
          <div className="panel-body">${T.b({ind:true})}</div>
        </div>
      </div>
    </div>`;
}

function Faq({items,dark}){
  if(!items||!items.length)return null;
  return html`<section className=${'band '+(dark?'char':'white')} id="faq"><div className="wrap faq-wrap">
    <div><${Eyebrow}>Questions<//><h2 className="title">Answers, <em>before you ask.</em></h2></div>
    <div className="faq">${items.map((f,i)=>html`<details key=${i} open=${i===0}><summary>${f[0]}</summary><p>${f[1]}</p></details>`)}</div>
  </div></section>`;
}

function IndustryPage({name}){
  const d=IND.find(x=>x.t===name),c=IND_COPY[name];
  return html`<div><${Nav}/><main id="main">
    <section className="hero ind-hero"><${HeroCanvas}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span aria-current="page">${name}</span></nav>
        <h1>${c.h1[0]}<em>${c.h1[1]}</em></h1>
        <p className="sub">${c.sub}</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a><a className="btn ghost" href="#journey">See the journey</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <div className="statement"><div className="wrap statement-in"><span>Be found.</span><span>Be understood.</span><span>Be chosen.</span>${d.doors?html`<${DoorsStat}/>`:null}</div></div>
    <section className="band char"><div className="wrap">
      <${Eyebrow}>The visibility problem for ${c.plural}<//>
      <h2 className="title" style=${{maxWidth:'16em'}}>Where the customer slips away, <em>and why.</em></h2>
      <div className="pains">${c.pains.map((p,i)=>html`<article className="pain" key=${i}><b>0${i+1}</b><h3>${p[0]}</h3><p>${p[1]}</p></article>`)}</div>
    </div></section>
    <section className="band white" id="journey"><div className="wrap">
      <${Eyebrow}>The customer journey<//>
      <h2 className="title" style=${{maxWidth:'15em'}}>Four moments decide <em>who gets chosen.</em></h2>
      <${IndJourney} d=${d}/>
    </div></section>
    <section className="band mist" id="intelligence"><div className="wrap">
      <${Eyebrow}>What LocalLift does for ${c.plural}<//>
      <h2 className="title" style=${{maxWidth:'15em'}}>The tools that matter here, <em>run for you.</em></h2>
      <p className="lede">We run the tools and tell you what they mean. You get the answer and one next step, not another login.</p>
      <div className="does">${c.does.map(x=>{const t=TOOLS.find(y=>y.n===x[0]);return html`<div className="do" key=${x[0]}><small>${t.c}</small><h3>${x[0]}</h3><p>${x[1]}</p></div>`})}</div>
      <${IndTools} d=${d} c=${c}/>
    </div></section>
    <${Faq} items=${FAQS[name]}/>
    <section className="band white" style=${{paddingTop:0}}><div className="wrap">
      <${Eyebrow}>Other industries<//>
      <div className="others">${IND.filter(x=>x.t!==name).map(x=>html`<a key=${x.t} href=${indHref(x)}>${x.t}</a>`)}</div>
    </div></section>
    <${Audit} industry=${name}/>
  </main><${Footer}/></div>`;
}

function IndustriesIndex(){
  return html`<div><${Nav}/><main id="main">
    <section className="hero ind-hero"><${HeroCanvas}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><span aria-current="page">Industries</span></nav>
        <h1>Built for businesses people <em>search for nearby.</em></h1>
        <p className="sub">Every customer takes a different path to the same decision. LocalLift follows that path across Google Search, Google Maps and AI answers for eight kinds of local business.</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <section className="band white"><div className="wrap">
      <${Eyebrow}>Choose your industry<//>
      <h2 className="title">Eight industries. <em>One loop.</em></h2>
      <div className="ind-cards">${IND.map(x=>html`<a className="card" key=${x.t} href=${indHref(x)}><span className="sample">Industry</span><h3>${x.t}</h3><p>${IND_COPY[x.t].card}</p><em>See LocalLift for ${x.t}</em></a>`)}</div>
    </div></section>
    <${Industries}/>
    <${Faq} items=${FAQS.Industries} dark=${true}/>
    <${Audit}/>
  </main><${Footer}/></div>`;
}

/* ---------- page registry ---------- */
const FAQS={
 Home:[
  ["What is LocalLift?","LocalLift is a local visibility service from The SocialDM. We show how your business appears across Google Search, Google Maps and AI answers, then do the work to strengthen it: daily Google posts, review responses, content and weekly reporting."],
  ["How do you know what AI assistants say about my business?","Every week we ask the leading AI assistants the questions your customers ask, and record who gets named. You see where you appear, where you do not, and who is named instead."],
  ["Do I need to learn a new platform?","No. There is no dashboard to log in to. Our team runs the tools and sends written reports you can read in minutes and forward to ownership."],
  ["What do I receive each week?","A Weekly Pulse every Friday with one recommended next step, plus weekly reads on your map rank, AI answers and listing accuracy. Snapshot and ClearView reports arrive monthly."],
  ["Does LocalLift replace my website or my ads?","No. LocalLift works alongside them. It strengthens how you appear in organic search, on Google Maps and in AI answers, where many local decisions start."],
  ["Are the numbers on this site real?","The door count, the weekly post count and the case study are real. Every number, chart, business and city in the samples is made up to show what our reports look like."],
  ["How do I get started?","Request a Visibility Audit with the form on this page. A real person replies within one business day."]],
 Industries:[
  ["Which industries does LocalLift work with?","Multifamily, build to rent, medical practices, med spas, real estate agents, hair salons, hospitality and portfolios of many properties."],
  ["Is the service different for each industry?","The loop is the same: discover, compare, strengthen and measure. The questions we track, the competitors we watch and the content we write change for each industry."],
  ["My industry is not listed. Can you still help?","If customers search for you nearby, the same approach applies. Contact The SocialDM and we will tell you honestly whether LocalLift fits."],
  ["Do you work with groups and multi location businesses?","Yes. Portfolio reporting puts every location side by side on the same measures, with one recommended move for each."]],
 "Multifamily":[
  ["How does LocalLift help apartment communities?","We track how renters find your community on Google Search, Google Maps and AI answers, fix what is wrong or out of date, and keep your Google presence active every day. Every Friday you get one page on what moved and one next step."],
  ["Do you track competitor rents and specials?","Yes. Market Survey compares asking rents, effective rents and specials at your competitors every Sunday, side by side with yours."],
  ["Are review responses written with fair housing in mind?","Yes. Every response is written in your voice, stays neutral and never references a protected characteristic or a resident's personal details."],
  ["Do you work with lease ups as well as stabilized communities?","Yes. Lease ups need visibility fast and change often. Stabilized communities need to hold their place against newer competitors. The weekly loop covers both."],
  ["How large is your multifamily portfolio?","LocalLift works across more than 7,900 doors, and counting."]],
 "Build to Rent":[
  ["What makes build to rent visibility different?","Many renters do not yet search for build to rent by name. Your community has to appear for the searches they do make, like homes for rent with a yard, and be explained clearly when they ask AI assistants."],
  ["Do you support communities still in lease up?","Yes. We keep phases, pricing and amenities current across your website, your Google profile and AI answers as they change."],
  ["Can you control what AI assistants say about us?","No one can control AI answers directly. We track what they say every week, correct the sources they draw on, and publish clear content so the answers improve over time."],
  ["Do you track nearby rentals and other communities?","Yes. Market Survey watches nearby offers every Sunday so you know what renters are comparing you with."]],
 "Medical":[
  ["Is your review response process safe for patient privacy?","Yes. Responses never confirm that someone is a patient and never discuss care. We do not need access to patient records."],
  ["Can you fix wrong hours, addresses or provider details?","Yes. Site Read checks your details across your website, your Google profile and AI answers every week, and we correct what is out of date."],
  ["Do you work with practices that have several locations?","Yes. Each location is tracked on its own, and portfolio reporting shows every location side by side."],
  ["Will this replace our website or patient marketing?","No. LocalLift works alongside them and focuses on how patients find and judge your practice before they call."]],
 "Med Spa":[
  ["How do you help a med spa get recommended by AI assistants?","We track the questions clients ask every week, see which med spas are named, and strengthen the reviews, posts and details AI answers draw on."],
  ["Can you promote our monthly offers?","Yes. Daily Presence posts feature current offers and treatments, and Site Read checks that the offer reads the same everywhere."],
  ["Do your posts make claims about treatment results?","No. Posts and review replies stay factual, avoid promising outcomes and respect client privacy."],
  ["How soon will we see changes?","Some fixes, like correct hours or a current offer, show within days. Map rank and AI answers move over weeks, which is why we report every week."]],
 "Real Estate":[
  ["Do you work with individual agents or teams?","Both. LocalLift works for a single agent, a team or a brokerage with many profiles."],
  ["Can you help me show up in specific neighborhoods?","Yes. Map Reach measures your Google Maps rank across the neighborhoods you choose, and your posts and content are written for those same areas."],
  ["Do I need to write the posts myself?","No. We write and publish daily Google posts on your listings, sales and market notes. You can review them whenever you like."],
  ["How do you handle client reviews?","Review Desk answers every review in your voice, so each reply adds to your reputation instead of sitting unanswered."]],
 "Hair Salons":[
  ["Does LocalLift work for a single salon?","Yes. LocalLift runs for you, so one salon gets the same weekly work without adding to the front desk."],
  ["Do you need our photos?","Your own photos work best. Share them with us and we will put them to work in your daily Google posts."],
  ["How do you handle a negative review?","Calmly and in your voice. We thank the client, acknowledge the concern and invite them to talk with you directly."],
  ["Will our hours and services stay correct online?","Yes. Site Read checks hours, services and prices across your website, your Google profile and AI answers every week."]],
 "Hospitality":[
  ["Can LocalLift help us earn more direct bookings?","We strengthen your own Google profile and website so travelers have a reason to book with you directly, and we report the calls and website clicks that come from Google."],
  ["How do you respond to guest reviews?","In your voice, while the stay is still fresh. Thoughtful replies show future guests that someone is paying attention."],
  ["Do you track how AI assistants recommend hotels?","Yes. Every week we ask the trip questions your guests ask and record which properties are named."],
  ["Do you work with groups of properties?","Yes. Portfolio reporting shows every property side by side on the same measures."]],
 "Portfolios":[
  ["How do you compare properties in different markets?","Each property is measured against its own local market, then scored on the same Lift Score, so a portfolio view is a fair comparison."],
  ["Can ownership read the reports directly?","Yes. Every report is written to be read in minutes and forwarded as it is."],
  ["How many properties can you cover?","From a handful to a full portfolio. Each property gets the same weekly read and one recommended move."],
  ["Do property teams need to change how they work?","No. There is no new login. Teams receive one clear next step each week, and our team does the visibility work."]],
};
const PAGES={home:App,industries:IndustriesIndex};
IND.forEach(x=>{PAGES['ind:'+x.t]=()=>html`<${IndustryPage} name=${x.t}/>`});
