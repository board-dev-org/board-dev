import pathlib, re
root = pathlib.Path(__file__).parent

import hashlib
CSSV = hashlib.md5((pathlib.Path(__file__).parent/"style.css").read_bytes()).hexdigest()[:8]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="style.css?v={cssv}">
<!-- Google Analytics (GA4) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MXGZ3Y4XRG"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-MXGZ3Y4XRG');</script>
<!-- HubSpot tracking -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/45089564.js"></script>
</head>
<body>
"""

NAV = """<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" alt="Board.Dev" width="229" height="32"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="menu" onclick="var m=document.getElementById('menu');m.classList.toggle('open');this.setAttribute('aria-expanded',m.classList.contains('open'))">Menu ☰</button>
    <ul class="nav-links" id="menu">
      <li><a href="what-we-do.html"{a1}>What We Do</a></li>
      <li><a href="resources.html"{a2}>Resources</a></li>
      <li><a href="about-us.html"{a3}>About</a></li>
      <li><a class="btn" href="get-in-touch.html">Get in touch</a></li>
    </ul>
  </div>
</header>
<main>
"""

NEWSLETTER = """<section class="section"><div class="wrap">
  <div class="newsletter">
    <h2>Join our newsletter for updates</h2>
    <a class="btn btn-light" href="newsletter.html">Subscribe</a>
  </div>
</div></section>
"""

FOOT = """</main>
<footer>
  <div class="wrap">
    <div>
      <a class="logo" href="index.html"><img src="assets/img/logo-white.png" alt="Board.Dev" width="229" height="32"></a>
      <p>Copyright © 2026 Board.Dev – All Rights Reserved.</p>
      <p>Board.Dev is a social enterprise fiscally sponsored by <a href="https://www.communityin.org/" target="_blank" rel="noopener">Community Initiatives</a>, a 501©(3). Engagements can be structured as corporate partnerships or tax-deductible charitable contributions.</p>
      <p><a href="privacy-policy.html">Privacy Policy</a></p>
    </div>
    <ul>
      <li><a href="what-we-do.html">What We Do</a></li>
      <li><a href="resources.html">Resources</a></li>
      <li><a href="about-us.html">About</a></li>
      <li><a class="btn" href="get-in-touch.html">Get in touch</a></li>
    </ul>
  </div>
