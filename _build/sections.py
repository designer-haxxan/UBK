"""Reusable page sections shared across several UBK pages."""

from core import t, img, is_ur


# ---------------------------------------------------------------- logos strip

def logos_strip(caption=True, cls=""):
    logos = [("logo-figma.png", "Figma"), ("logo-wifaq.png", "Wifaq ul Madaris"), ("logo-adobe.png", "Adobe"),
             ("logo-google-ads.png", "Google Ads"), ("logo-meta.png", "Meta"), ("logo-capcut.png", "CapCut")]
    items = "".join(f'<img src="{img(f)}" alt="{a}" loading="lazy">' for f, a in logos)
    cap = f'<p class="caption">{t("Guided by scholars and industry professionals", "علما اور فیلڈ کے ماہرین کی نگرانی میں")}</p>' if caption else ""
    return f"""
  <section class="logos-strip {cls}">
    <div class="container">
      {cap}
      <div class="marquee" aria-label="{t('Partners and tools', 'شراکت دار اور ٹولز')}">
        <div class="marquee-track">{items}{items}{items}{items}</div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- stats band

def stats_band(contained=True):
    stats = [
        (100, "%", False, t("Scholarship Option", "اسکالرشپ آپشن")),
        (4, "", True, t("Core Skill Tracks", "بنیادی مہارت ٹریکس")),
        (500, "+", False, t("Students Trained", "تربیت یافتہ طلبہ")),
        (3, "", True, t("Ways to Pay", "ادائیگی کے طریقے")),
    ]
    cells = "".join(
        f'<div class="col-6 col-md-3 stat"><div class="num" data-count="{n}" data-suffix="{s}" data-pad="{str(p).lower()}">0</div><div class="lbl">{l}</div></div>'
        for n, s, p, l in stats
    )
    inner = f'<div class="stats-band{" rounded-band" if contained else ""}" data-aos="fade-up"><div class="row g-0">{cells}</div></div>'
    if contained:
        return f'<div class="container">{inner}</div>'
    return inner


# ---------------------------------------------------------------- tracks

def tracks_grid(title=None, lead=None, view_all=False):
    title = title or t("Explore Our Income-<br>Focused Skill Tracks", "روزگار سے جڑے عملی ہنر سیکھیں")
    lead = lead or t("Four practical tracks, taught by working professionals and built around real client work.",
                     "چار عملی شعبے، جن کی تربیت تجربہ کار ماہرین حقیقی کلائنٹ ورک کے ذریعے دیتے ہیں۔")
    cards = [
        ("ecommerce.html", "track-ecommerce.jpg", t("eCommerce", "ای کامرس"),
         t("Source, list and sell products on local and international marketplaces.",
           "مقامی اور عالمی مارکیٹس میں مصنوعات تلاش کرنا، لسٹ کرنا اور فروخت کرنا سیکھیں۔")),
        ("digital-marketing.html", "track-marketing.jpg", t("Digital Marketing", "ڈیجیٹل مارکیٹنگ"),
         t("Run ads, manage social pages and bring paying customers to a business.",
           "اشتہارات چلانا، سوشل میڈیا سنبھالنا اور کاروبار کے لیے گاہک لانا سیکھیں۔")),
        ("graphic-design.html", "track-design.jpg", t("Graphic Design", "گرافک ڈیزائن"),
         t("Design logos, social posts and brand material clients actually pay for.",
           "کلائنٹس کے لیے لوگو، سوشل میڈیا پوسٹس اور برانڈنگ مواد تیار کرنا سیکھیں۔")),
        ("video-editing.html", "track-video.jpg", t("Video Editing", "ویڈیو ایڈیٹنگ"),
         t("Cut, caption and colour video for creators, brands and campaigns.",
           "کریئیٹرز، برانڈز اور اشتہارات کے لیے ویڈیو ایڈٹ کرنا، کیپشن لگانا اور رنگ بہتر بنانا سیکھیں۔")),
    ]
    items = "".join(f"""
        <div class="col-6 col-lg-3" data-aos="fade-up" data-aos-delay="{i * 100}">
          <a class="track-card" href="{href}">
            <img src="{img(im)}" alt="{name}" loading="lazy">
            <span class="go"><i class="bi bi-arrow-up-right"></i></span>
            <div class="body"><h3>{name}</h3><p>{desc}</p></div>
          </a>
        </div>""" for i, (href, im, name, desc) in enumerate(cards))
    link_all = f'<a href="courses.html" class="link-arrow mt-2">{t("View all four tracks", "چاروں کورسز دیکھیں")} <i class="bi bi-arrow-right"></i></a>' if view_all else ""
    return f"""
  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{title}</h2>
        <div data-aos="fade-up" data-aos-delay="100"><p class="section-lead">{lead}</p>{link_all}</div>
      </div>
      <div class="row g-3">{items}</div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- student work slider

