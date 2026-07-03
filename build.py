# -*- coding: utf-8 -*-
# Generates the NorthStar multi-page static site.
import io

def img(i, w=1000):
    return "https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=%s" % (i, i, w)

TEACHER_CHILD = img(4173338, 1200)   # teacher helping child (hero/warm)
TEACHER_ASSIST = img(35290755)       # 1:1 teacher assisting child (SEIT)
BLOCKS = img(16145654)               # toddler developmental play
FAMILY = img(5336930)                # family with specialist
OUTDOORS = img(14545192, 1200)       # children outdoors

V_HOME = "https://videos.pexels.com/video-files/6952302/6952302-sd_960_540_30fps.mp4"
V_PLAY = "https://videos.pexels.com/video-files/8160138/8160138-sd_960_540_25fps.mp4"
V_SEIT = "https://videos.pexels.com/video-files/8925026/8925026-sd_960_540_25fps.mp4"

MARK = ('<svg class="mark" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<circle cx="22" cy="22" r="21" fill="#0A1930"/>'
        '<path d="M22 9l2.6 7.4L32 19l-7.4 2.6L22 29l-2.6-7.4L12 19l7.4-2.6L22 9z" fill="#C9A24B"/>'
        '<path d="M14 32c3-3.5 12-3.5 16 0" stroke="#EAF2FB" stroke-width="1.6" stroke-linecap="round"/></svg>')
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6L9 17l-5-5"/></svg>'

NAV = [("index.html","Home"),("about.html","About"),("services.html","Services"),
       ("programs.html","Programs"),("faq.html","FAQ"),("contact.html","Contact")]

def header(active):
    links = ""
    for href, label in NAV:
        if label == "Services":
            cls = " active" if active in ("services.html","seit.html","child-development.html","family-navigation.html") else ""
            links += ('<span class="navitem"><a href="services.html" class="%s">Services ▾</a>'
                      '<span class="drop">'
                      '<a href="seit.html"><b>SEIT Services</b><span>One-on-one specialized instruction</span></a>'
                      '<a href="child-development.html"><b>Child Development Support</b><span>Milestones, evaluations, referrals</span></a>'
                      '<a href="family-navigation.html"><b>Family Navigation</b><span>Understanding the CPSE process</span></a>'
                      '<a href="services.html"><b>All Services</b><span>See everything we offer</span></a>'
                      '</span></span>') % cls.strip()
        else:
            cls = " active" if active == href else ""
            links += '<a href="%s" class="%s">%s</a>' % (href, cls.strip(), label)
    return ('<header class="site" id="top-header"><div class="wrap bar">'
            '<a href="index.html" class="brand" aria-label="NorthStar Child Development Services home">%s'
            '<span class="txt"><b>NorthStar</b><small>CHILD DEVELOPMENT SERVICES</small></span></a>'
            '<nav class="main" aria-label="Primary">%s</nav>'
            '<div class="hcta"><a href="enroll.html" class="btn btn-gold">Begin Enrollment <span class="a">→</span></a>'
            '<button class="burger" id="burger" aria-label="Open menu"><span></span><span></span><span></span></button></div>'
            '</div></header>'
            '<div class="mobile" id="mobile" aria-hidden="true">'
            '<div class="mtop"><span class="eyebrow"><span class="star">✦</span> Menu</span>'
            '<button class="mclose" id="mclose">Close ✕</button></div>'
            '<a href="index.html">Home</a><a href="about.html">About</a>'
            '<a href="services.html">Services</a>'
            '<a href="seit.html" class="sub">SEIT Services</a>'
            '<a href="child-development.html" class="sub">Child Development Support</a>'
            '<a href="family-navigation.html" class="sub">Family Navigation</a>'
            '<a href="programs.html">Programs</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a>'
            '<div style="margin-top:22px"><a href="enroll.html" class="btn btn-gold" style="color:#fff">Begin Enrollment →</a></div>'
            '</div>') % (MARK, links)