</footer>
<script>
document.querySelectorAll('.video[data-id]').forEach(function(a){
  a.addEventListener('click',function(e){
    e.preventDefault();
    var id=a.dataset.id, t=a.querySelector('.thumb');
    t.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="Video" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    a.classList.add('playing');
  });
});
</script>
</body>
</html>
"""

DOTS = """<svg class="dots" viewBox="0 0 140 60" aria-hidden="true">
<circle cx="112" cy="24" r="18" fill="#c92240"/><circle cx="80" cy="34" r="9" fill="#c92240"/>
<circle cx="58" cy="22" r="4" fill="#c92240"/><circle cx="62" cy="42" r="3" fill="#c92240"/>
<circle cx="42" cy="32" r="2.5" fill="#c92240"/><circle cx="96" cy="48" r="3" fill="#c92240"/></svg>"""

pages = {}

# ---------- HOME ----------
pages["index.html"] = dict(title="Board.Dev", desc="Board.Dev builds the boards nonprofits need for the AI era.", active=0, body=f"""
<section class="section" style="padding-top:24px"><div class="wrap">
  <div class="hero">
    <h1>Leadership is the only tech skill that doesn't go out of style.</h1>
    <p>Companies need leaders who can navigate the AI era. So do the nonprofits they support. Board.Dev builds both—connecting business leaders across marketing, finance, HR, operations, and technology with nonprofits where strategic decisions matter.</p>
    {DOTS}
  </div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="two">
    <div>
      <h3>Building the Leadership Nonprofits Need to Make AI Work.</h3>
      <p>A new co-publication of Board.Dev and Dell Technologies based on a national nonprofit survey—a hard look at why the sector is stuck and what leadership teams can do about it.</p>
      <a class="btn btn-navy" href="assets/pdfs/board-dev-dell-building-the-leadership-nonprofits-need-to-make-ai-work.pdf" target="_blank" rel="noopener">Read the report</a>
    </div>
    <div>
      <h3>What can my board do that AI can't?</h3>
      <p>Thirty nonprofit CEOs, funders, and board chairs spent an afternoon in San Francisco on that question.<br>The first dispatch from our 2026 field research, with Okta and AWS.</p>
      <a class="btn btn-navy" href="assets/pdfs/board-dev-sf-dispatch.pdf" target="_blank" rel="noopener">Read the dispatch</a>
    </div>
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <div class="callout">
    <h2>92% of nonprofits are already using AI. Only 14% have board-level oversight. That's not a technology problem—it's a leadership problem.</h2>
    <p>Nonprofits are making irreversible technology decisions—on AI adoption, cybersecurity, vendor risk, and data governance—without anyone in the room qualified to stress-test them. When boards can't lead on technology, organizations look like a risk to funders, miss corporate partnerships, and make expensive mistakes that never get fixed.</p>
    <p>Companies face the same gap from the other side. The leaders making AI decisions inside your organization are building judgment in real time—at real cost, and not fast enough.</p>
    <p>Structured board engagement changes that. Board service is where leadership gets tested for real. There's nothing else like it.</p>
  </div>
  <h2 style="text-align:center;font-size:24px;font-weight:500;margin:40px 0 28px">What we do</h2>
  <div class="three">
    <div>
      <div class="ill"><svg width="110" height="110" viewBox="0 0 110 110" aria-hidden="true"><rect x="40" y="10" width="14" height="70" fill="#2f4192" transform="skewX(-12)"/><rect x="70" y="20" width="14" height="60" fill="#2f4192" transform="skewX(-12)"/><circle cx="48" cy="60" r="18" fill="#c92240"/><path d="M20 70 l18 -14 l6 8 z" fill="#fff" stroke="#c92240" stroke-width="3"/></svg></div>
      <h3>Build Board Tech Fluency</h3>
      <p>Board.Dev trains nonprofit boards and executives on AI strategy, cybersecurity, and digital decision-making—so leaders can guide technology investments, not just approve them. Available as a standalone 90-minute session or as part of a multi-week cohort program. Works for 10 people or 1,000.</p>
    </div>
    <div>
      <div class="ill"><svg width="110" height="110" viewBox="0 0 110 110" aria-hidden="true"><rect x="10" y="70" width="34" height="30" fill="#2f4192"/><rect x="66" y="70" width="34" height="30" fill="#2f4192"/><path d="M48 10 l20 12 l-8 26 l-18 -6 z" fill="none" stroke="#c92240" stroke-width="3"/><circle cx="55" cy="68" r="22" fill="#c92240"/></svg></div>
      <h3>Develop Leaders Through Board Service</h3>
      <p>Through board placements, mentorship, and subject matter expert roles, Board.Dev connects business professionals—across marketing, finance, HR, operations, and technology, not just engineers—with nonprofits where real decisions get made. Real budgets, real risk, real accountability. The judgment leaders build here transfers directly back to their day jobs. This is the development experience internal programs can't replicate.</p>
    </div>
    <div>
      <div class="ill"><svg width="110" height="110" viewBox="0 0 110 110" aria-hidden="true"><rect x="50" y="30" width="36" height="46" fill="#2f4192" opacity=".4" transform="rotate(-10 68 53)"/><rect x="58" y="36" width="36" height="46" fill="#2f4192" opacity=".7" transform="rotate(-10 76 59)"/><circle cx="40" cy="42" r="24" fill="#c92240"/><path d="M30 70 l14 -10 l10 12 l-4 20 l-20 -4 z" fill="none" stroke="#c92240" stroke-width="3"/></svg></div>
      <h3>Partner with Companies</h3>
      <p>Board.Dev works with companies who want to develop their leaders and strengthen their nonprofit partners at the same time. Through structured board engagement—training, placements, cohorts, and mentorship—we deliver measurable impact with minimal lift on your team. Board.Dev manages delivery end to end.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="logo-wall">
    <div class="featured"><img src="assets/img/logos/okta.png" alt="Okta"></div>
    <div class="grid"><img src="assets/img/logos/atlassian.png" alt="Atlassian" loading="lazy"><img src="assets/img/logos/aws.png" alt="Amazon Web Services" loading="lazy"><img src="assets/img/logos/benevity.png" alt="Benevity" loading="lazy"><img src="assets/img/logos/cdw.png" alt="CDW" loading="lazy"><img src="assets/img/logos/chicago-scholars.png" alt="Chicago Scholars" loading="lazy"><img src="assets/img/logos/cics.png" alt="Chicago International Charter School" loading="lazy"><img src="assets/img/logos/compass-working-capital.png" alt="Compass Working Capital" loading="lazy"><img src="assets/img/logos/cuny.png" alt="CUNY" loading="lazy"><img src="assets/img/logos/colorstack.png" alt="ColorStack" loading="lazy"><img src="assets/img/logos/dell.png" alt="Dell Technologies" loading="lazy"><img src="assets/img/logos/develop-for-good.png" alt="Develop for Good" loading="lazy"><img src="assets/img/logos/empowr.png" alt="Empowr" loading="lazy"><img src="assets/img/logos/fast-forward.png" alt="Fast Forward" loading="lazy"><img src="assets/img/logos/finequity.png" alt="finEQUITY" loading="lazy"><img src="assets/img/logos/food-connect.png" alt="Food Connect" loading="lazy"><img src="assets/img/logos/generation.svg" alt="Generation" loading="lazy"><img src="assets/img/logos/genesys-works.png" alt="Genesys Works" loading="lazy"><img src="assets/img/logos/growing-home.png" alt="Growing Home" loading="lazy"><img src="assets/img/logos/hack-the-hood.png" alt="Hack the Hood" loading="lazy"><img src="assets/img/logos/hera-digital-health.png" alt="HERA Digital Health" loading="lazy"><img src="assets/img/logos/hidden-genius-project.png" alt="The Hidden Genius Project" loading="lazy"><img src="assets/img/logos/human-rights-first.png" alt="Human Rights First" loading="lazy"><img src="assets/img/logos/jvs.png" alt="JVS" loading="lazy"><img src="assets/img/logos/les-ecology-center.png" alt="LES Ecology Center" loading="lazy"><img src="assets/img/logos/linkedin.png" alt="LinkedIn" loading="lazy"><img src="assets/img/logos/pwc.png" alt="PwC" loading="lazy"><img src="assets/img/logos/marin-community-foundation.png" alt="Marin Community Foundation" loading="lazy"><img src="assets/img/logos/morgan-stanley.png" alt="Morgan Stanley" loading="lazy"><img src="assets/img/logos/netapp.png" alt="NetApp" loading="lazy"><img src="assets/img/logos/nethope.png" alt="NetHope" loading="lazy"><img src="assets/img/logos/nten.png" alt="NTEN" loading="lazy"><img src="assets/img/logos/possibility-project.png" alt="The Possibility Project" loading="lazy"><img src="assets/img/logos/rise.png" alt="RISE" loading="lazy"><img src="assets/img/logos/sadie-nash.png" alt="Sadie Nash Leadership Project" loading="lazy"><img src="assets/img/logos/schmidt-futures.png" alt="Schmidt Futures" loading="lazy"><img src="assets/img/logos/servicenow.png" alt="ServiceNow" loading="lazy"><img src="assets/img/logos/techsoup.png" alt="TechSoup" loading="lazy"><img src="assets/img/logos/tipping-point.png" alt="Tipping Point Community" loading="lazy"><img src="assets/img/logos/world-pulse.png" alt="World Pulse" loading="lazy"><img src="assets/img/logos/raise-for-good.png" alt="Raise for Good" loading="lazy"><img src="assets/img/logos/justworks.png" alt="Justworks" loading="lazy"><img src="assets/img/logos/global-business-coalition-for-education.png" alt="Global Business Coalition for Education" loading="lazy"><img src="assets/img/logos/youthbuild.png" alt="YouthBuild" loading="lazy"></div>
  </div>
  <p class="callout" style="margin-top:40px;font-size:1.15rem;color:var(--ink)">Through the <b>Nonprofit Tech Governance Congress</b>, Board.Dev convenes the leaders setting standards for AI decision-making in the social sector—and through our annual salon series, brings together nonprofit CEOs, funders, and corporate leaders to design the board nonprofits need now.</p>
  <p style="text-align:center;margin-top:20px"><a class="btn btn-navy" href="about-us.html">Learn more</a></p>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="band" style="border-radius:var(--radius);padding:36px 28px">
    <h2 style="text-align:center;font-size:24px;font-weight:500;margin-bottom:24px">See how board service builds leaders and impact</h2>
    <div class="videos">
      <a class="video" href="https://www.youtube.com/watch?v=L19EyN38Qh4" data-id="L19EyN38Qh4" target="_blank" rel="noopener"><div class="thumb"><img src="https://img.youtube.com/vi/L19EyN38Qh4/hqdefault.jpg" alt="" loading="lazy"></div><div class="cap">Arnab Bose<small>Asana, CPO</small></div></a>
      <a class="video" href="https://www.youtube.com/watch?v=na8TBGlQo4A" data-id="na8TBGlQo4A" target="_blank" rel="noopener"><div class="thumb"><img src="https://img.youtube.com/vi/na8TBGlQo4A/hqdefault.jpg" alt="" loading="lazy"></div><div class="cap">Erin Baudo Felter<small>Okta, VP Global Impact</small></div></a>
      <a class="video" href="https://www.youtube.com/watch?v=N85-_qqMywg" data-id="N85-_qqMywg" target="_blank" rel="noopener"><div class="thumb"><img src="https://img.youtube.com/vi/N85-_qqMywg/hqdefault.jpg" alt="" loading="lazy"></div><div class="cap">Susi Hajeski<small>CDW, Head of Cybersecurity</small></div></a>
    </div>
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <h2 style="text-align:center;font-size:24px;font-weight:500;margin-bottom:24px">Why Board.Dev?</h2>
  <div class="quote-row">
    <div class="quote-card">
      <p>Board members are essential to moving AI and tech forward. Their primary job in governance is to support the strategic direction. They aren't setting it, but they are making sure it's moving—and AI strategy is no different.</p>
      <cite>Shannon Farley, Fast Forward</cite>
    </div>
    <div class="quote-card">
      <p>I'm a physician and know nothing about the IT side of things. We need someone not to actually build the technology but to help us visualize how the infrastructure could help us move forward. It's a series of decisions with which we could use tech expertise as we grow.</p>
      <cite>Aral Surmeli, Founder, HERA Digital Health</cite>
    </div>
    <div class="quote-card">
      <p>It was just this beautiful gift that we received an email from Board.Dev. You don't have that fulltime, dedicated tech data person on staff—that high-level strategy is expensive. Even for us, with a $160 million budget, it's not really within the realm of possibilities. I gasped to think that there are tech professionals who feel like they would not be a value add to a nonprofit. This is such an enormous need.</p>
      <cite>Meaghan Jennings, ED, Chicago International Charter School</cite>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="stats">
    <div class="stat"><svg class="ico" viewBox="0 0 64 64" fill="currentColor" aria-hidden="true"><circle cx="20" cy="12" r="8"/><rect x="12" y="22" width="16" height="30" rx="4"/><rect x="34" y="6" width="4" height="52"/><path d="M38 8h20l-6 8 6 8H38z"/></svg><div><b>4,200+</b><small>Leaders in the community</small></div></div>
    <div class="stat"><svg class="ico" viewBox="0 0 64 64" fill="currentColor" aria-hidden="true"><circle cx="32" cy="16" r="9"/><circle cx="12" cy="22" r="7"/><circle cx="52" cy="22" r="7"/><path d="M4 50c0-10 6-16 14-16s8 2 14 2 6-2 14-2 14 6 14 16v6H4z"/></svg><div><b>30,000</b><small>Tech leaders on boards by 2030 goal</small></div></div>
  </div>
