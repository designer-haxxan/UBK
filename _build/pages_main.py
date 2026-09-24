"""Home, About, Courses and the four course-detail pages."""

from core import t, img, page_hero
from sections import (logos_strip, stats_band, tracks_grid, work_slider, scholars_section, skills_section,
                      testimonials_section, pricing_section, faq_cards_section, cta_wide, cta_trio)


# ================================================================= HOME

def home():
    meta = (t("UBK — Rooted in ilm. Equipped for the digital future.", "UBK — دینی علم کے ساتھ جدید ہنر"),
            t("Practical training in eCommerce, digital marketing, graphic design and video editing for madrasa graduates.",
              "مدارس کے فارغ التحصیل طلبہ کے لیے ای کامرس، ڈیجیٹل مارکیٹنگ، گرافک ڈیزائن اور ویڈیو ایڈیٹنگ کی عملی تربیت۔"))
    h1 = t(
        '<span class="reveal-line"><span>Rooted in ilm.</span></span>'
        '<span class="reveal-line"><span>Equipped for the</span></span>'
        '<span class="reveal-line"><span class="text-orange">Digital Future.</span></span>',
        '<span class="reveal-line"><span>دینی علم کے ساتھ جدید</span></span>'
        '<span class="reveal-line"><span>ہنر سیکھیں،</span></span>'
        '<span class="reveal-line"><span class="text-orange">اپنا ڈیجیٹل مستقبل</span></span>'
        '<span class="reveal-line"><span class="text-orange">سنواریں۔</span></span>')
    body = f"""
  <section class="hero-home">
    <div class="container">
      <div class="row align-items-center g-4">
        <div class="col-lg-6">
          <h1>{h1}</h1>
          <p class="subtitle fade-in-up d-2">{t('Modern Skills for Madrasa Graduates', 'مدارس کے فارغ التحصیل طلبہ کے لیے جدید ڈیجیٹل کورسز')}</p>
          <p class="lead-text fade-in-up d-2">{t('Practical training in eCommerce, marketing, design and video — built for scholars who want to earn independently.', 'ای کامرس، مارکیٹنگ، ڈیزائن اور ویڈیو کی عملی تربیت — ان علما کے لیے جو جدید ہنر سیکھ کر خود مختار طریقے سے کمانا چاہتے ہیں۔')}</p>
          <a href="courses.html" class="btn-ubk btn-orange btn-sm-ubk mt-4 fade-in-up d-3">{t('Explore Courses', 'کورسز دیکھیں')}</a>

          <div class="scholar-card fade-in-up d-4">
            <span class="pill-badge"><span class="ico"><i class="bi bi-mortarboard-fill"></i></span>{t('100% Scholarship', '100% اسکالرشپ')}</span>
            <h6>{t('Apply, qualify, and study without paying any fee.', 'درخواست دیں، اسکالرشپ حاصل کریں اور بالکل مفت سیکھیں۔')}</h6>
            <div class="social-proof">
              <img class="avatars" src="{img('avatars.png')}" alt="">
              <div><strong>1.5k+</strong>{t('satisfied Students', 'مطمئن طلبہ')}</div>
              <span class="divider"></span>
              <div><strong>5 <small style="font-size:.6rem">.0</small> <span class="stars">★★★★★</span></strong>{t('rated happy students', 'طلبہ کی ریٹنگ')}</div>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="hero-bento">
            <div class="col-a" style="transition:transform .6s cubic-bezier(.22,1,.36,1)">
              <div class="bento-img h-1 pop d-1"><img src="{img('hero-student.jpg')}" alt="{t('Student learning on a laptop', 'لیپ ٹاپ پر سیکھتا طالب علم')}"></div>
              <div class="pop d-2"><div class="bento-card float-y">
                <p class="quote">{t('“I completed my first paid order in the second month.”', '“میں نے دوسرے ہی مہینے اپنا پہلا پیڈ آرڈر مکمل کیا۔”')}</p>
                <a href="apply.html" class="btn-mini">{t('Apply for 100% Free Scholarship', 'مکمل مفت اسکالرشپ کے لیے اپلائی کریں')}</a>
              </div></div>
              <div class="bento-card pop d-3">
                <div class="num" data-count="4" data-pad="true">04</div>
                <small>{t('Skill tracks built around<br>real client work', 'حقیقی کلائنٹ ورک پر مبنی<br>چار کورسز')}</small>
              </div>
            </div>
            <div class="col-b" style="transition:transform .6s cubic-bezier(.22,1,.36,1)">
              <div class="bento-img h-2 pop d-2"><img src="{img('hero-orange.jpg')}" alt="{t('Scholar working on digital marketing', 'ڈیجیٹل مارکیٹنگ پر کام کرتا عالم')}"></div>
              <div class="bento-img h-3 overlay pop d-3"><img src="{img('hero-campus.jpg')}" alt="{t('Students training on campus', 'کیمپس میں تربیت لیتے طلبہ')}"><span class="label">{t('On-Campus Training', 'آن کیمپس تربیت')}</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  {logos_strip()}

  <section class="section pb-4">
    <div class="container">
      <div class="row g-5 align-items-center">
        <div class="col-lg-5" data-aos="fade-right">
          <h2 class="section-title">{t('Training Built<br>for Real Income', 'عملی تربیت، بہتر روزگار<br>کی مضبوط بنیاد')}</h2>
          <p class="mt-3" style="max-width:300px;font-size:.9rem">{t('UBK is a Pakistan-based institute equipping madrasa graduates with practical, income-earning skills.', 'UBK پاکستان کا تربیتی ادارہ ہے، جو مدارس کے فضلا کو بہتر روزگار کے لیے عملی اور جدید ہنر سکھاتا ہے۔')}</p>
          <a href="about.html" class="btn-ubk btn-sm-ubk mt-4">{t('Explore Courses', 'مزید جانیں')}</a>
        </div>
        <div class="col-lg-6 offset-lg-1" data-aos="zoom-in-up">
          <div class="split-media">
            <span class="badge-orange"><i class="bi bi-check2"></i> {t('Scholar Supervised', 'اساتذہ کی زیرِ نگرانی')}</span>
            <img src="{img('training.jpg')}" alt="{t('Mentor guiding a student', 'استاد طالب علم کی رہنمائی کرتے ہوئے')}">
            <div class="chip-stack"><span>{t('eCommerce', 'ای کامرس')}</span><span>{t('Digital Marketing', 'ڈیجیٹل مارکیٹنگ')}</span><span>{t('Graphic Design', 'گرافک ڈیزائن')}</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  {stats_band()}
  {tracks_grid()}
  {work_slider("pt-0")}
  {scholars_section()}
  {skills_section()}
  {testimonials_section()}
  {pricing_section()}
  {faq_cards_section("pt-0")}
  {cta_wide("pt-0")}
"""
    return meta, body