FOOTER = ('<footer class="site"><div class="wrap"><div class="foot">'
          '<div><div class="brand" style="gap:11px">%s'
          '<span class="txt"><b style="color:#fff;font-family:\'Newsreader\',serif;font-size:20px">NorthStar</b>'
          '<small style="display:block;color:#8f9fbb;letter-spacing:.2em;font-size:9.5px;font-weight:800">CHILD DEVELOPMENT SERVICES</small></span></div>'
          '<p class="tag" style="margin-top:18px">Guiding Children, Empowering Futures.</p>'
          '<p>SEIT services and child development support for NYC families. Serving all five boroughs with care and clarity.</p></div>'
          '<div><h5>Services</h5><ul>'
          '<li><a href="seit.html">SEIT Services</a></li>'
          '<li><a href="child-development.html">Child Development Support</a></li>'
          '<li><a href="family-navigation.html">Family Navigation</a></li>'
          '<li><a href="programs.html">Programs</a></li></ul></div>'
          '<div><h5>Explore</h5><ul>'
          '<li><a href="about.html">About Us</a></li>'
          '<li><a href="enroll.html">Enrollment</a></li>'
          '<li><a href="faq.html">FAQ</a></li>'
          '<li><a href="contact.html">Contact</a></li></ul></div>'
          '<div><h5>Contact</h5><ul>'
          '<li><a href="tel:7185550134">(718) 555-0134</a></li>'
          '<li><a href="mailto:hello@northstarchilddevelopmentservices.com">Email us</a></li>'
          '<li>Response within 1 business day</li></ul></div>'
          '</div><div class="fbot">'
          '<span>&copy; <span id="yr">2026</span> NorthStar Child Development Services LLC. All rights reserved.</span>'
          '<span>Manhattan &middot; Brooklyn &middot; Queens &middot; Bronx &middot; Staten Island</span>'
          '</div></div></footer>') % MARK

def shell(title, desc, active, body):
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>'
            '<meta name="viewport" content="width=device-width, initial-scale=1"/>'
            '<title>%s</title><meta name="description" content="%s"/>'
            '<meta property="og:title" content="%s"/><meta property="og:description" content="%s"/>'
            '<link rel="preconnect" href="https://fonts.googleapis.com"/>'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>'
            '<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"/>'
            '<link rel="stylesheet" href="assets/style.css"/></head><body>'
            '%s<main>%s</main>%s<script src="assets/app.js"></script></body></html>'
            ) % (title, desc, title, desc, header(active), body, FOOTER)

def page_head(crumb, h1, p):
    return ('<section class="page-head"><div class="wrap">'
            '<div class="crumb rev"><a href="index.html">Home</a> &middot; %s</div>'
            '<h1 class="rev">%s</h1><p class="rev">%s</p></div></section>') % (crumb, h1, p)

def cta_band(h2="Ready to take the first step?", sub="We respond within one business day."):
    return ('<section class="band cream"><div class="wrap cta-band rev">'
            '<span class="eyebrow" style="justify-content:center"><span class="star">✦</span> Get started</span>'
            '<h2 style="margin-top:14px">%s</h2><p style="color:var(--muted);max-width:52ch;margin:0 auto">%s</p>'
            '<div class="btns"><a href="enroll.html" class="btn btn-gold">Begin Enrollment <span class="a">→</span></a>'
            '<a href="contact.html" class="btn btn-ghost">Contact Us</a></div></div></section>') % (h2, sub)