</div></section>
{NEWSLETTER}
""")

# ---------- WHAT WE DO ----------
pages["what-we-do.html"] = dict(title="What We Do — Board.Dev", desc="How Board.Dev builds board tech fluency, develops leaders through board service, and partners with companies and funders.", active=1, body=f"""
<section class="section" style="padding-top:24px"><div class="wrap">
  <div class="hero compact">
    <h1>Leadership is the leverage point.</h1>
    <p>Digital transformation doesn't start with tools. It starts with leadership.</p>
    <p>We strengthen nonprofits by building tech fluency at the board level and connecting them with professionals who can help navigate AI, cybersecurity, and digital strategy.</p>
  </div>
</div></section>

<section class="section band"><div class="wrap prose">
  <h2>Build Board Tech Fluency</h2>
  <p>Board.Dev trains nonprofit boards and executives on AI strategy, cybersecurity, and digital decision-making—so leaders can guide technology investments, not just approve them. Available as a standalone 90-minute session or as part of a multi-week cohort program. Works for 10 people or 1,000.</p>
  <h2>Develop Leaders Through Board Service</h2>
  <p><b>The best leadership development happens where the stakes are real.</b> We connect business professionals across marketing, finance, HR, operations, legal, and technology with nonprofits making consequential decisions about growth, technology, and strategy. Board and advisory board placements where your expertise matters.</p>
  <p>Your people build judgment through real governance experience. Nonprofits get expertise they need but can't afford to hire. Everyone wins.</p>
  <p>80% of participants report being better leaders. The skills transfer directly: strategic thinking under resource constraints, stakeholder alignment, risk assessment, decision-making when you can't control all the variables.</p>
  <p>Companies developing next-level leaders, nonprofits building board capacity</p>
  <p>We change that. Organizations where staff and board co-developed AI principles are 12× more likely to reach pilots or scaling. We build that board-staff partnership through focused training, peer learning, and practical frameworks that clarify who does what—creating field-wide capacity that makes every tech investment more effective.</p>
  <p>Nonprofit boards, funders strengthening portfolio organizations.</p>