WORK = [
    ("work-store.jpg", "ecommerce", t, "Online Store Setup & Launch", "آن لائن اسٹور سیٹ اپ اور لانچ"),
    ("work-brand.jpg", "design", t, "Brand Identity & Design Kit", "برانڈ شناخت اور ڈیزائن کٹ"),
    ("work-social.jpg", "marketing", t, "Social Media Campaign", "سوشل میڈیا مہم"),
    ("work-store.jpg", "ecommerce", t, "Product Listing Launch", "پروڈکٹ لسٹنگ لانچ"),
    ("work-brand.jpg", "design", t, "Café Branding Package", "کیفے برانڈنگ پیکج"),
]


def work_slider(cls=""):
    slides = "".join(f"""
        <div><a class="work-card" href="student-work.html">
          <div class="media"><img src="{img(im)}" alt="{tr(en, ur)}" loading="lazy"></div>
          <div class="meta"><small>© 2026 — UBK</small><h4>{tr(en, ur)}</h4></div>
        </a></div>""" for im, _, tr, en, ur in WORK)
    return f"""
  <section class="section {cls}">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Real Client Work<br>Our Students Deliver', 'حقیقی کلائنٹس کے لیے<br>ہمارے طلبہ کا کام')}</h2>
        <div class="d-flex flex-column gap-3 align-items-lg-end" data-aos="fade-up" data-aos-delay="100">
          <p class="section-lead">{t('Every track ends with live projects our students complete for real businesses.', 'ہر کورس کے اختتام پر طلبہ حقیقی کاروباروں کے لیے عملی پروجیکٹس مکمل کرتے ہیں۔')}</p>
          <div class="slider-nav"><button class="prev" aria-label="{t('Previous', 'پچھلا')}"><i class="bi bi-arrow-left"></i></button><button class="next" aria-label="{t('Next', 'اگلا')}"><i class="bi bi-arrow-right"></i></button></div>
        </div>
      </div>
      <div class="work-slider" data-aos="fade-up">{slides}</div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- scholars accordion

def scholars_section():
    items = [
        (t("Scholar Supervised", "اساتذہ کی نگرانی میں"),
         t("Every course runs under the supervision of respected scholars, so your training never conflicts with your values.",
           "ہر کورس معزز اساتذہ کی نگرانی میں چلتا ہے، تاکہ آپ کی تربیت آپ کی اقدار سے کبھی نہ ٹکرائے۔")),
        (t("Industry Mentors", "فیلڈ کے ماہرین کی رہنمائی"),
         t("Learn directly from designers, marketers and sellers who earn from these skills every day.",
           "ان ڈیزائنرز، مارکیٹرز اور سیلرز سے براہ راست سیکھیں جو روزانہ انہی مہارتوں سے کماتے ہیں۔")),
        (t("Real Client Projects", "اصل کلائنٹس کے پروجیکٹس"),
         t("You finish each track with live work for real businesses — not practice exercises.",
           "ہر کورس کے آخر میں آپ حقیقی کاروباروں کے لیے اصل کام کرتے ہیں — صرف مشقیں نہیں۔")),
        (t("Freelance Support", "فری لانس کام میں مدد"),
         t("We help you set up profiles, price your work and land your first paying clients.",
           "ہم پروفائل بنانے، کام کی قیمت طے کرنے اور پہلے کلائنٹس حاصل کرنے میں آپ کی مدد کرتے ہیں۔")),
    ]
    acc = "".join(f"""
          <div class="acc-item{' open' if i == 0 else ''}">
            <button class="acc-head" aria-expanded="{'true' if i == 0 else 'false'}">{h}<i class="bi bi-caret-down-fill caret"></i></button>
            <div class="acc-body">{b}</div>
          </div>""" for i, (h, b) in enumerate(items))
    return f"""
  <section class="section pt-0">
    <div class="container">
      <div class="row g-5 align-items-stretch">
        <div class="col-lg-6" data-aos="fade-right">
          <div class="scholars-media"><img src="{img('scholars.jpg')}" alt="{t('Scholar mentoring a student', 'استاد طالب علم کی رہنمائی کرتے ہوئے')}" loading="lazy"></div>
        </div>
        <div class="col-lg-6 d-flex flex-column justify-content-center" data-aos="fade-left">
          <h2 class="section-title mb-4">{t('Built for Scholars,<br>Driven by Results', 'فضلا مدارس کے لیے،<br>عملی کامیابی کے ساتھ')}</h2>
          <div class="ubk-acc">{acc}</div>
        </div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- skills timeline