# ================================================================= ABOUT

def about():
    meta = (t("About UBK", "UBK کا تعارف"),
            t("UBK is a Pakistan-based skills institute that equips madrasa graduates with practical, income-earning digital skills.",
              "UBK پاکستان کا تربیتی ادارہ ہے جو مدارس کے فضلا کو عملی اور آمدنی والے ڈیجیٹل ہنر سکھاتا ہے۔"))
    teach = [
        (t("Scholar Supervised", "اساتذہ کی نگرانی میں"),
         t("Every class is overseen by qualified Islamic scholars who ensure the learning environment stays true to your values.",
           "ہر کلاس مستند علما کی نگرانی میں ہوتی ہے، جو یقینی بناتے ہیں کہ تعلیمی ماحول آپ کی اقدار کے مطابق رہے۔")),
        (t("Industry Mentors", "فیلڈ کے ماہرین کی رہنمائی"),
         t("Working designers, marketers and sellers teach the skills they use with paying clients every week.",
           "تجربہ کار ڈیزائنرز، مارکیٹرز اور سیلرز وہی ہنر سکھاتے ہیں جو وہ ہر ہفتے اپنے کلائنٹس کے لیے استعمال کرتے ہیں۔")),
        (t("Real Client Projects", "اصل کلائنٹس کے پروجیکٹس"),
         t("From the middle of each track you work on live briefs from real businesses, building a portfolio as you learn.",
           "ہر کورس کے درمیان سے ہی آپ حقیقی کاروباروں کے اصل پروجیکٹس پر کام کرتے ہیں اور ساتھ ساتھ پورٹ فولیو بناتے ہیں۔")),
        (t("Freelance Support", "فری لانس کام میں مدد"),
         t("We help you set up marketplace profiles, price your services and win your first clients.",
           "ہم مارکیٹ پلیس پروفائل بنانے، سروسز کی قیمت طے کرنے اور پہلے کلائنٹس حاصل کرنے میں مدد کرتے ہیں۔")),
    ]
    acc = "".join(f"""<div class="acc-item{' open' if i == 0 else ''}"><button class="acc-head">{h}<i class="bi bi-caret-down-fill caret"></i></button><div class="acc-body">{b}</div></div>"""
                  for i, (h, b) in enumerate(teach))
    campus = [
        ("campus-hall.jpg", t("Main Training Hall", "مرکزی تربیتی ہال")),
        ("campus-lab.jpg", t("Computer Lab", "کمپیوٹر لیب")),
        ("campus-mentoring.jpg", t("Mentoring Room", "مینٹورنگ روم")),
        ("hero-campus.jpg", t("Group Study Area", "گروپ اسٹڈی ایریا")),
    ]
    slides = "".join(f"""<div><div class="campus-card"><div class="media"><img src="{img(im)}" alt="{n}" loading="lazy"></div><div class="cap"><small>{t('Campus', 'کیمپس')}</small><h4>{n}</h4></div></div></div>""" for im, n in campus)
    body = f"""
  {page_hero(t('About UBK', 'UBK کا تعارف'), t('Rooted in ilm.<br>Built for real income.', 'دینی علم میں جڑیں،<br>حقیقی آمدنی کے لیے تیار۔'),
             t('UBK is a Pakistan-based skills institute that equips madrasa graduates with practical, income-earning digital skills.', 'UBK پاکستان کا ایک تربیتی ادارہ ہے جو مدارس کے فضلا کو عملی اور آمدنی والے ڈیجیٹل ہنر سکھاتا ہے۔'),
             'about-hero.jpg', t('Scholar teaching students', 'طلبہ کو پڑھاتے ہوئے استاد'))}

  <section class="section">
    <div class="container">
      <div class="row g-5 align-items-center">
        <div class="col-lg-6" data-aos="fade-right"><h2 class="display-title">{t('Why<br>UBK Exists', 'UBK کیوں<br>قائم کیا گیا؟')}</h2></div>
        <div class="col-lg-5 offset-lg-1" data-aos="fade-left" style="font-size:.88rem">
          <p class="mb-3">{t('Thousands of madrasa graduates leave their institutions with strong character, discipline and a deep foundation in Islamic scholarship — but without the practical skills the modern economy rewards. UBK bridges that gap.', 'ہر سال ہزاروں طلبہ مضبوط کردار، نظم و ضبط اور دینی علم کی گہری بنیاد کے ساتھ مدارس سے فارغ ہوتے ہیں — لیکن ان کے پاس وہ عملی ہنر نہیں ہوتے جن کی آج کی معیشت قدر کرتی ہے۔ UBK اسی خلا کو پُر کرتا ہے۔')}</p>
          <p>{t('We provide structured, mentor-led training in digital skills that lead directly to freelance income, employment or business creation. Every programme is designed around real client work, not theory.', 'ہم ڈیجیٹل ہنر کی منظم اور مینٹر کی زیرِ نگرانی تربیت دیتے ہیں جو براہ راست فری لانس آمدنی، ملازمت یا اپنے کاروبار تک لے جاتی ہے۔ ہر پروگرام نظریے کے بجائے حقیقی کلائنٹ ورک پر مبنی ہے۔')}</p>
        </div>
      </div>
    </div>
  </section>

  {stats_band(contained=False)}

  <section class="section bg-soft">
    <div class="container">
      <div class="row g-5 align-items-start">
        <div class="col-lg-6" data-aos="fade-right"><div class="teach-media"><img src="{img('how-we-teach.jpg')}" alt="{t('Mentor teaching two students', 'دو طلبہ کو پڑھاتا ہوا استاد')}" loading="lazy"></div></div>
        <div class="col-lg-6" data-aos="fade-left">
          <h2 class="section-title mb-4">{t('How We Teach', 'ہمارا طریقۂ تدریس')}</h2>
          <div class="ubk-acc bullets">{acc}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-soft pt-0">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('On-Campus<br>Training', 'آن کیمپس<br>تربیت')}</h2>
        <div class="d-flex flex-column gap-3 align-items-lg-end" data-aos="fade-up">
          <p class="section-lead">{t('Purpose-built facilities where scholars learn, practise and collaborate on real projects.', 'جدید سہولیات جہاں طلبہ سیکھتے، مشق کرتے اور حقیقی پروجیکٹس پر مل کر کام کرتے ہیں۔')}</p>
          <div class="slider-nav"><button class="prev" aria-label="{t('Previous', 'پچھلا')}"><i class="bi bi-arrow-left"></i></button><button class="next" aria-label="{t('Next', 'اگلا')}"><i class="bi bi-arrow-right"></i></button></div>
        </div>
      </div>
      <div class="work-slider" data-aos="fade-up">{slides}</div>
    </div>
  </section>

  {cta_trio("pt-5")}
"""
    return meta, body