</div></section>

<section class="section"><div class="wrap">
  <h2 style="text-align:center;font-size:26px;font-weight:500;margin-bottom:24px">Corporate Leader Perspectives</h2>
  <div class="videos two-up">
    <a class="video" href="https://www.youtube.com/watch?v=L19EyN38Qh4" data-id="L19EyN38Qh4" target="_blank" rel="noopener"><div class="thumb"><img src="https://img.youtube.com/vi/L19EyN38Qh4/hqdefault.jpg" alt="" loading="lazy"></div><div class="cap">Arnab Bose (Asana CPO) on how board service shaped his leadership</div></a>
    <a class="video" href="https://www.youtube.com/watch?v=na8TBGlQo4A" data-id="na8TBGlQo4A" target="_blank" rel="noopener"><div class="thumb"><img src="https://img.youtube.com/vi/na8TBGlQo4A/hqdefault.jpg" alt="" loading="lazy"></div><div class="cap">Erin Baudo Felter (Okta) on why board service is a unique lever for social impact</div></a>
  </div>
</div></section>

<section class="section band"><div class="wrap prose">
  <h2>Partner with Companies</h2>
  <p class="lead">Are your leaders building AI-era judgment fast enough?</p>
  <p>We help companies navigate transformation through board placements, AI leadership labs, and training cohorts that strengthen nonprofit relationships. Your marketing, finance, HR, and operations leaders—not just your technologists—get real governance experience where strategic decisions have community impact.</p>
  <p>L&amp;D leaders, CSR teams, companies with established nonprofit relationships</p>
</div></section>

<section class="section"><div class="wrap prose right">
  <h2>For Funders</h2>
  <p class="lead">Protect your tech investments by funding the leadership that makes them work.</p>
  <p>You fund technology. But technology investments only work if boards can lead through them. Only 24% of nonprofit boards have tech or data backgrounds represented. 90% of foundations provide no AI implementation support to grantees. We help funders protect their portfolios by building the leadership infrastructure that makes every grant more effective—through training, board development, and field-wide standards.</p>
  <p>Strategic philanthropists, program officers, foundations investing in nonprofit technology capacity</p>
