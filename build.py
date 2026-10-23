import pathlib, re
root = pathlib.Path(__file__).parent

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""

NAV = """<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html">BOARD.<span>DEV</span></a>
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
    <a class="btn btn-light" href="get-in-touch.html">Subscribe</a>
  </div>
</div></section>
"""

FOOT = """</main>
<footer>
  <div class="wrap">
    <div>
      <a class="logo" href="index.html">BOARD.<span>DEV</span></a>
      <p>Copyright © 2025 Board.Dev – All Rights Reserved.</p>
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
      <a class="btn btn-navy" href="resources.html">Read the report</a>
    </div>
    <div>
      <h3>What can my board do that AI can't?</h3>
      <p>Thirty nonprofit CEOs, funders, and board chairs spent an afternoon in San Francisco on that question.<br>The first dispatch from our 2026 field research, with Okta and AWS.</p>
      <a class="btn btn-navy" href="resources.html">Read the dispatch</a>
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
  <h2 style="text-align:center;font-size:1.5rem;font-weight:500;margin:40px 0 28px">What we do</h2>
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
  <div class="logos">
    <span class="featured">okta</span>
    <span>COMPASS WORKING CAPITAL</span><span>benevity</span><span>CDW</span><span>CHICAGO SCHOLARS</span><span>CICS</span><span>CUNY</span><span>ColorStack</span><span>DELL</span><span>develop for good</span><span>EMPOWR</span><span>fastforward</span><span>finEQUITY</span><span>Food Connect</span><span>Generation</span><span>GENESYS WORKS</span><span>GROWING HOME</span><span>hack the hood</span><span>HERA Digital Health</span><span>Hidden Genius Project</span><span>Human Rights First</span><span>JVS</span><span>LES Ecology Center</span><span>LinkedIn</span><span>pwc</span><span>Marin Community Foundation</span><span>Morgan Stanley</span><span>NetApp</span><span>NETHOPE</span><span>nten</span><span>The Possibility Project</span><span>RISE</span><span>Sadie Nash Leadership Project</span><span>Schmidt Futures</span><span>servicenow</span><span>techsoup</span><span>Tipping Point Community</span><span>WORLD PULSE</span><span>Raise for Good</span><span>Justworks</span><span>Global Business Coalition for Education</span><span>YouthBuild</span>
  </div>
  <p class="callout" style="margin-top:40px;font-size:1.15rem;color:var(--ink)">Through the <b>Nonprofit Tech Governance Congress</b>, Board.Dev convenes the leaders setting standards for AI decision-making in the social sector—and through our annual salon series, brings together nonprofit CEOs, funders, and corporate leaders to design the board nonprofits need now.</p>
  <p style="text-align:center;margin-top:20px"><a class="btn btn-navy" href="about-us.html">Learn more</a></p>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="band" style="border-radius:var(--radius);padding:36px 28px">
    <h2 style="text-align:center;font-size:1.5rem;font-weight:500;margin-bottom:24px">See how board service builds leaders and impact</h2>
    <div class="videos">
      <a class="video" href="https://www.youtube.com/@boarddev" target="_blank" rel="noopener"><div class="thumb"></div><div class="cap">Arnab Bose<small>Asana, CPO</small></div></a>
      <a class="video" href="https://www.youtube.com/@boarddev" target="_blank" rel="noopener"><div class="thumb"></div><div class="cap">Erin Baudo Felter<small>Okta, VP Global Impact</small></div></a>
      <a class="video" href="https://www.youtube.com/@boarddev" target="_blank" rel="noopener"><div class="thumb"></div><div class="cap">Susi Hajeski<small>CDW, Head of Cybersecurity</small></div></a>
    </div>
  </div>
</div></section>

<section class="section band"><div class="wrap">
  <h2 style="text-align:center;font-size:1.5rem;font-weight:500;margin-bottom:24px">Why Board.Dev?</h2>
  <div class="quote-card">
    <p>It was just this beautiful gift that we received an email from Board.Dev. You don't have that fulltime, dedicated tech data person on staff—that high-level strategy is expensive. Even for us, with a $160 million budget, it's not really within the realm of possibilities. I gasped to think that there are tech professionals who feel like they would not be a value add to a nonprofit. This is such an enormous need.</p>
    <cite>Meaghan Jennings, ED, Chicago International Charter School</cite>
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
    {DOTS}
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
  <h2 style="text-align:center;font-size:1.6rem;font-weight:500;margin-bottom:24px">Corporate Leader Perspectives</h2>
  <div class="videos two-up">
    <a class="video" href="https://www.youtube.com/@boarddev" target="_blank" rel="noopener"><div class="thumb"></div><div class="cap">Arnab Bose (Asana CPO) on how board service shaped his leadership</div></a>
    <a class="video" href="https://www.youtube.com/@boarddev" target="_blank" rel="noopener"><div class="thumb"></div><div class="cap">Erin Baudo Felter (Okta) on why board service is a unique lever for social impact</div></a>
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
 ("Building the Board We Need Now: SF Dispatch","A new co-publication of Board.Dev and Dell Technologies based on a national nonprofit survey—a hard look at why the sector is stuck and what leadership teams can do about it.","Photo: salon roundtable"),
 ("Building the Leadership Nonprofits Need to Make AI Work.","A new co-publication of Board.Dev and Dell Technologies based on a national nonprofit survey—a hard look at why the sector is stuck and what leadership teams can do about it.","Photo: panel discussion"),
 ("Interview Guide: Tech Board Candidates","A practical, structured tool to help you lead more effective interviews with prospective tech board members. It covers four key areas: experience and skills, approach, motivation and fit, and expectations. Download the guide to strengthen your board recruitment process.","Photo: interview"),
 ("Tech Board Role Description Template","Need a board member with tech expertise? Use this editable template to quickly draft and post a compelling role description that attracts the right candidates.","Photo: laptop"),
 ("Guide: Finding Board Members","Our free guide walks you through all the steps you'll need to find and recruit potential board members via LinkedIn, using your greatest resource: your current board members.","Photo: LinkedIn"),
 ("Board Brief: AI Adoption + Policy","A 3-month action plan to help nonprofit boards lead on AI strategy, policy, and ethics. This brief offers practical guidance, key questions, and concrete steps to support human-centered, mission-aligned AI adoption without requiring boards to be tech experts. Use it to set values-based guardrails, boost tech fluency, and make confident decisions.","Photo: AI chip"),
 ("The Tech Governance Playbook","Our free Tech Governance Playbook provides everything you need to know about how nonprofits leverage tech executives to maximize their impact. Download now to learn how you can start making change right now.","Photo: boardroom"),
 ("The Tech 28","A set of 28 essential questions to help nonprofit boards and CEOs start strategic conversations about technology, risk, and innovation. Use The Tech 28 to align your board, strengthen decision-making, and make tech a core part of your organization's mission and impact.","Photo: planning"),
]
cards = "".join(f"""
    <article class="res">
      <div class="body"><h3>{t}</h3><p>{d}</p><a class="btn btn-ghost" href="get-in-touch.html">Download</a></div>
      <div class="ph">{ph}</div>
    </article>""" for t,d,ph in res)
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
def initials(n): return "".join(p[0] for p in n.split()[:2])
mem = "".join(f'<div class="member"><div class="avatar sm">{initials(n)}</div><b>{n}</b><small>{r}</small></div>' for n,r in members)
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
    <div class="founder"><div class="avatar">AH</div><h3>Alethea Hannemann</h3><div class="role">Co-Founder/CEO</div><p>Built cross-sector collaborations at Taproot, Okta, Google, and Splunk. Former COO of a $25M nonprofit. Co-author of Powered by Pro Bono. Bridges tech, philanthropy, and mission leadership.</p></div>
    <div class="founder"><div class="avatar">AH</div><h3>Aaron Hurst</h3><div class="role">Co-Founder/Advisor</div><p>Serial social entrepreneur; founded Taproot Foundation ($15B pro bono market) and Imperative (venture-backed B Corp). Advisor to LinkedIn and longtime board member. Author of Powered by Pro Bono and The Purpose Economy.</p></div>
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
    <div class="logos"><span>Stanford Social Innovation Review</span><span>The Chronicle of Philanthropy</span><span>Tech Policy Press</span></div>
  </div>
  <div class="gallery" aria-label="Event photo gallery">{"".join("<div></div>" for _ in range(12))}</div>
  <p class="tagline">Tech-ready boards.<br>Mission-ready nonprofits.</p>
</div></section>
{NEWSLETTER}
""")