# ================================================================= COURSES

def courses():
    meta = (t("Skill Tracks", "کورسز"),
            t("Four practical skill tracks — Graphic Design, eCommerce, Digital Marketing and Video Editing — taught by working professionals.",
              "چار عملی کورسز — گرافک ڈیزائن، ای کامرس، ڈیجیٹل مارکیٹنگ اور ویڈیو ایڈیٹنگ — تجربہ کار ماہرین کی نگرانی میں۔"))
    body = f"""
  {page_hero(t('Skill Tracks', 'کورسز'), t('Four tracks.<br>One goal.<br><span class="text-orange">your first paid work.</span>', 'چار کورسز۔<br>ایک مقصد۔<br><span class="text-orange">آپ کی پہلی کمائی۔</span>'),
             t('Practical skills taught by working professionals — from first lesson to first invoice.', 'تجربہ کار ماہرین سے عملی ہنر سیکھیں — پہلے سبق سے پہلی کمائی تک۔'),
             'courses-hero.jpg', t('Mentor and student at a laptop', 'لیپ ٹاپ پر استاد اور طالب علم'), button=(t('Apply Now', 'ابھی اپلائی کریں'), 'apply.html'))}
  {tracks_grid(view_all=True)}
  {logos_strip(cls="pt-0")}
  {skills_section()}
  {pricing_section("pt-0")}
  {cta_trio()}
"""
    return meta, body