</div></section>
""")

# ---------- RESOURCES ----------
res = [
 ("Building the Board We Need Now: SF Dispatch","What can my board do that AI can't? Thirty nonprofit CEOs, funders, and board chairs spent an afternoon in San Francisco on that question. The first dispatch from our 2026 field research, with Okta and AWS.","sf-dispatch","assets/pdfs/board-dev-sf-dispatch.pdf","Read the dispatch"),
 ("Building the Leadership Nonprofits Need to Make AI Work.","A new co-publication of Board.Dev and Dell Technologies based on a national nonprofit survey—a hard look at why the sector is stuck and what leadership teams can do about it.","dell-report","assets/pdfs/board-dev-dell-building-the-leadership-nonprofits-need-to-make-ai-work.pdf","Read the report"),
 ("Interview Guide: Tech Board Candidates","A practical, structured tool to help you lead more effective interviews with prospective tech board members. It covers four key areas: experience and skills, approach, motivation and fit, and expectations. Download the guide to strengthen your board recruitment process.","interview-guide","assets/pdfs/board-dev-interview-guide-tech-board-candidates.pdf","Download"),
 ("Tech Board Role Description Template","Need a board member with tech expertise? Use this editable template to quickly draft and post a compelling role description that attracts the right candidates.","role-description-template","https://docs.google.com/document/d/1CWvjTivdMP-jFOL0KP4ij-6rtfyzHsmG4s0OD3V4Yc0/edit","Open template"),
 ("Guide: Finding Board Members","Our free guide walks you through all the steps you'll need to find and recruit potential board members via LinkedIn, using your greatest resource: your current board members.","finding-board-members","assets/pdfs/board-dev-guide-finding-board-members-linkedin.pdf","Download"),
 ("Board Brief: AI Adoption + Policy","A 3-month action plan to help nonprofit boards lead on AI strategy, policy, and ethics. This brief offers practical guidance, key questions, and concrete steps to support human-centered, mission-aligned AI adoption without requiring boards to be tech experts. Use it to set values-based guardrails, boost tech fluency, and make confident decisions.","board-brief-ai","assets/pdfs/board-dev-board-brief-ai-adoption-policy.pdf","Download"),
 ("The Tech Governance Playbook","Our free Tech Governance Playbook provides everything you need to know about how nonprofits leverage tech executives to maximize their impact. Download now to learn how you can start making change right now.","tech-governance-playbook","assets/pdfs/board-dev-tech-governance-playbook.pdf","Download"),
 ("The Tech 28","A set of 28 essential questions to help nonprofit boards and CEOs start strategic conversations about technology, risk, and innovation. Use The Tech 28 to align your board, strengthen decision-making, and make tech a core part of your organization's mission and impact.","tech-28","assets/pdfs/board-dev-the-tech-28.pdf","Download"),
]
cards = "".join(f"""
    <article class="res">
      <div class="body"><h3>{t}</h3><p>{d}</p><a class="btn btn-ghost" href="{href}" target="_blank" rel="noopener">{cta}</a></div>
      <div class="ph"><img src="assets/img/resources/{img}.jpg" alt="" loading="lazy"></div>
    </article>""" for t,d,img,href,cta in res)
pages["resources.html"] = dict(title="Resources — Board.Dev", desc="Free tools to help nonprofit leaders, funders, and partners build tech fluency and strategic capacity.", active=2, body=f"""
<section class="section"><div class="wrap">
  <div class="page-title">
    <h1>Tools to Help Boards Lead Through Tech</h1>
    <p>Free tools to help nonprofit leaders, funders, and partners build tech fluency and strategic capacity.</p>
  </div>
  <div class="res-grid">{cards}
  </div>
</div></section>
{NEWSLETTER}
""")

# ---------- ABOUT ----------
members = [("Alvina Antar","Chief Digital Officer, F5"),("Amy Sample Ward","CEO, NTEN"),("Anil Dash","Principal & Cofounder, antitech"),
("Chantal Forster","Independent Advisor, Warren West Advisor"),("Darian Rodriguez Heyman","Founder, Helping People Help / Former Executive Director, Craigslist Foundation"),("Edima Elinewinga","VP, CTO, Association of Corporate Counsel"),
("Erik Arnold","VP, Sector Initiatives, DARO"),("Erran Berger","CTO, Engineering, LinkedIn"),("Georgia Bullen","Executive Director, Superbloom"),
("Jim Fruchterman","Founder/CEO, Tech Matters"),("John Mohr","CIO, MacArthur Foundation"),("Idalin Bobe","Founder, Tech Intersections"),
("Kevin Barenblat","Co-founder & President, Fast Forward"),("Kristen Swanson","Member of Technical Staff, Anthropic"),("Mike Belinsky","Civil Society & Philanthropy, OpenAI Foundation"),
("Nate Wong","Partner, Bridgespan Group"),("Oliver Hurst-Hiller","Board of Directors, Fast Forward"),("Sajit Joseph","CTO, Risepoint"),
("Satwik Seshasai","Executive in Residence, Inovia Capital"),("Tara Huffman","Chief Program and Strategy Officer, BoardSource"),("Alex Diaz","Head of AI for Social Good, Google"),("Nabiha Syed","ED, Mozilla Foundation")]
def slugify(n): return re.sub(r"[^a-z0-9]+","-",n.lower()).strip("-")
mem = "".join(f'<div class="member"><div class="avatar sm"><img src="assets/img/team/{slugify(n)}.jpg" alt="{n}" loading="lazy"></div><b>{n}</b><small>{r}</small></div>' for n,r in members)
pages["about-us.html"] = dict(title="About — Board.Dev", desc="The founding team and the Nonprofit Tech Governance Congress behind Board.Dev.", active=3, body=f"""
<section class="section"><div class="wrap">
  <div class="about-head">
    <h1>The Leaders Behind the Movement</h1>
    <p>We helped build the pro bono movement. Now we're building the boards nonprofits need for the AI era.</p>
  </div>