def service_cards():
    def c(anchor, im, t, p):
        return ('<article class="card rev"><div class="pic"><img src="%s" alt="%s" loading="lazy"/></div>'
                '<div class="body"><h3>%s</h3><p>%s</p>'
                '<div class="m"><a href="%s" class="tlink">Learn more <span class="a">→</span></a></div></div></article>'
                ) % (im, t, t, p, anchor)
    return ('<div class="grid-3">'
            + c("seit.html", TEACHER_ASSIST, "SEIT Services",
                "Individualized, one-on-one specialized instruction at home or in a center-based setting, guided by each child’s goals.")
            + c("child-development.html", BLOCKS, "Child Development Support",
                "Guidance for families navigating developmental milestones, evaluations, referrals, and next steps.")
            + c("family-navigation.html", FAMILY, "Family Navigation",
                "Help understanding the CPSE process, eligibility, and what to expect at every stage of your child’s journey.")
            + '</div>')

STEPS = ('<div class="steps">'
         '<div class="step rev"><div class="n">01</div><h4>Reach Out</h4><p>Contact us by form or phone. We respond promptly and clearly.</p></div>'
         '<div class="step rev d1"><div class="n">02</div><h4>Initial Consultation</h4><p>We learn about your child’s needs and explain available services.</p></div>'
         '<div class="step rev d2"><div class="n">03</div><h4>Intake &amp; Documentation</h4><p>We guide you through the information needed to move forward.</p></div>'
         '<div class="step rev d3"><div class="n">04</div><h4>Matching &amp; Planning</h4><p>Your child is connected with the right support for their needs.</p></div>'
         '<div class="step rev d3"><div class="n">05</div><h4>Ongoing Support</h4><p>Services begin with consistent communication every step of the way.</p></div>'
         '</div>')

def form(kind="contact"):
    extra = ''
    if kind == "enroll":
        extra = ('<div class="fld row"><div class="fld"><label for="age">Child’s age</label>'
                 '<select id="age" name="child_age"><option>Under 3</option><option>3 years</option><option>4 years</option><option>5 years</option></select></div>'
                 '<div class="fld"><label for="boro">Borough</label><select id="boro" name="borough">'
                 '<option>Manhattan</option><option>Brooklyn</option><option>Queens</option><option>Bronx</option><option>Staten Island</option></select></div></div>')
    subj = "New enrollment inquiry" if kind == "enroll" else "New inquiry"
    return ('<form class="cform rev" id="contactForm" action="https://api.web3forms.com/submit" method="POST">'
            '<input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY"/>'
            '<input type="hidden" name="subject" value="%s — NorthStar Child Development Services"/>'
            '<input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off"/>'
            '<div class="fld row"><div class="fld"><label for="name">Your name</label><input id="name" name="name" type="text" required placeholder="Full name"/></div>'
            '<div class="fld"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="(optional)"/></div></div>'
            '<div class="fld"><label for="email">Email</label><input id="email" name="email" type="email" required placeholder="you@email.com"/></div>'
            '%s'
            '<div class="fld"><label for="role">I am a…</label><select id="role" name="role">'
            '<option>Family / parent</option><option>Referral partner (attorney, advocate, evaluator, community)</option><option>Other</option></select></div>'
            '<div class="fld"><label for="message">How can we help?</label><textarea id="message" name="message" required placeholder="Tell us a little about your child or your inquiry."></textarea></div>'
            '<button type="submit" class="btn btn-gold" style="width:100%%;justify-content:center;color:#fff">Send message <span class="a">→</span></button>'
            '<p class="fnote">We respond within one business day. Your information is only used to reply to your inquiry.</p>'
            '<p class="fstatus" id="fstatus"></p></form>') % (subj, extra)

PAGES = {}