def skills_section(cls=""):
    learn = [
        t("Structured, Step-By-Step Curriculum", "مرحلہ وار مکمل نصاب"),
        t("Hands-On Project Experience", "عملی پروجیکٹس کا تجربہ"),
        t("Real Client Case Studies", "اصل کلائنٹس کی کیس اسٹڈیز"),
        t("Regular Feedback & Assessment", "باقاعدہ فیڈبیک اور جائزہ"),
        t("Flexible Class Timings", "لچکدار کلاس اوقات"),
        t("Career-Focused Assignments", "کیریئر پر مبنی اسائنمنٹس"),
    ]
    get = [
        t("Practical, Skill-Based Training", "عملی، مہارت پر مبنی تربیت"),
        t("Market-Ready Portfolio", "مارکیٹ کے لیے تیار پورٹ فولیو"),
        t("Clear Goals & Progress Milestones", "واضح اہداف اور ترقی کے سنگِ میل"),
        t("Industry-Relevant Knowledge", "انڈسٹری سے متعلق علم"),
        t("Freelance & Marketplace Guidance", "فری لانس اور مارکیٹ پلیس رہنمائی"),
        t("Confidence to Earn Independently", "خود مختار طریقے سے کمانے کا اعتماد"),
    ]
    li_l = "".join(f'<li data-aos="fade-right" data-aos-delay="{i * 80}">{x}</li>' for i, x in enumerate(learn))
    li_g = "".join(f'<li data-aos="fade-left" data-aos-delay="{i * 80}">{x}</li>' for i, x in enumerate(get))
    return f"""
  <section class="section {cls}">
    <div class="container">
      <div class="text-center mb-5" data-aos="fade-up">
        <h2 class="section-title">{t('Skills That Prepare You<br>for Real Earning', 'وہ مہارتیں جو آپ کو<br>واقعی کمانے کے قابل بنائیں')}</h2>
        <p class="section-lead mx-auto mt-3" style="max-width:320px">{t('Every track is built to move you from your first lesson to your first paid piece of work.', 'سیکھنے سے لے کر کمانے تک، ہر چیز عملی انداز میں۔')}</p>
      </div>
      <div class="skills-grid">
        <div class="skills-col learn"><h4>{t('What You Learn', 'آپ کیا سیکھیں گے')}</h4><ul>{li_l}</ul></div>
        <div class="skills-line" data-rows="6"></div>
        <div class="skills-col get"><h4>{t('What You Get', 'آپ کو کیا ملے گا')}</h4><ul>{li_g}</ul></div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- testimonials

def testimonials_section():
    slides = [
        (t("“I started with no computer background at all. By the third month I was running my own store.”",
           "“میرے پاس کمپیوٹر کا کوئی تجربہ نہیں تھا۔ تیسرے مہینے تک میں اپنا آن لائن اسٹور چلا رہا تھا۔”"),
         t("Bilal Ahmed", "بلال احمد"), t("eCommerce Track", "ای کامرس ٹریک"),
         [t("eCommerce", "ای کامرس"), t("Scholarship", "اسکالرشپ")]),
        (t("“My first client paid me for my first project while my course was still running.”",
           "“میرے پہلے کلائنٹ نے مجھے میرے پہلے پروجیکٹ پر ادائیگی کر دی جبکہ میرا کورس ابھی چل رہا تھا۔”"),
         t("Abdullah Shah", "عبداللہ شاہ"), t("Video Editing Track", "ویڈیو ایڈیٹنگ ٹریک"),
         [t("Freelance", "فری لانس"), t("Video", "ویڈیو")]),
    ]
    html = "".join(f"""
          <div><div class="quote-card">
            <blockquote>{q}</blockquote>
            <div class="person">
              <img src="{img('avatar-bilal.jpg')}" alt="{n}" loading="lazy">
              <div><div class="qmark">“</div><div class="name">{n}</div><div class="role">{r}</div></div>
              <div class="tags">{''.join(f'<span>{x}</span>' for x in tags)}</div>
            </div>
          </div></div>""" for q, n, r, tags in slides)
    return f"""
  <section class="section testimonials">
    <span class="blob b1"></span><span class="blob b2"></span>
    <div class="container position-relative">
      <div class="row g-5 align-items-center">
        <div class="col-lg-4 d-flex flex-column" data-aos="fade-up">
          <h2 class="section-title">{t('What Our<br>Students Say', 'ہمارے طلبہ<br>کیا کہتے ہیں')}</h2>
          <p class="section-lead mt-3" style="max-width:260px">{t('Real feedback from scholars who completed a track at UBK.', 'UBK سے کورس مکمل کرنے والے طلبہ کے اپنے تجربات۔')}</p>
          <div class="mt-5"><a href="courses.html" class="btn-ubk btn-sm-ubk">{t('Explore Courses', 'کورسز دیکھیں')}</a></div>
        </div>
        <div class="col-lg-7 offset-lg-1" data-aos="fade-left">
          <div class="testimonial-slider">{html}</div>
        </div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- pricing / three ways