</div></section>
<section class="founders"><div class="wrap">
  <h2>Founding Team</h2>
  <div class="founder-grid">
    <div class="founder"><div class="avatar"><img src="assets/img/team/alethea-hannemann.jpg" alt="Alethea Hannemann"></div><h3>Alethea Hannemann</h3><div class="role">Co-Founder/CEO</div><p>Built cross-sector collaborations at Taproot, Okta, Google, and Splunk. Former COO of a $25M nonprofit. Co-author of Powered by Pro Bono. Bridges tech, philanthropy, and mission leadership.</p></div>
    <div class="founder"><div class="avatar"><img src="assets/img/team/aaron-hurst.jpg" alt="Aaron Hurst"></div><h3>Aaron Hurst</h3><div class="role">Co-Founder/Advisor</div><p>Serial social entrepreneur; founded Taproot Foundation ($15B pro bono market) and Imperative (venture-backed B Corp). Advisor to LinkedIn and longtime board member. Author of Powered by Pro Bono and The Purpose Economy.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="congress">
    <h2>Nonprofit Tech Governance Congress</h2>
    <p>The Nonprofit Tech Governance Congress brings together experts from tech, philanthropy, and civil society to define shared standards for responsible tech adoption at the board level. This work addresses urgent risks like bias, surveillance, and exclusion, and creates the leadership infrastructure every product, grant, and innovation needs to succeed. The Congress aligns funders, companies, and nonprofits so AI and digital transformation deliver real impact.</p>
  </div>
  <div class="members">
    <h2>Our Members</h2>
    <div class="member-grid">{mem}</div>
  </div>
  <div class="featured-in">
    <p>Featured in</p>
    <div class="press"><img src="assets/img/press/ssir.png" alt="Stanford Social Innovation Review" loading="lazy"><img src="assets/img/press/chronicle-of-philanthropy.png" alt="The Chronicle of Philanthropy" loading="lazy"><img src="assets/img/press/tech-policy-press.png" alt="Tech Policy Press" loading="lazy"></div>
  </div>
  <div class="gallery" aria-label="Event photo gallery"><img src="assets/img/events/event-01.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-02.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-03.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-04.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-05.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-06.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-07.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-08.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-09.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-10.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-11.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-12.jpg" alt="Board.Dev event photo" loading="lazy"><img src="assets/img/events/event-13.jpg" alt="Board.Dev event photo" loading="lazy"></div>
  <p class="tagline">Tech-ready boards.<br>Mission-ready nonprofits.</p>
  <svg class="tagline-art" viewBox="0 0 1200 170" aria-hidden="true">
    <polyline points="40,40 400,120 760,40 1120,135" fill="none" stroke="#b7c3ea" stroke-width="3" stroke-dasharray="7 9" stroke-linecap="round"/>
    <polygon points="40,10 70,30 60,62 20,62 10,30" fill="#1a2a8f"/>
    <circle cx="400" cy="120" r="32" fill="#c92240"/>
    <rect x="732" y="12" width="56" height="56" fill="#a9c4f5"/>
    <polygon points="1100,98 1150,150 1080,160" fill="#3a4aa0"/>
  </svg>
</div></section>
{NEWSLETTER}
""")

# ---------- GET IN TOUCH ----------
pages["get-in-touch.html"] = dict(title="Get in touch — Board.Dev", desc="Contact Board.Dev.", active=-1, body="""
<section class="section band" style="min-height:70vh"><div class="wrap">
  <h1 style="text-align:center;font-size:27px;font-weight:500;margin-bottom:28px">Get in touch</h1>
  <div class="form-card hs-form" id="contact-form"></div>
  <script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
  <script>hbspt.forms.create({portalId:"45089564",formId:"e7e9d42a-2db1-42a0-ac6c-a5b3f6a86a66",region:"na1",target:"#contact-form"});</script>
</div></section>
""")


pages["newsletter.html"] = dict(title="Newsletter — Board.Dev", desc="Short monthly notes on AI governance, tech leadership, and the work of the Nonprofit Tech Governance Congress.", active=-1, body="""
<section class="section band" style="min-height:70vh"><div class="wrap">
  <h1 style="text-align:center;font-size:32px;font-weight:500;margin-bottom:28px">Join our newsletter</h1>
  <div class="form-card newsletter-card">
    <iframe id="hubspotForm" title="Newsletter sign-up" src="https://share.hsforms.com/16MlNR8ilRoqOEsInxyf06gqufbw" width="100%" height="640" frameborder="0" scrolling="no" style="display:block;border:0"></iframe>
  </div>