# ---------------- HOME ----------------
PAGES["index.html"] = shell(
 "NorthStar Child Development Services — SEIT &amp; Child Development Support in NYC",
 "SEIT and child development support for families across New York City’s five boroughs. Warm, clear guidance through evaluations, the CPSE process, and one-on-one preschool special education support.",
 "index.html",
 # hero
 ('<section class="hero"><div class="wrap hero-grid">'
  '<div><span class="eyebrow rev"><span class="star">✦</span> Warm, trusted support for NYC families</span>'
  '<h1 class="rev">Helping children grow with care, clarity, and support.</h1>'
  '<p class="lead rev">NorthStar Child Development Services provides SEIT and child development support for families across New York City — with warm guidance, plain language, and a calm, well-managed process from your first question to ongoing care.</p>'
  '<div class="cta rev"><a href="services.html" class="btn btn-navy">Explore Services <span class="a">→</span></a>'
  '<a href="enroll.html" class="btn btn-ghost">Begin Enrollment</a></div>'
  '<div class="badges rev"><div><span class="dot"></span> Ages 3–5 · one-on-one SEIT support</div>'
  '<div><span class="dot"></span> All five boroughs · at home or center-based</div>'
  '<div><span class="dot"></span> Response within one business day</div></div></div>'
  '<div class="media rev"><svg class="starfloat" viewBox="0 0 44 44" aria-hidden="true"><path d="M22 4l3.4 9.6L35 17l-9.6 3.4L22 30l-3.4-9.6L9 17l9.6-3.4L22 4z" fill="#C9A24B"/></svg>'
  '<div class="frame"><img src="%s" alt="A teacher warmly helping a young child learn"/>'
  '<video id="hv" autoplay muted loop playsinline preload="metadata" poster="%s"><source src="%s" type="video/mp4"/></video>'
  '<button class="vidbtn" data-vidbtn="hv" aria-label="Play or pause video">'
  '<svg class="ip" viewBox="0 0 24 24" fill="currentColor" style="display:none"><path d="M8 5v14l11-7z"/></svg>'
  '<svg class="ipp" viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg><span class="lb">Pause</span></button></div>'
  '<div class="chip"><b>One-on-one SEIT</b><span>At home or in a center-based setting</span></div></div>'
  '</div></section>') % (TEACHER_CHILD, TEACHER_CHILD, V_HOME)
 # trust bar
 + ('<section class="band" style="padding:44px 0"><div class="wrap trust rev">'
    '<div class="t"><b>5</b><span>NYC boroughs served</span></div>'
    '<div class="t"><b>3–5</b><span>ages supported</span></div>'
    '<div class="t"><b>1:1</b><span>individualized SEIT</span></div>'
    '<div class="t"><b>&lt;1 day</b><span>response time</span></div></div></section>')
 # services overview
 + ('<section class="band cream"><div class="wrap"><div class="shead rev">'
    '<span class="eyebrow"><span class="star">✦</span> What we offer</span>'
    '<h2>Services designed for your family’s journey</h2>'
    '<p>Every child’s path is different. We meet you where you are — explore each service in depth.</p></div>'
    + service_cards()
    + '<div class="rev" style="text-align:center;margin-top:34px"><a href="services.html" class="btn btn-ghost">View all services <span class="a">→</span></a></div>'
    + '</div></section>')
 # about teaser
 + ('<section class="band"><div class="wrap split"><div class="pic-frame rev"><img src="%s" alt="A family meeting warmly with a specialist"/></div>'
    '<div class="rev"><span class="eyebrow"><span class="star">✦</span> Why NorthStar</span>'
    '<h2 style="font-size:clamp(28px,3.4vw,42px);margin:14px 0 14px">Support that feels human, not overwhelming</h2>'
    '<p style="color:var(--muted);font-size:16.5px">Families tell us the hardest part isn’t the services — it’s the uncertainty. We lead with warm communication, plain language, and a simple intake, so you always know what comes next.</p>'
    '<div style="margin-top:22px"><a href="about.html" class="tlink">More about NorthStar <span class="a">→</span></a></div></div></div></section>') % FAMILY
 # programs teaser
 + ('<section class="band sky"><div class="wrap split wide-l"><div class="rev"><span class="eyebrow"><span class="star">✦</span> Programs</span>'
    '<h2 style="font-size:clamp(28px,3.4vw,42px);margin:14px 0 14px">Thoughtful programs for growing minds</h2>'
    '<p style="color:var(--muted);font-size:16.5px">From in-home SEIT to school-readiness and parent coaching, our programs are designed around your child — and your family’s peace of mind.</p>'
    '<div style="margin-top:22px"><a href="programs.html" class="btn btn-navy">Explore programs <span class="a">→</span></a></div></div>'
    '<div class="pic-frame rev"><img src="%s" alt="A young child engaged in developmental play"/></div></div></section>') % BLOCKS
 # quote
 + ('<section class="band"><div class="wrap quote rev">'
    '<p>“We lead with warm communication, plain language, and a simple intake — so you always know what comes next.”</p>'
    '<div class="who">NorthStar Child Development Services</div></div></section>')
 + cta_band()
)