# ================================================================= COURSE DETAIL

COURSE_DATA = {
    "graphic-design": {
        "hero": "hero-design.jpg",
        "title": ("Graphic<br>Design", "گرافک<br>ڈیزائن"),
        "intro": ("Design logos, social posts and brand packages that clients pay for — and build a portfolio to prove it.",
                  "لوگو، سوشل میڈیا پوسٹس اور برانڈ پیکجز ڈیزائن کرنا سیکھیں جن کے لیے کلائنٹس ادائیگی کرتے ہیں — اور اس کا ثبوت پورٹ فولیو کی صورت میں بنائیں۔"),
        "suits": ("This track is for anyone who enjoys visual work — whether you have drawn since childhood or never opened a design tool. If you want to earn from creativity, this is your starting point. No prior software experience is needed; we teach every tool from scratch.",
                  "یہ کورس ہر اس شخص کے لیے ہے جسے بصری کام پسند ہے — چاہے آپ بچپن سے ڈرائنگ کرتے ہوں یا کبھی کوئی ڈیزائن ٹول نہ کھولا ہو۔ اگر آپ تخلیقی صلاحیت سے کمانا چاہتے ہیں تو یہ آپ کا نقطۂ آغاز ہے۔ کسی سافٹ ویئر کا تجربہ ضروری نہیں؛ ہم ہر ٹول شروع سے سکھاتے ہیں۔"),
        "outcome": ("By the end of the ten weeks you will design logos, build social media kits, lay out print material and assemble a complete brand guidelines document. You will leave with a portfolio of real client work and the confidence to take on paid projects independently.",
                    "دس ہفتوں کے اختتام تک آپ لوگو ڈیزائن کریں گے، سوشل میڈیا کٹس بنائیں گے، پرنٹ میٹیریل تیار کریں گے اور مکمل برانڈ گائیڈ لائنز دستاویز بنائیں گے۔ آپ حقیقی کلائنٹ ورک کے پورٹ فولیو اور خود مختار طور پر پیڈ پروجیکٹس لینے کے اعتماد کے ساتھ فارغ ہوں گے۔"),
        "cover_lead": ("Eight modules over ten weeks, moving from foundations to a complete client-ready portfolio.",
                       "دس ہفتوں میں آٹھ ماڈیولز — بنیادی اصولوں سے لے کر کلائنٹ کے لیے تیار مکمل پورٹ فولیو تک۔"),
        "modules": [
            ("01 Design Foundations — Week 1", "01 ڈیزائن کی بنیادیں — ہفتہ 1", "Colour theory, composition and layout principles applied to real design briefs.", "رنگوں کا نظریہ، ترتیب اور لے آؤٹ کے اصول، حقیقی ڈیزائن بریفس پر عملی اطلاق کے ساتھ۔"),
            ("02 Typography & Layout — Week 2", "02 ٹائپوگرافی اور لے آؤٹ — ہفتہ 2", "Choosing and pairing typefaces, hierarchy and grid systems.", "فونٹس کا انتخاب اور جوڑ، درجہ بندی اور گرڈ سسٹمز۔"),
            ("03 Logo & Identity Design — Weeks 3–4", "03 لوگو اور شناختی ڈیزائن — ہفتہ 3–4", "From sketches to vector logos and a simple identity system.", "خاکوں سے ویکٹر لوگو اور سادہ شناختی نظام تک۔"),
            ("04 Social Media Graphics — Week 5", "04 سوشل میڈیا گرافکس — ہفتہ 5", "Post templates, carousels and story designs for real brands.", "حقیقی برانڈز کے لیے پوسٹ ٹیمپلیٹس، کیروسلز اور اسٹوری ڈیزائنز۔"),
            ("05 Print & Packaging — Week 6", "05 پرنٹ اور پیکیجنگ — ہفتہ 6", "Brochures, flyers and packaging mockups for real businesses.", "حقیقی کاروباروں کے لیے بروشرز، فلائرز اور پیکیجنگ ماک اپس۔"),
            ("06 Brand Guidelines — Week 7", "06 برانڈ گائیڈ لائنز — ہفتہ 7", "Documenting colours, type and usage rules into a brand book.", "رنگ، فونٹ اور استعمال کے اصولوں کو برانڈ بک میں مرتب کرنا۔"),
            ("07 Client Project I — Week 8", "07 کلائنٹ پروجیکٹ اول — ہفتہ 8", "Your first live brief, reviewed by mentors and the client.", "آپ کا پہلا حقیقی بریف، جس کا جائزہ مینٹرز اور کلائنٹ لیں گے۔"),
            ("08 Client Project II & Portfolio — Weeks 9–10", "08 کلائنٹ پروجیکٹ دوم اور پورٹ فولیو — ہفتہ 9–10", "A second paid brief and a polished portfolio ready to share.", "دوسرا پیڈ بریف اور شیئر کرنے کے لیے تیار مکمل پورٹ فولیو۔"),
        ],
    },
    "ecommerce": {
        "hero": "hero-ecommerce.jpg",
        "title": ("eCommerce", "ای کامرس"),
        "intro": ("Source, list and sell products on local and international platforms — and make your first sale before the course ends.",
                  "مقامی اور عالمی پلیٹ فارمز پر مصنوعات تلاش کریں، لسٹ کریں اور فروخت کریں — اور کورس ختم ہونے سے پہلے اپنی پہلی سیل کریں۔"),
        "suits": ("This track is for anyone who wants to earn by selling online — whether physical products, dropshipping or digital goods. You do not need business experience; we start from product research and take you to your first real sale.",
                  "یہ کورس ہر اس شخص کے لیے ہے جو آن لائن فروخت سے کمانا چاہتا ہے — چاہے فزیکل پروڈکٹس ہوں، ڈراپ شپنگ یا ڈیجیٹل اشیاء۔ کاروباری تجربہ ضروری نہیں؛ ہم پروڈکٹ ریسرچ سے شروع کر کے آپ کو پہلی حقیقی سیل تک لے جاتے ہیں۔"),
        "outcome": ("By the end of twelve weeks you will have sourced products, set up a live store, handled customers and processed orders. You will leave with a working storefront and the skills to scale it independently.",
                    "بارہ ہفتوں کے اختتام تک آپ پروڈکٹس تلاش کر چکے ہوں گے، ایک لائیو اسٹور بنا چکے ہوں گے، گاہکوں کو سنبھال چکے ہوں گے اور آرڈرز مکمل کر چکے ہوں گے۔ آپ ایک چلتے ہوئے اسٹور اور اسے خود بڑھانے کی مہارت کے ساتھ فارغ ہوں گے۔"),
        "cover_lead": ("Eight modules over twelve weeks, from product research to a live store with real sales.",
                       "بارہ ہفتوں میں آٹھ ماڈیولز — پروڈکٹ ریسرچ سے لے کر حقیقی سیلز والے لائیو اسٹور تک۔"),
        "modules": [
            ("01 Product Research & Niches — Week 1", "01 پروڈکٹ ریسرچ اور نیش — ہفتہ 1", "Finding profitable products and validating demand before you invest.", "سرمایہ لگانے سے پہلے منافع بخش پروڈکٹس تلاش کرنا اور طلب کی تصدیق کرنا۔"),
            ("02 Sourcing & Suppliers — Week 2", "02 سورسنگ اور سپلائرز — ہفتہ 2", "Working with local and international suppliers you can trust.", "قابلِ اعتماد مقامی اور بین الاقوامی سپلائرز کے ساتھ کام کرنا۔"),
            ("03 Listing & Photography — Weeks 3–4", "03 لسٹنگ اور فوٹوگرافی — ہفتہ 3–4", "Product photos and listings that convert browsers into buyers.", "ایسی تصاویر اور لسٹنگز جو دیکھنے والوں کو خریدار بنا دیں۔"),
            ("04 Store Setup — Week 5", "04 اسٹور سیٹ اپ — ہفتہ 5", "Building a clean, trustworthy online store step by step.", "مرحلہ وار ایک صاف ستھرا اور قابلِ اعتماد آن لائن اسٹور بنانا۔"),
            ("05 Pricing & Margins — Week 6", "05 قیمت اور منافع — ہفتہ 6", "Setting prices that cover costs, compete on the market and leave you profit.", "ایسی قیمتیں طے کرنا جو اخراجات پورے کریں، مارکیٹ میں مقابلہ کریں اور منافع دیں۔"),
            ("06 Shipping & Fulfilment — Weeks 7–8", "06 شپنگ اور ڈیلیوری — ہفتہ 7–8", "Couriers, packaging and returns handled professionally.", "کوریئر، پیکیجنگ اور واپسی کا پیشہ ورانہ انتظام۔"),
            ("07 Customer Service — Week 9", "07 کسٹمر سروس — ہفتہ 9", "Messaging, reviews and building repeat customers.", "پیغامات، ریویوز اور مستقل گاہک بنانا۔"),
            ("08 Scaling & Marketing — Weeks 10–12", "08 کاروبار بڑھانا اور مارکیٹنگ — ہفتہ 10–12", "Ads, promotions and systems to grow your store.", "اشتہارات، پروموشنز اور اسٹور بڑھانے کے نظام۔"),
        ],
    },
    "digital-marketing": {
        "hero": "hero-marketing.jpg",
        "title": ("Digital<br>Marketing", "ڈیجیٹل<br>مارکیٹنگ"),
        "intro": ("Run ads, manage social pages and bring paying customers to any business — starting with real campaigns in class.",
                  "اشتہارات چلائیں، سوشل میڈیا پیجز سنبھالیں اور کسی بھی کاروبار کے لیے گاہک لائیں — کلاس ہی میں حقیقی مہمات سے آغاز کریں۔"),
        "suits": ("This track is for anyone who wants to help businesses grow online — whether you are drawn to social media, advertising or content. You do not need a marketing background; we teach every platform and strategy from the ground up.",
                  "یہ کورس ہر اس شخص کے لیے ہے جو کاروباروں کو آن لائن بڑھانے میں مدد کرنا چاہتا ہے — چاہے آپ کی دلچسپی سوشل میڈیا، اشتہارات یا کانٹینٹ میں ہو۔ مارکیٹنگ کا پس منظر ضروری نہیں؛ ہم ہر پلیٹ فارم اور حکمتِ عملی بنیاد سے سکھاتے ہیں۔"),
        "outcome": ("By the end of twelve weeks you will run paid ad campaigns, manage social media accounts, write marketing copy and read analytics. You will leave with campaign results you can show employers and clients.",
                    "بارہ ہفتوں کے اختتام تک آپ پیڈ اشتہاری مہمات چلائیں گے، سوشل میڈیا اکاؤنٹس سنبھالیں گے، مارکیٹنگ تحریریں لکھیں گے اور اینالیٹکس سمجھیں گے۔ آپ ایسے نتائج کے ساتھ فارغ ہوں گے جو آجر اور کلائنٹس کو دکھا سکیں۔"),
        "cover_lead": ("Eight modules over twelve weeks, from marketing principles to a live campaign with measurable results.",
                       "بارہ ہفتوں میں آٹھ ماڈیولز — مارکیٹنگ کے اصولوں سے لے کر قابلِ پیمائش نتائج والی لائیو مہم تک۔"),
        "modules": [
            ("01 Marketing Fundamentals — Week 1", "01 مارکیٹنگ کی بنیادیں — ہفتہ 1", "Understanding audiences, funnels and the principles behind every successful campaign.", "ناظرین، سیلز فنل اور ہر کامیاب مہم کے پیچھے اصولوں کو سمجھنا۔"),
            ("02 Social Media Management — Weeks 2–3", "02 سوشل میڈیا مینجمنٹ — ہفتہ 2–3", "Planning, posting and growing business pages consistently.", "کاروباری پیجز کی منصوبہ بندی، پوسٹنگ اور مسلسل ترقی۔"),
            ("03 Content Creation — Week 4", "03 کانٹینٹ کی تیاری — ہفتہ 4", "Writing and producing posts that people stop to read.", "ایسی پوسٹس لکھنا اور بنانا جنہیں لوگ رک کر پڑھیں۔"),
            ("04 Facebook & Instagram Ads — Weeks 5–6", "04 فیس بک اور انسٹاگرام اشتہارات — ہفتہ 5–6", "Targeting, budgets and creatives that bring customers.", "ٹارگٹنگ، بجٹ اور ایسے اشتہارات جو گاہک لائیں۔"),
            ("05 Google Ads — Weeks 7–8", "05 گوگل ایڈز — ہفتہ 7–8", "Search campaigns, keyword strategy and bidding that delivers a return on ad spend.", "سرچ مہمات، کی ورڈ حکمتِ عملی اور بِڈنگ جو اشتہاری خرچ پر منافع دے۔"),
            ("06 Email Marketing — Week 9", "06 ای میل مارکیٹنگ — ہفتہ 9", "Lists, automations and newsletters that sell.", "ای میل لسٹس، آٹومیشن اور فروخت بڑھانے والے نیوز لیٹرز۔"),
            ("07 Analytics & Reporting — Week 10", "07 اینالیٹکس اور رپورٹنگ — ہفتہ 10", "Measuring results and reporting clearly to clients.", "نتائج کی پیمائش اور کلائنٹس کو واضح رپورٹنگ۔"),
            ("08 Live Campaign Project — Weeks 11–12", "08 لائیو مہم پروجیکٹ — ہفتہ 11–12", "Plan, launch and optimise a campaign for a real business.", "ایک حقیقی کاروبار کے لیے مہم کی منصوبہ بندی، آغاز اور بہتری۔"),
        ],
    },
    "video-editing": {
        "hero": "hero-video.jpg",
        "title": ("Video<br>Editing", "ویڈیو<br>ایڈیٹنگ"),
        "intro": ("Cut, caption and colour video for creators, brands and campaigns — and deliver your first paid edit before you graduate.",
                  "کریئیٹرز، برانڈز اور مہمات کے لیے ویڈیو کاٹیں، کیپشن لگائیں اور رنگ درست کریں — اور کورس ختم ہونے سے پہلے اپنا پہلا پیڈ ایڈٹ ڈیلیور کریں۔"),
        "suits": ("This track is for anyone drawn to video — whether you watch YouTube tutorials for fun or dream of editing for a living. No prior editing experience is needed; we start with the interface and build to professional delivery.",
                  "یہ کورس ہر اس شخص کے لیے ہے جسے ویڈیو سے دلچسپی ہے — چاہے آپ شوق سے یوٹیوب ٹیوٹوریلز دیکھتے ہوں یا ایڈیٹنگ کو پیشہ بنانا چاہتے ہوں۔ ایڈیٹنگ کا تجربہ ضروری نہیں؛ ہم سافٹ ویئر کی بنیاد سے شروع کر کے پیشہ ورانہ معیار تک لے جاتے ہیں۔"),
        "outcome": ("By the end of ten weeks you will cut long-form and short-form video, mix audio, grade colour and add motion titles. You will leave with a showreel and the skills to take on paid editing work.",
                    "دس ہفتوں کے اختتام تک آپ طویل اور مختصر ویڈیوز ایڈٹ کریں گے، آڈیو مکس کریں گے، رنگ درست کریں گے اور موشن ٹائٹلز شامل کریں گے۔ آپ ایک شو ریل اور پیڈ ایڈیٹنگ کام لینے کی مہارت کے ساتھ فارغ ہوں گے۔"),
        "cover_lead": ("Eight modules over ten weeks, from timeline basics to a complete showreel of professional edits.",
                       "دس ہفتوں میں آٹھ ماڈیولز — ٹائم لائن کی بنیادوں سے لے کر پیشہ ورانہ ایڈٹس کی مکمل شو ریل تک۔"),
        "modules": [
            ("01 Editing Fundamentals — Week 1", "01 ایڈیٹنگ کی بنیادیں — ہفتہ 1", "Timeline navigation, cutting techniques and the grammar of visual storytelling.", "ٹائم لائن کا استعمال، کٹنگ کی تکنیکیں اور بصری کہانی سنانے کے اصول۔"),
            ("02 Cutting & Pacing — Week 2", "02 کٹنگ اور رفتار — ہفتہ 2", "Rhythm, b-roll and keeping viewers watching.", "ردھم، بی رول اور ناظرین کو آخر تک جوڑے رکھنا۔"),
            ("03 Audio & Sound Design — Week 3", "03 آڈیو اور ساؤنڈ ڈیزائن — ہفتہ 3", "Clean dialogue, music and sound effects.", "صاف آواز، بیک گراؤنڈ اور ساؤنڈ ایفیکٹس۔"),
            ("04 Colour Grading — Week 4", "04 کلر گریڈنگ — ہفتہ 4", "Correcting and styling footage for a professional look.", "فوٹیج کے رنگ درست کر کے پیشہ ورانہ انداز دینا۔"),
            ("05 Motion Graphics & Titles — Week 5", "05 موشن گرافکس اور ٹائٹلز — ہفتہ 5", "Lower thirds, title cards and basic motion design for professional polish.", "لوئر تھرڈز، ٹائٹل کارڈز اور بنیادی موشن ڈیزائن۔"),
            ("06 Subtitles & Captions — Week 6", "06 سب ٹائٹلز اور کیپشنز — ہفتہ 6", "Accurate, stylish captions for every platform.", "ہر پلیٹ فارم کے لیے درست اور خوبصورت کیپشنز۔"),
            ("07 Short-Form Content — Weeks 7–8", "07 مختصر ویڈیوز — ہفتہ 7–8", "Reels, Shorts and TikTok edits that perform.", "ریلز، شارٹس اور ٹک ٹاک کے لیے مؤثر ایڈٹس۔"),
            ("08 Client Project & Showreel — Weeks 9–10", "08 کلائنٹ پروجیکٹ اور شو ریل — ہفتہ 9–10", "A real client edit and your finished showreel.", "ایک حقیقی کلائنٹ ایڈٹ اور آپ کی مکمل شو ریل۔"),
        ],
    },
}