</div></section>
""")

pages["privacy-policy.html"] = dict(title="Privacy Policy — Board.Dev", desc="Board.Dev privacy policy.", active=-1, body="""
<section class="section"><div class="wrap prose" style="max-width:720px">
  <h1 style="font-size:27px;font-weight:500">Board.Dev Privacy Policy</h1>
  <p class="eyebrow" style="margin-top:8px">Last updated: August 20, 2026</p>
  <p>Board.Dev connects tech-fluent leaders with nonprofit boards and delivers AI leadership programs for nonprofits and corporate partners. This policy explains what information we collect, how we use it, and who we share it with.</p>
  <h2>1. Information we collect</h2>
  <p>We collect information when you fill out a form on our site, apply to be considered for a board placement, register for an event or program, subscribe to our emails, respond to a survey, or contact us directly.</p>
  <p>Depending on how you interact with us, this may include your name, email address, phone number, employer, job title, professional background and experience, board service history, areas of interest, geographic location, and any other information you choose to provide.</p>
  <p>We also collect technical information automatically when you visit our website, including browser type, device, pages visited, and general usage patterns.</p>
  <h2>2. How we use your information</h2>
  <p>We use your information to evaluate and match candidates with nonprofit board opportunities, deliver programs and events you have registered for, respond to your questions, send updates and invitations, and improve our services and content.</p>
  <h2>3. Board placement candidates</h2>
  <p>If you apply or are nominated for a board placement, we assess your background and experience to identify nonprofit organizations where you may be a strong fit. As part of that process, we share your professional profile and relevant application materials with nonprofit organizations we believe are a match, so they can decide whether to interview you.</p>
  <p>We use software tools, including AI-assisted systems, to help organize and evaluate candidate information. All matching recommendations are reviewed by a person before we share your information with any organization.</p>
  <p>If your participation is sponsored by your employer, we share your enrollment status, participation, and placement outcome with that employer. We do not share the substance of your individual application materials, interview feedback, or personal information beyond what is necessary to report on the program. In some programs your employer participates in the matching process and also sees the information you provide in your application.</p>
  <h2>4. Nonprofit organizations</h2>
  <p>If your organization applies for a board placement or participates in one of our programs, we collect information about your organization, its board, its technology and AI practices, and the people we work with. We share relevant portions with candidates so they can evaluate the opportunity, and with the corporate partner sponsoring the program in aggregate or summary form.</p>
  <h2>5. Research and publications</h2>
  <p>We conduct research on nonprofit boards and AI adoption, sometimes with partners. If you participate in a survey or interview, we tell you at the time how the information will be used. We report research findings in aggregate and do not identify individuals or organizations in publications without permission.</p>
  <h2>6. Sharing your information</h2>
  <p>We do not sell your personal information.</p>
  <p>We share information with nonprofit organizations and corporate partners as described above, and with service providers who help us operate, including email, analytics, and customer relationship management platforms, including Google Analytics and HubSpot, and AI platforms including Anthropic's Claude API. These providers may only use the information to provide services to us.</p>
  <p>We may disclose information if required by law, or to protect our rights or the safety of others.</p>
  <h2>7. How long we keep information</h2>
  <p>We keep candidate information for as long as you may be interested in board service, so we can contact you about future opportunities. We keep program and event records as long as we need them for our operations and any reporting obligations. You can ask us to delete your information at any time.</p>
  <h2>8. Cookies</h2>
  <p>We use cookies and similar technologies to understand how people use our site and to improve it. You can control cookies through your browser settings.</p>
  <h2>9. Data security</h2>
  <p>We take reasonable measures to protect your information. No system is completely secure, and we cannot guarantee absolute security.</p>
  <h2>10. Your choices and rights</h2>
  <p>You can unsubscribe from our emails at any time using the link in any message. You can ask us to access, correct, or delete the information we hold about you, ask us to stop sharing your profile with organizations, or withdraw your consent to future communications.</p>
  <p>Depending on where you live, you may have additional rights, including the right to know what personal information we collect and how we use it, the right to request deletion, the right to correct inaccurate information, and the right not to be discriminated against for exercising these rights. If you are in the European Economic Area or the United Kingdom, you also have the right to object to or restrict processing, the right to data portability, and the right to lodge a complaint with your local data protection authority. Where we process your information, we do so because you have consented, because it is necessary to provide a service you requested, or because we have a legitimate interest in operating our programs.</p>
  <p>To exercise any of these rights, email us at <a href="mailto:info@board.dev">info@board.dev</a>.</p>
  <h2>11. International transfers</h2>
  <p>We operate in the United States, and information we collect is stored and processed there. If you are outside the United States, you understand your information will be transferred to and processed in the United States.</p>
  <h2>12. Children</h2>
  <p>Our services are for adults. We do not knowingly collect information from anyone under 16. If you believe a child has provided us information, contact us and we will delete it.</p>
  <h2>13. Changes</h2>
  <p>We may update this policy. Changes will be posted here with a new date.</p>
  <h2>14. Contact</h2>
  <p>Board.Dev<br><a href="mailto:info@board.dev">info@board.dev</a><br><a href="https://www.board.dev">https://www.board.dev</a></p>

</div></section>
""")


# ---------- SALON RECAP: SAN FRANCISCO ----------
# Self-hosted clips (no YouTube, no third-party script). Drop files in assets/video/ and list them here.
SF_VIDEOS = [
 ("sf-01","What can a board do that AI can't?","Buddy Shah (Clinton Health Access Initiative) with Charlotte Wylie (Okta)"),
 ("sf-02","Building a tech-fluent board","Hilary Noon, AWS, with Michael Lissner, Free Law Project"),
 ("sf-03","Ways to support nonprofits","Victor Cordon, Okta"),
]
sf_vids = "".join(f"""
      <figure class="clip">
        <video controls preload="metadata" playsinline poster="assets/video/{f}.jpg"><source src="assets/video/{f}.mp4" type="video/mp4">Your browser can't play this video. <a href="assets/video/{f}.mp4">Download it</a> instead.</video>
        <figcaption><b>{t}</b><small>{c}</small></figcaption>
      </figure>""" for f,t,c in SF_VIDEOS)
pages["salon-sf.html"] = dict(title="Salon Recap: San Francisco — Board.Dev", desc="What can a board do that AI can't? Thirty nonprofit CEOs, funders, and board chairs spent an afternoon in San Francisco on that question. Highlights from the first stop of the 2026 Salon Series with Okta and AWS.", active=-1, body=f"""
<section class="section" style="padding-top:24px"><div class="wrap">
  <div class="hero compact">
    <p class="eyebrow" style="color:#dfe3f3">2026 Salon Series · San Francisco · June 8</p>
    <h1>What can a board do that AI can't?</h1>
    <p>Thirty nonprofit CEOs, funders, and board chairs spent an afternoon on that question. The first stop of Building the Board Nonprofits Need Now, presented by Board.Dev and Okta.</p>
  </div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <h2 style="text-align:center;font-weight:500;margin-bottom:24px">Watch the highlights</h2>
  <div class="clips">{sf_vids}
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <div class="two" style="text-align:left">
    <div>
      <p class="eyebrow">On stage</p>
      <h3>Three conversations, one question</h3>
      <p>Buddy Shah, CEO of the Clinton Health Access Initiative and chair of Anthropic's Long-Term Benefit Trust, opened the series with Charlotte Wylie of Okta. Hilary Noon of AWS and Michael Lissner of Free Law Project took on what a tech-fluent board looks like in practice. Victor Cordon of Okta closed with how companies can show up for nonprofits.</p>
    </div>
    <div>
      <p class="eyebrow">What we built</p>
      <h3>Two questions and ten mandates</h3>
      <p>San Francisco surfaced the two questions the whole series now runs on: what can a board do that AI can't, and how do we finally build the board we've needed for decades? The room drafted ten mandates to answer them. New York pressure-tested those mandates. Chicago extended them.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="stats">
    <div class="stat"><div><b>3</b><small>Cities in the 2026 series</small></div></div>
    <div class="stat"><div><b>77</b><small>Leaders in the working sessions</small></div></div>
    <div class="stat"><div><b>190</b><small>Organizations registered</small></div></div>
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <div class="two">
    <div>
      <h3>Read the June dispatch</h3>
      <p>Everything the San Francisco room built, in one brief.</p>
      <a class="btn btn-navy" href="assets/pdfs/board-dev-sf-dispatch.pdf" target="_blank" rel="noopener">Read the dispatch</a>
    </div>
    <div>
      <h3>The full blueprint lands in January 2027</h3>
      <p>Building the Board Nonprofits Need Now, in collaboration with The Bridgespan Group. Subscribe to get it first.</p>
      <a class="btn btn-navy" href="newsletter.html">Subscribe</a>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="featured-in">
    <p>With thanks to our San Francisco partners</p>
    <div class="press"><img src="assets/img/logos/okta.png" alt="Okta, presenting partner and working session host" loading="lazy"><img src="assets/img/logos/aws.png" alt="Amazon Web Services, reception host" loading="lazy"></div>
  </div>