# ---------- GET IN TOUCH ----------
pages["get-in-touch.html"] = dict(title="Get in touch — Board.Dev", desc="Contact Board.Dev.", active=-1, body="""
<section class="section band" style="min-height:70vh"><div class="wrap">
  <h1 style="text-align:center;font-size:1.7rem;font-weight:500;margin-bottom:28px">Get in touch</h1>
  <form class="form-card" id="contact" onsubmit="event.preventDefault();document.getElementById('thanks').hidden=false;this.reset()">
    <div class="row">
      <div><label for="fn">First Name<i>*</i></label><input id="fn" name="firstname" required></div>
      <div><label for="ln">Last Name<i>*</i></label><input id="ln" name="lastname" required></div>
    </div>
    <label for="em">Email<i>*</i></label><input id="em" name="email" type="email" required>
    <label for="org">Organization</label><input id="org" name="company">
    <label for="loc">Location<i>*</i></label>
    <select id="loc" name="location" required><option value="">Please Select</option><option>United States</option><option>Canada</option><option>Other</option></select>
    <label for="role">Professional role or function<i>*</i></label>
    <select id="role" name="role" required><option value="">Please Select</option><option>Nonprofit executive</option><option>Board member</option><option>Funder</option><option>Corporate leader</option><option>Other</option></select>
    <label for="int">I am interested in:<i>*</i></label>
    <select id="int" name="interest" required><option value="">Please Select</option><option>Board tech fluency training</option><option>Board service for my team</option><option>Partnering as a company</option><option>Funding this work</option><option>Resources and newsletter</option></select>
    <p class="legal">Board.Dev is committed to protecting and respecting your privacy. From time to time, we would like to contact you about new events, resources and other content that may be of interest to you. You can unsubscribe from these communications at any time. If you consent to us contacting you for this purpose, please check the box below:</p>
    <label class="consent"><input type="checkbox" id="consent" name="consent"> I agree to receive marketing communications from Board.Dev.</label>
    <p class="legal">By clicking submit below, you consent to allow Board.Dev to store and process the personal information submitted above to provide you the content requested.</p>
    <button class="submit" type="submit">Submit</button>
    <p id="thanks" hidden style="text-align:center;color:var(--navy);margin-top:14px;font-weight:600">Thanks — we'll be in touch.</p>
  </form>
  <p class="form-note">V1 note: this form will be replaced by the live HubSpot embed.</p>
</div></section>
""")