def pricing_cards():
    ok, no = '<i class="bi bi-check2"></i>', '<i class="bi bi-x"></i>'

    def li(items):
        return "".join(f"<li>{ok if good else no}{txt}</li>" for good, txt in items)

    full = t("Full course access", "مکمل کورس تک رسائی")
    mat = t("All learning material", "تمام تعلیمی مواد")
    live = t("Live mentor sessions", "لائیو مینٹر سیشنز")
    cert = t("Certificate on completion", "مکمل ہونے پر سرٹیفکیٹ")
    free = t("Freelance setup support", "فری لانس سیٹ اپ سپورٹ")
    cards = [
        ("", t("Scholarship", "اسکالرشپ"), t("Free", "مکمل مفت"), t("100% covered", "100٪ اخراجات شامل"),
         t("For deserving students who apply and qualify through our review process.",
           "ان طلبہ کے لیے جو درخواست اور جانچ کے بعد اسکالرشپ کے اہل قرار پائیں۔"),
         li([(1, full), (1, mat), (1, live), (1, cert), (0, free), (0, t("Application and review required", "درخواست اور جائزہ ضروری"))])),
        ("featured", t("Sponsored", "ادائیگی بعد میں"), t("Later", "پہلے سیکھیں"), t("pay once you earn", "کمائی شروع ہونے پر ادائیگی"),
         t("Study now, return the fee once you start earning from a job or freelancing.",
           "ابھی سیکھیں، نوکری یا فری لانسنگ سے کمائی شروع ہونے پر فیس واپس کریں۔"),
         li([(1, full), (1, mat), (1, live), (1, cert), (1, free), (1, t("Nothing to pay until you earn", "کمائی تک کوئی ادائیگی نہیں"))])),
        ("", t("Self-Paid", "براہ راست ادائیگی"), t("Direct", "براہِ راست"), t("pay and start", "فیس دیں اور شروع کریں"),
         t("Pay your fee directly and start straight away, with no application waiting period.",
           "اپنی فیس براہ راست ادا کریں اور بغیر کسی انتظار کے فوراً شروع کریں۔"),
         li([(1, full), (1, mat), (1, live), (1, cert), (1, free), (1, t("Immediate enrolment, no waiting", "فوری داخلہ، کوئی انتظار نہیں"))])),
    ]
    return "".join(f"""
        <div class="col-md-4" data-aos="fade-up" data-aos-delay="{i * 120}">
          <a href="apply.html" class="price-card d-block {c}">
            <span class="tag">{tag}</span>
            <div class="head"><h3>{h}</h3><span class="sub">{sub}</span><span class="go"><i class="bi bi-arrow-up-right"></i></span></div>
            <p class="desc">{d}</p>
            <ul>{lis}</ul>
          </a>
        </div>""" for i, (c, tag, h, sub, d, lis) in enumerate(cards))