</div></section>
""")

# ---------- OUTPUT ----------
# URLs must match the old WordPress permalinks exactly (/about-us/, /what-we-do/ ...)
# so every link in past emails, Google, LinkedIn and partner sites keeps working.
# Each page is written to <slug>/index.html and all links are made root-relative.
SITE = "https://board.dev"
ROUTES = {
    "index.html":          "/",
    "what-we-do.html":     "/what-we-do/",
    "resources.html":      "/resources/",
    "about-us.html":       "/about-us/",
    "get-in-touch.html":   "/get-in-touch/",
    "newsletter.html":     "/newsletter-sign-up/",
    "privacy-policy.html": "/privacy-policy/",
    "salon-sf.html":       "/salon-recap/san-francisco/",
}
# Old WordPress URLs that no longer have a page of their own -> where they go now.
REDIRECTS = {
    "/join-form/":  "/get-in-touch/",
    "/newsletter/": "/newsletter-sign-up/",
    "/june-blueprint/": "/assets/pdfs/board-dev-sf-dispatch.pdf",
}

def rootify(html):
    """Rewrite page-relative links to root-relative so pages work from /slug/ folders."""
    for name, route in ROUTES.items():
        html = html.replace(f'href="{name}"', f'href="{route}"')
    html = re.sub(r'(href|src|poster)="(assets/)', r'\1="/\2', html)
    html = html.replace('href="style.css?', 'href="/style.css?')
    return html

def out_path(route):
    return root/"index.html" if route == "/" else root/route.strip("/")/"index.html"

for name, p in pages.items():
    route = ROUTES[name]
    act = {i:(' class="active"' if p["active"]==i else "") for i in (1,2,3)}
    nav = NAV.format(a1=act[1],a2=act[2],a3=act[3])
    head = HEAD.format(title=p["title"],desc=p["desc"],cssv=CSSV).replace(
        "</head>", f'<link rel="canonical" href="{SITE}{route}">\n</head>')
    html = rootify(head + nav + p["body"] + FOOT)
    dest = out_path(route)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)
    if route != "/":
        (root/name).unlink(missing_ok=True)   # drop the old flat .html file

REDIRECT_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{site}{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}")</script>
</head><body><p>This page has moved to <a href="{to}">{site}{to}</a>.</p></body></html>
"""
for frm, to in REDIRECTS.items():
    dest = out_path(frm)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(REDIRECT_HTML.format(site=SITE, to=to))

# 404 page (GitHub Pages serves /404.html for any missing URL)
nav404 = NAV.format(a1="",a2="",a3="")
html404 = HEAD.format(title="Page not found — Board.Dev", desc="Page not found.", cssv=CSSV) + nav404 + """
<section class="section"><div class="wrap">
  <h1>Page not found</h1>
  <p>That page doesn't exist or has moved. Try the <a href="/">homepage</a>, <a href="/resources/">Resources</a>, or <a href="/get-in-touch/">get in touch</a>.</p>
</div></section>
""" + FOOT
(root/"404.html").write_text(rootify(html404))

# Custom domain for GitHub Pages
(root/"CNAME").write_text("board.dev\n")

(root/"README.md").write_text("# Board.Dev — static site\n\nPlain HTML/CSS, no build step. `build.py` is the source of truth for page content: edit it and run `python3 build.py` to regenerate the site.\n\n- Pages are written to `<slug>/index.html` so URLs match the old WordPress permalinks (`/about-us/`, `/what-we-do/` ...). The slug map is `ROUTES` in `build.py`; old URLs that moved are in `REDIRECTS`.\n- `assets/img/` — processed images (logo, team headshots, partner logos, resource cards)\n- `assets/pdfs/` — downloadable resources\n- `_source/` — original uploaded assets (not committed)\n- `404.html` — served by GitHub Pages for unknown URLs\n- `CNAME` — custom domain (`board.dev`); do not delete\n\nForms are HubSpot embeds (contact + newsletter). Video thumbnails load from YouTube.\n\nDeploy: GitHub Pages from `main` (root). GoDaddy DNS: four A records for `@` -> 185.199.108.153 / .109.153 / .110.153 / .111.153, CNAME `www` -> board-dev-org.github.io.\n")
print("built", [ROUTES[n] for n in pages], "+ redirects", list(REDIRECTS), "+ 404.html, CNAME")