pages["privacy-policy.html"] = dict(title="Privacy Policy — Board.Dev", desc="Board.Dev privacy policy.", active=-1, body="""
<section class="section"><div class="wrap prose" style="max-width:720px">
  <h1 style="font-size:1.7rem;font-weight:500">Privacy Policy</h1>
  <p>Placeholder for the existing Board.Dev privacy policy text. Paste the current policy here before launch.</p>
</div></section>
""")

for name, p in pages.items():
    act = {i:(' class="active"' if p["active"]==i else "") for i in (1,2,3)}
    nav = NAV.format(a1=act[1],a2=act[2],a3=act[3])
    html = HEAD.format(title=p["title"],desc=p["desc"]) + nav + p["body"] + FOOT
    (root/name).write_text(html)

# artifact copy of index: no doctype/html/head/body wrappers
idx = (root/"index.html").read_text()
m = re.search(r"<head>(.*?)</head>\s*<body>(.*)</body>", idx, re.S)
head_inner = re.sub(r'<meta (charset|name="viewport")[^>]*>\n?', "", m.group(1))
head_inner = re.sub(r'<link[^>]*preconnect[^>]*>\n?', "", head_inner)
art = '<meta name="claude:viewport-fit-sides" content="cover">\n' + head_inner.strip() + "\n" + m.group(2)
pathlib.Path("/home/claude/boarddev-artifact").mkdir(exist_ok=True)
pathlib.Path("/home/claude/boarddev-artifact/index.html").write_text(art)
(root/"CNAME").write_text("board.dev\n")
(root/"README.md").write_text("# Board.Dev — static site\n\nPlain HTML/CSS, no build step. Edit the `.html` files directly, or edit `build.py` (the page source of truth) and run `python3 build.py` to regenerate.\n\nDeploy: GitHub Pages from `main`, custom domain `board.dev` (see `CNAME`).\n")
print("built", list(pages))