# ---------------- ABOUT ----------------
PAGES["about.html"] = shell(
 "About Us — NorthStar Child Development Services",
 "NorthStar is a New York child development practice supporting families through SEIT and the preschool special education journey with warmth, clarity, and experienced care.",
 "about.html",
 page_head("About", "Guiding children, empowering futures.",
           "NorthStar Child Development Services helps New York City families navigate SEIT and early childhood support with warmth, clarity, and calm, well-organized care.")
 + ('<section class="band"><div class="wrap split"><div class="pic-frame pic-tall rev"><img src="%s" alt="A teacher helping a young child learn"/></div>'
    '<div class="prose rev"><span class="eyebrow"><span class="star">✦</span> Who we are</span>'
    '<h2 style="font-size:clamp(26px,3.2vw,38px);margin:12px 0 16px">A calmer way to find the right support</h2>'
    '<p>NorthStar Child Development Services is a New York–based practice supporting families through SEIT (Special Education Itinerant Teacher) services and the wider child development journey. We pair experienced, caring educators with a thoughtful, well-managed process — so your family feels informed and supported at every step.</p>'
    '<p>We know the preschool special education process can feel confusing and stressful. Our role is to make it clearer and calmer: explaining each stage in plain language, answering your questions honestly, and guiding you toward the right support for your child.</p>'
    '</div></div></section>') % TEACHER_CHILD
 + ('<section class="band cream"><div class="wrap"><div class="shead rev"><span class="eyebrow"><span class="star">✦</span> Our values</span>'
    '<h2>What families can count on</h2></div><div class="grid-2">'
    '<div class="icard rev"><div class="k">01</div><h3>Parent-centered communication</h3><p>You are the expert on your child. We listen first, keep you informed, and make sure your voice guides every decision.</p></div>'
    '<div class="icard rev d1"><div class="k">02</div><h3>Plain language, no jargon</h3><p>Evaluations, the CPSE, IEPs — we translate the acronyms and explain what each step actually means for your family.</p></div>'
    '<div class="icard rev d2"><div class="k">03</div><h3>Experienced NYC team</h3><p>Educators who understand New York City families and the local process, delivering warm, individualized instruction.</p></div>'
    '<div class="icard rev d3"><div class="k">04</div><h3>Clear next steps, every time</h3><p>You always know what comes next — and you never have to navigate the process alone.</p></div>'
    '</div></div></section>')
 + ('<section class="band"><div class="wrap"><div class="shead rev"><span class="eyebrow"><span class="star">✦</span> Where we work</span>'
    '<h2>Serving families across all five boroughs</h2>'
    '<p>Manhattan, Brooklyn, Queens, the Bronx, and Staten Island — with responsive, child-centered care.</p></div>'
    '<div class="rev" style="display:flex;justify-content:center"><div class="boroughs">'
    '<span>Manhattan</span><span>Brooklyn</span><span>Queens</span><span>Bronx</span><span>Staten Island</span></div></div></div></section>')
 + cta_band()
)