def pricing_section(cls=""):
    return f"""
  <section class="section {cls}">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Three Ways to<br>Start Learning at UBK', 'UBK میں سیکھنا شروع<br>کرنے کے تین طریقے')}</h2>
        <p class="section-lead" data-aos="fade-up" data-aos-delay="100">{t('Cost should never be the reason you stay behind. Choose the route that fits your situation.', 'فیس کو اپنی ترقی میں رکاوٹ نہ بننے دیں۔ اپنی سہولت کے مطابق راستہ منتخب کریں۔')}</p>
      </div>
      <div class="row g-3">{pricing_cards()}</div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- FAQ cards

def faq_cards_section(cls=""):
    faqs = [
        ("bi-book", t("Who can enrol at UBK?", "UBK میں کون داخلہ لے سکتا ہے؟"),
         t("Any madrasa graduate, and anyone else willing to learn. No prior computer experience is required — every track begins from the very first step.",
           "کوئی بھی مدرسہ فارغ التحصیل، اور ہر وہ شخص جو سیکھنا چاہے۔ کمپیوٹر کا پہلے سے تجربہ ضروری نہیں — ہر کورس بالکل بنیاد سے شروع ہوتا ہے۔")),
        ("bi-patch-check", t("Do I get a certificate after completion?", "کیا کورس مکمل کرنے پر سرٹیفکیٹ ملتا ہے؟"),
         t("Yes. Every student who completes the attendance, projects and final assessment receives a UBK certificate.",
           "جی ہاں۔ حاضری، پروجیکٹس اور آخری جائزہ مکمل کرنے والے ہر طالب علم کو UBK سرٹیفکیٹ دیا جاتا ہے۔")),
        ("bi-mortarboard", t("Do I really pay nothing on a scholarship?", "کیا اسکالرشپ پر واقعی کوئی فیس نہیں دینی ہوتی؟"),
         t("Correct. Scholarship students pay no tuition fee at all — the full course, material and mentor sessions are covered.",
           "بالکل۔ اسکالرشپ والے طلبہ کوئی فیس ادا نہیں کرتے — مکمل کورس، مواد اور مینٹر سیشنز سب شامل ہیں۔")),
        ("bi-mortarboard", t("Are the courses beginner friendly?", "کیا یہ کورسز نئے سیکھنے والوں کے لیے بھی آسان ہیں؟"),
         t("Yes. Lessons start with the basics and mentors support you one-to-one until you are confident.",
           "جی ہاں۔ اسباق بنیادی باتوں سے شروع ہوتے ہیں اور مینٹرز اعتماد آنے تک انفرادی رہنمائی کرتے ہیں۔")),
    ]
    cards = "".join(f"""
          <div class="faq-card{' open' if i == 0 else ''}" data-aos="zoom-in" data-aos-delay="{i * 90}" role="button" tabindex="0">
            <i class="bi {ic} ico"></i><h4>{q}</h4><p class="ans">{a}</p>
          </div>""" for i, (ic, q, a) in enumerate(faqs))
    return f"""
  <section class="section {cls}">
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-4 d-flex flex-column justify-content-between" data-aos="fade-up">
          <h2 class="section-title">{t('Frequently<br>Asked<br>Questions', 'اکثر پوچھے<br>جانے والے سوالات')}</h2>
          <div class="mt-4">
            <p class="section-lead mb-3" style="max-width:190px">{t('Everything you need to know before you apply.', 'اپلائی کرنے سے پہلے آپ کو جو کچھ جاننا ضروری ہے۔')}</p>
            <a href="contact.html" class="btn-ubk btn-sm-ubk">{t('Contact Us', 'ہم سے رابطہ کریں')}</a>
          </div>
        </div>
        <div class="col-lg-8"><div class="faq-grid">{cards}</div></div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- CTAs