def course_detail(slug):
    d = COURSE_DATA[slug]
    name_plain = t(d["title"][0].replace("<br>", " "), d["title"][1].replace("<br>", " "))
    meta = (name_plain, t(d["intro"][0], d["intro"][1]))

    def module(i, m):
        en, ur, den, dur = m
        open_ = " open" if i in (0, 4) else ""
        return f'<div class="acc-item{open_}"><button class="acc-head">{t(en, ur)}<i class="bi bi-caret-down-fill caret"></i></button><div class="acc-body">{t(den, dur)}</div></div>'

    g1 = "".join(module(i, m) for i, m in enumerate(d["modules"][:4]))
    g2 = "".join(module(i + 4, m) for i, m in enumerate(d["modules"][4:]))
    body = f"""
  {page_hero(t('Skill Track', 'مہارت کورس'), t(*d['title']), t(*d['intro']), d['hero'], name_plain,
             button=(t('Apply Now', 'ابھی اپلائی کریں'), f'apply.html?track={slug}'))}

  <section class="section-sm">
    <div class="container">
      <h2 class="section-title mb-4" data-aos="fade-up">{t('Who This Track Suits', 'یہ کورس کس کے لیے ہے؟')}</h2>
      <div class="row g-4 two-col-text">
        <div class="col-md-6" data-aos="fade-up"><p>{t(*d['suits'])}</p></div>
        <div class="col-md-6" data-aos="fade-up" data-aos-delay="100"><p>{t(*d['outcome'])}</p></div>
      </div>
    </div>
  </section>

  {stats_band(contained=False)}

  <section class="section bg-soft modules">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t("What You'll Cover", 'آپ کیا سیکھیں گے')}</h2>
        <p class="section-lead" data-aos="fade-up">{t(*d['cover_lead'])}</p>
      </div>
      <div class="ubk-acc bullets lined group" data-single="false" data-aos="fade-up">{g1}</div>
      <div class="ubk-acc bullets lined group" data-single="false" data-aos="fade-up">{g2}</div>
    </div>
  </section>

  {logos_strip()}
  {skills_section("pt-4")}
  {work_slider("pt-0")}
  {testimonials_section()}
  {pricing_section()}
  {cta_wide("pt-0")}
"""
    return meta, body