# ---------------- SERVICES HUB ----------------
PAGES["services.html"] = shell(
 "Services — NorthStar Child Development Services",
 "SEIT services, child development support, and family navigation for NYC families. Explore how NorthStar supports your child’s growth.",
 "services.html",
 page_head("Services", "Services designed for your family’s journey.",
           "Every child’s path is different. Explore our core services in depth — and see how we guide your family from first question to ongoing support.")
 + '<section class="band"><div class="wrap">' + service_cards() + '</div></section>'
 + ('<section class="band cream"><div class="wrap"><div class="shead rev"><span class="eyebrow"><span class="star">✦</span> The process</span>'
    '<h2>Simple steps toward the right support</h2><p>A clear, guided path — you always know what comes next.</p></div>'
    + STEPS + '</div></section>')
 + cta_band()
)

# ---------------- SEIT ----------------
def detail(active, crumb, h1, lead, im, video, poster, prose_h, prose_ps, listitems, im_is_video=False):
    media = ('<div class="pic-frame pic-tall rev">'
             + ('<video autoplay muted loop playsinline preload="metadata" poster="%s"><source src="%s" type="video/mp4"/></video>' % (poster, video) if im_is_video
                else '<img src="%s" alt="%s"/>' % (im, h1))
             + '</div>')
    lis = "".join('<li>%s %s</li>' % (CHECK, x) for x in listitems)
    ps = "".join('<p>%s</p>' % x for x in prose_ps)
    return shell(h1 + " — NorthStar Child Development Services", lead, active,
        page_head(crumb, h1, lead)
        + ('<section class="band"><div class="wrap split">%s'
           '<div class="prose rev"><h2 style="font-size:clamp(26px,3vw,36px);margin:0 0 16px">%s</h2>%s'
           '<ul>%s</ul>'
           '<div style="margin-top:26px"><a href="enroll.html" class="btn btn-gold">Begin Enrollment <span class="a">→</span></a></div>'
           '</div></div></section>') % (media, prose_h, ps, lis)
        + cta_band()
    )

PAGES["seit.html"] = detail("seit.html", '<a href="services.html">Services</a> &middot; SEIT Services',
    "SEIT Services", "One-on-one specialized instruction, guided by your child’s goals.",
    TEACHER_ASSIST, V_SEIT, TEACHER_ASSIST,
    "Individualized instruction, where your child already is",
    ["A Special Education Itinerant Teacher (SEIT) provides individualized, one-on-one specialized instruction for eligible preschool-age children (ages 3–5).",
     "Sessions take place where your child is most comfortable — at home or in a childcare or center-based setting — and are guided by each child’s specific goals.",
     "Our educators focus on the skills that matter most for your child’s growth, working in close partnership with you and any other providers involved."],
    ["One-on-one, individualized instruction", "At home or center-based", "For eligible children ages 3–5",
     "Goal-driven, in partnership with families", "Warm, consistent communication"],
    im_is_video=True)

PAGES["child-development.html"] = detail("child-development.html", '<a href="services.html">Services</a> &middot; Child Development Support',
    "Child Development Support", "Guidance through milestones, evaluations, and next steps.",
    BLOCKS, "", BLOCKS,
    "Steady guidance as your child grows",
    ["Every child develops at their own pace. When you have questions about milestones or next steps, we help you understand what you’re seeing and what your options are.",
     "We support families through developmental questions, evaluations, and referrals — connecting you with the right resources and explaining each step clearly.",
     "Our goal is simple: to replace uncertainty with clarity, so you can focus on your child."],
    ["Understanding developmental milestones", "Guidance around evaluations", "Referrals and resource connections",
     "Clear explanations, no jargon", "A partner from first question onward"])

PAGES["family-navigation.html"] = detail("family-navigation.html", '<a href="services.html">Services</a> &middot; Family Navigation',
    "Family Navigation", "Understand the CPSE process and what to expect at every stage.",
    FAMILY, "", FAMILY,
    "A guide through the CPSE journey",
    ["The CPSE (Committee on Preschool Special Education) determines a preschool child’s eligibility for services and the supports they’ll receive. It can feel overwhelming — we make it manageable.",
     "We help you understand eligibility, prepare for each meeting, and know what to expect at every stage of your child’s support journey.",
     "You’ll always have a clear picture of where you are in the process and what comes next."],
    ["Understanding the CPSE process", "Eligibility, explained simply", "What to expect at each stage",
     "Preparing for meetings with confidence", "A steady, reassuring guide"])