def cta_wide(cls=""):
    return f"""
  <section class="section-sm {cls}">
    <div class="container">
      <div class="cta-wide" data-aos="fade-up">
        <div class="media"><img src="{img('cta-student.jpg')}" alt="{t('UBK student', 'UBK کا طالب علم')}" loading="lazy"></div>
        <div class="cta-box">
          <h2>{t('Start Earning From Your Skills Today', 'آج ہی اپنی مہارتوں سے کمانا شروع کریں')}</h2>
          <p>{t('Applications for the next batch are open. Apply in five minutes and our team will contact you.', 'اگلے بیچ کے لیے داخلے جاری ہیں۔ پانچ منٹ میں اپلائی کریں، ہماری ٹیم آپ سے رابطہ کرے گی۔')}</p>
          <div><a href="apply.html" class="btn-ubk btn-white btn-sm-ubk">{t('Apply Now', 'ابھی اپلائی کریں')}</a></div>
        </div>
      </div>
    </div>
  </section>
"""


def cta_trio(cls=""):
    return f"""
  <section class="section-sm {cls}">
    <div class="container">
      <div class="cta-trio">
        <div class="media" data-aos="fade-up"><img src="{img('cta-left.jpg')}" alt="{t('UBK student in class', 'کلاس میں UBK کا طالب علم')}" loading="lazy"></div>
        <div class="cta-box" data-aos="fade-up" data-aos-delay="100">
          <h2>{t('Start Earning From Your Skills Today', 'آج ہی اپنی مہارتوں سے کمانا شروع کریں')}</h2>
          <p>{t('Applications for the next batch are open. Apply in five minutes.', 'اگلے بیچ کے لیے داخلے جاری ہیں۔ پانچ منٹ میں اپلائی کریں۔')}</p>
          <div><a href="apply.html" class="btn-ubk btn-white btn-sm-ubk">{t('Apply Now', 'ابھی اپلائی کریں')}</a></div>
        </div>
        <div class="media" data-aos="fade-up" data-aos-delay="200"><img src="{img('cta-right.jpg')}" alt="{t('UBK student working', 'کام کرتا ہوا UBK کا طالب علم')}" loading="lazy"></div>
      </div>
    </div>
  </section>
"""