# ---------------- PROGRAMS ----------------
def prog(t, p):
    return '<div class="icard rev"><div class="k">Program</div><h3>%s</h3><p>%s</p><div class="m"><a href="enroll.html" class="tlink">Get started <span class="a">→</span></a></div></div>' % (t, p)

PAGES["programs.html"] = shell(
 "Programs — NorthStar Child Development Services",
 "In-home and center-based SEIT, school-readiness support, parent coaching, and developmental play groups for NYC preschoolers.",
 "programs.html",
 page_head("Programs", "Thoughtful programs for growing minds.",
           "Our programs are designed around your child — and your family’s peace of mind. Each one pairs individualized support with warm, consistent communication.")
 + ('<section class="band"><div class="wrap"><div class="grid-2">'
    + prog("In-Home SEIT", "One-on-one specialized instruction delivered in the comfort of your home, built around your child’s goals and daily routines.")
    + prog("Center-Based SEIT", "Individualized SEIT support within your child’s childcare or preschool setting, in coordination with their everyday environment.")
    + prog("School-Readiness Support", "Focused help building the foundational skills — attention, communication, social play — that set children up to thrive.")
    + prog("Parent Coaching &amp; Workshops", "Practical guidance and reassurance for parents, so the strategies that help your child extend naturally into home life.")
    + '</div></div></section>')
 + ('<section class="band cream"><div class="wrap split"><div class="pic-frame rev">'
    '<video autoplay muted loop playsinline preload="metadata" poster="%s"><source src="%s" type="video/mp4"/></video></div>'
    '<div class="prose rev"><span class="eyebrow"><span class="star">✦</span> Play with purpose</span>'
    '<h2 style="font-size:clamp(26px,3vw,36px);margin:12px 0 16px">Learning that feels like play</h2>'
    '<p>Young children learn best through play. Our programs use hands-on, developmentally appropriate activities that build real skills while keeping learning joyful.</p>'
    '<p>Every program is individualized, goal-driven, and delivered with the warm, plain-language communication families count on from NorthStar.</p>'
    '<div style="margin-top:22px"><a href="enroll.html" class="btn btn-navy">Begin Enrollment <span class="a">→</span></a></div></div></div></section>') % (BLOCKS, V_PLAY)
 + cta_band()
)

# ---------------- ENROLL ----------------
PAGES["enroll.html"] = shell(
 "Enrollment — NorthStar Child Development Services",
 "Begin enrollment with NorthStar Child Development Services. A calm, guided path to SEIT and child development support for your child.",
 "enroll.html",
 page_head("Enrollment", "A calm, guided path to getting started.",
           "Beginning services should feel reassuring, not overwhelming. Here’s exactly how enrollment works — and how to take the first step today.")
 + '<section class="band"><div class="wrap"><div class="shead rev"><span class="eyebrow"><span class="star">✦</span> How enrollment works</span><h2>Five simple steps</h2></div>' + STEPS + '</div></section>'
 + ('<section class="band cream"><div class="wrap split"><div class="prose rev"><span class="eyebrow"><span class="star">✦</span> Before you begin</span>'
    '<h2 style="font-size:clamp(26px,3vw,36px);margin:12px 0 16px">What helps us help you</h2>'
    '<p>You don’t need to have everything ready — we’ll guide you. If you have any of the following, it can help us move faster:</p>'
    '<ul><li>%s Your child’s age and borough</li><li>%s Any evaluations or reports you already have</li>'
    '<li>%s Notes on your questions or concerns</li><li>%s The best way and time to reach you</li></ul>'
    '<p style="margin-top:14px">Prefer to talk first? Call or text <a href="tel:7185550134" style="color:var(--teal);font-weight:800">(718) 555-0134</a>.</p></div>'
    '%s</div></section>') % (CHECK, CHECK, CHECK, CHECK, form("enroll"))
 + cta_band("Questions before you enroll?", "We’re happy to talk it through — no pressure, no jargon.")
)

# ---------------- FAQ ----------------
def q(s, a):
    return '<details class="q rev"><summary>%s</summary><p>%s</p></details>' % (s, a)

PAGES["faq.html"] = shell(
 "FAQ — NorthStar Child Development Services",
 "Answers to common questions about SEIT, eligibility, the CPSE process, cost, and getting started with NorthStar Child Development Services.",
 "faq.html",
 page_head("FAQ", "Frequently asked questions.",
           "Clear answers to what families ask us most. Still have a question? We’re one message away.")
 + ('<section class="band"><div class="wrap"><div class="faq">'
    + q("What is SEIT?", "SEIT (Special Education Itinerant Teacher) is individualized, one-on-one specialized instruction for preschool-age children (ages 3–5) who are eligible for preschool special education. Sessions take place where your child already is — at home or in a childcare or center-based setting.")
    + q("Who is eligible for services?", "Children ages 3–5 who are found eligible through the CPSE (Committee on Preschool Special Education) process. If your child hasn’t been evaluated yet, we can help you understand and navigate the steps.")
    + q("Is there a cost to families?", "For eligible children, preschool special education services such as SEIT are provided at no cost to families when authorized through the CPSE process. We’ll help you understand exactly what to expect.")
    + q("What is the CPSE process?", "The CPSE (Committee on Preschool Special Education) determines a preschool child’s eligibility for special education services and the supports they’ll receive. Our Family Navigation service helps you understand eligibility and each stage of the journey.")
    + q("Which areas do you serve?", "We serve families across all five NYC boroughs — Manhattan, Brooklyn, Queens, the Bronx, and Staten Island.")
    + q("How do I get started?", "Reach out through the enrollment form or by phone. We respond within one business day, learn about your child’s needs, and clearly explain the available services and next steps.")
    + '</div></div></section>')
 + cta_band()
)

# ---------------- CONTACT ----------------
PAGES["contact.html"] = shell(
 "Contact — NorthStar Child Development Services",
 "Contact NorthStar Child Development Services. Call, email, or send a message — we respond within one business day. Serving all five NYC boroughs.",
 "contact.html",
 page_head("Contact", "We’re here to help.",
           "Whether you’re a family just starting out or a referral partner looking to connect, reach out — we respond within one business day.")
 + ('<section class="band navy"><div class="wrap contact-grid"><div class="rev">'
    '<span class="eyebrow" style="color:var(--gold-bright)"><span class="star">✦</span> Get in touch</span>'
    '<h2 style="font-size:clamp(26px,3.4vw,40px);margin:14px 0 14px">Let’s take the first step together</h2>'
    '<p style="color:#c7d3e6;font-size:16.5px;max-width:44ch">Have a question about services, programs, or the process? We’d love to hear from you.</p>'
    '<div class="cinfo">'
    '<a href="tel:7185550134"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 4h4l2 5-3 2a12 12 0 005 5l2-3 5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/></svg></span><span><b>(718) 555-0134</b><span>Call or text</span></span></a>'
    '<a href="mailto:hello@northstarchilddevelopmentservices.com"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span><span><b>hello@northstarchilddevelopmentservices.com</b><span>Email us anytime</span></span></a>'
    '<div class="row"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><span><b>Response within 1 business day</b><span>Serving all five boroughs</span></span></div>'
    '</div></div>' + form("contact") + '</div></section>')
)

for name, html in PAGES.items():
    with io.open(name, "w", encoding="utf-8") as fh:
        fh.write(html)
print("generated", len(PAGES), "pages:", ", ".join(sorted(PAGES)))
