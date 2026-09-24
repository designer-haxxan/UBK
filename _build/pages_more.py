"""Funding, Admissions, Apply, Application received, Student work, FAQ, Contact."""

from core import t, img, page_hero, COURSES
from sections import pricing_section, skills_section, faq_cards_section, cta_wide, cta_trio


# ================================================================= FUNDING

def funding():
    meta = (t("Funding Options", "مالی سہولت"),
            t("Scholarship, sponsored or self-paid — every UBK student gets the same course, mentors and certificate.",
              "اسکالرشپ، بعد میں ادائیگی یا براہ راست فیس — ہر UBK طالب علم کو ایک جیسا کورس، مینٹرز اور سرٹیفکیٹ ملتا ہے۔"))
    dot = '<span class="dot"></span>'
    rows = [
        (t("Full course access", "مکمل کورس تک رسائی"), dot, dot, dot),
        (t("All learning material", "تمام تعلیمی مواد"), dot, dot, dot),
        (t("Live mentor sessions", "لائیو مینٹر سیشنز"), dot, dot, dot),
        (t("Real client projects", "حقیقی کلائنٹ پروجیکٹس"), dot, dot, dot),
        (t("Career guidance", "کیریئر رہنمائی"), dot, dot, dot),
        (t("Certificate on completion", "مکمل ہونے پر سرٹیفکیٹ"), dot, dot, dot),
        (t("Freelance setup support", "فری لانس سیٹ اپ سپورٹ"), dot, dot, dot),
        (t("Upfront cost", "پیشگی فیس"), t("None", "کوئی نہیں"), t("Deferred", "بعد میں"), t("Full fee", "مکمل فیس")),
        (t("Application required", "درخواست ضروری"), t("Yes", "ہاں"), t("Via employer", "آجر کے ذریعے"), t("No", "نہیں")),
        (t("Eligibility review", "اہلیت کا جائزہ"), t("Merit-based", "میرٹ پر"), t("Not required", "ضروری نہیں"), t("Not required", "ضروری نہیں")),
        (t("Start timing", "آغاز کا وقت"), t("On acceptance", "منظوری پر"), t("On employer match", "آجر ملنے پر"), t("Next intake", "اگلا بیچ")),
    ]
    trs = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
    qualify = [
        (t("Scholarship — merit-based, fully funded", "اسکالرشپ — میرٹ پر، مکمل مفت"),
         t("Open to madrasa graduates who demonstrate aptitude and commitment during the application process. You submit a short written application, attend a brief interview and complete a simple skills exercise.",
           "ان مدارس کے فضلا کے لیے جو درخواست کے مرحلے میں صلاحیت اور لگن کا مظاہرہ کریں۔ آپ ایک مختصر تحریری درخواست دیں گے، ایک مختصر انٹرویو دیں گے اور ایک آسان مہارتی مشق مکمل کریں گے۔")),
        (t("Sponsored — employer-deferred payment", "اسپانسرڈ — آجر کے ذریعے بعد میں ادائیگی"),
         t("You study now and repay the fee in small instalments once you are employed or earning from freelancing. We match you with partner employers during the course.",
           "آپ ابھی پڑھتے ہیں اور ملازمت یا فری لانسنگ سے کمائی شروع ہونے پر آسان اقساط میں فیس واپس کرتے ہیں۔ کورس کے دوران ہم آپ کو شراکت دار آجروں سے ملواتے ہیں۔")),
        (t("Self-Paid — open enrolment, no review", "سیلف پیڈ — کھلا داخلہ، کوئی جائزہ نہیں"),
         t("Anyone can enrol by paying the course fee directly. There is no eligibility review and you can start in the next intake.",
           "کوئی بھی براہ راست کورس فیس ادا کر کے داخلہ لے سکتا ہے۔ اہلیت کا کوئی جائزہ نہیں اور آپ اگلے بیچ میں شروع کر سکتے ہیں۔")),
        (t("Can I switch between options?", "کیا میں آپشن تبدیل کر سکتا ہوں؟"),
         t("Yes. If your situation changes before the intake starts, contact admissions and we will move you to the option that fits.",
           "جی ہاں۔ اگر بیچ شروع ہونے سے پہلے آپ کے حالات بدل جائیں تو داخلہ ٹیم سے رابطہ کریں، ہم آپ کو مناسب آپشن میں منتقل کر دیں گے۔")),
    ]
    acc = "".join(f'<div class="acc-item{" open" if i == 0 else ""}"><button class="acc-head">{h}<i class="bi bi-caret-down-fill caret"></i></button><div class="acc-body">{b}</div></div>' for i, (h, b) in enumerate(qualify))
    body = f"""
  {page_hero(t('Funding Options', 'مالی سہولت'), t('Three ways to start.<br>One of them costs nothing.', 'شروع کرنے کے تین طریقے۔<br>ان میں سے ایک بالکل مفت۔'),
             t('Every UBK student gets the same course, the same mentors and the same certificate — the only difference is how the fee is covered.', 'ہر UBK طالب علم کو ایک جیسا کورس، ایک جیسے مینٹرز اور ایک جیسا سرٹیفکیٹ ملتا ہے — فرق صرف فیس ادا کرنے کے طریقے کا ہے۔'),
             'funding-hero.jpg', t('Scholar advising a student', 'طالب علم کو مشورہ دیتے ہوئے استاد'))}
  {pricing_section()}

  <section class="section border-top">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Compared side by side', 'تینوں کا موازنہ')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('See exactly what each option includes and how they differ.', 'دیکھیں کہ ہر آپشن میں کیا شامل ہے اور ان میں کیا فرق ہے۔')}</p>
      </div>
      <div class="table-responsive" data-aos="fade-up">
        <table class="compare-table">
          <thead><tr><th></th><th>{t('Scholarship', 'اسکالرشپ')}</th><th>{t('Sponsored', 'اسپانسرڈ')}</th><th>{t('Self-Paid', 'سیلف پیڈ')}</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section pt-0">
    <div class="container">
      <div class="section-head mb-3">
        <h2 class="section-title" data-aos="fade-up">{t('Who qualifies', 'کون اہل ہے؟')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('Each option has different eligibility criteria. Here is what you need to know before you apply.', 'ہر آپشن کی اہلیت مختلف ہے۔ اپلائی کرنے سے پہلے یہ جان لیں۔')}</p>
      </div>
      <div class="ubk-acc bullets lined" data-aos="fade-up">{acc}</div>
    </div>
  </section>

  {faq_cards_section("bg-soft")}
  {cta_wide("pt-5")}
"""
    return meta, body


# ================================================================= ADMISSIONS

def admissions():
    meta = (t("Admissions", "داخلہ"),
            t("How to apply to UBK — five simple steps, about two weeks from application to offer.",
              "UBK میں اپلائی کرنے کا طریقہ — پانچ آسان مراحل، درخواست سے آفر تک تقریباً دو ہفتے۔"))
    steps = [
        (t("Choose your track", "اپنا کورس منتخب کریں"),
         t("Review the four skill tracks — Graphic Design, eCommerce, Digital Marketing and Video Editing — and pick the one that matches where you want your career to go.",
           "چاروں کورسز — گرافک ڈیزائن، ای کامرس، ڈیجیٹل مارکیٹنگ اور ویڈیو ایڈیٹنگ — دیکھیں اور وہ منتخب کریں جو آپ کے کیریئر کے مقصد سے میل کھاتا ہو۔")),
        (t("Fill in the application", "درخواست فارم پُر کریں"),
         t("Complete the online form. It takes about ten minutes and asks for your background, your goals and your preferred intake date.",
           "آن لائن فارم مکمل کریں۔ اس میں تقریباً دس منٹ لگتے ہیں اور آپ کا پس منظر، اہداف اور پسندیدہ بیچ پوچھا جاتا ہے۔")),
        (t("Complete the skills exercise", "مہارتی مشق مکمل کریں"),
         t("We send you a short practical exercise related to your chosen track. There is nothing to study — we want to see how you think and solve problems.",
           "ہم آپ کے منتخب کورس سے متعلق ایک مختصر عملی مشق بھیجتے ہیں۔ اس کے لیے کچھ پڑھنا ضروری نہیں — ہم صرف آپ کی سوچ اور مسئلہ حل کرنے کا انداز دیکھنا چاہتے ہیں۔")),
        (t("Attend a short interview", "مختصر انٹرویو دیں"),
         t("A fifteen-minute video call with one of our mentors. We want to understand your motivation and make sure UBK is right for you.",
           "ہمارے کسی مینٹر کے ساتھ پندرہ منٹ کی ویڈیو کال۔ ہم آپ کا جذبہ سمجھنا اور یقینی بنانا چاہتے ہیں کہ UBK آپ کے لیے درست انتخاب ہے۔")),
        (t("Receive your offer", "اپنی آفر وصول کریں"),
         t("Successful applicants get an offer within five working days. Accept it, choose your funding option and you are in.",
           "کامیاب امیدواروں کو پانچ کاروباری دنوں میں آفر مل جاتی ہے۔ اسے قبول کریں، مالی آپشن منتخب کریں اور آپ کا داخلہ ہو گیا۔")),
    ]

    def card(i, h, p, delay):
        n = f"{i + 1:02d}"
        return f'<div class="step-card" data-n="{n}" data-aos="fade-up" data-aos-delay="{delay}"><div class="n">{n}</div><h5>{h}</h5><p>{p}</p></div>'

    row1 = "".join(f'<div class="col-md-4">{card(i, h, p, i * 100)}</div>' for i, (h, p) in enumerate(steps[:3]))
    row2 = "".join(f'<div class="col-md-4">{card(i + 3, h, p, i * 100)}</div>' for i, (h, p) in enumerate(steps[3:]))
    intakes = [
        (t("Winter 2027", "سرما 2027"), t("January 6 – March 28", "6 جنوری – 28 مارچ"), t("Applications open Nov 24", "درخواستیں 24 نومبر سے")),
        (t("Spring 2027", "بہار 2027"), t("April 7 – June 27", "7 اپریل – 27 جون"), t("Applications open Feb 24", "درخواستیں 24 فروری سے")),
        (t("Summer 2027", "گرما 2027"), t("July 7 – September 26", "7 جولائی – 26 ستمبر"), t("Applications open May 26", "درخواستیں 26 مئی سے")),
        (t("Autumn 2027", "خزاں 2027"), t("October 6 – December 19", "6 اکتوبر – 19 دسمبر"), t("Applications open Aug 25", "درخواستیں 25 اگست سے")),
    ]
    trs = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{"<span class=status-dot></span>" if i == 0 else ""}{c}</td></tr>' for i, (a, b, c) in enumerate(intakes))
    body = f"""
  {page_hero(t('Admissions', 'داخلہ'), t('How to apply', 'اپلائی کرنے کا طریقہ'),
             t('The whole process takes about two weeks from application to offer.', 'درخواست سے آفر تک پورا عمل تقریباً دو ہفتے میں مکمل ہوتا ہے۔'),
             'admissions-hero.jpg', t('Mentor reviewing an application with a student', 'طالب علم کے ساتھ درخواست کا جائزہ لیتے ہوئے مینٹر'),
             button=(t('Start your application', 'درخواست شروع کریں'), 'apply.html'))}

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Five steps', 'پانچ مراحل')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('From application to offer in about two weeks. Here is exactly what happens at each stage.', 'درخواست سے آفر تک تقریباً دو ہفتے۔ ہر مرحلے پر کیا ہوتا ہے، یہاں دیکھیں۔')}</p>
      </div>
      <div class="row g-3">{row1}</div>
      <div class="row g-3 mt-0 justify-content-center">{row2}</div>
    </div>
  </section>

  {skills_section("bg-soft")}

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Intake dates', 'داخلے کی تاریخیں')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('We run four intakes each year. Applications open six weeks before each start date.', 'ہم سال میں چار بیچ شروع کرتے ہیں۔ ہر بیچ سے چھ ہفتے پہلے درخواستیں کھلتی ہیں۔')}</p>
      </div>
      <div class="table-responsive" data-aos="fade-up">
        <table class="intake-table">
          <thead><tr><th>{t('Intake', 'بیچ')}</th><th>{t('Dates', 'تاریخیں')}</th><th>{t('Status', 'صورتحال')}</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
    </div>
  </section>

  {faq_cards_section("bg-soft")}
  {cta_wide("pt-5")}
"""
    return meta, body


# ================================================================= APPLY

def apply():
    meta = (t("Apply to UBK", "UBK میں اپلائی کریں"),
            t("Apply to UBK in about ten minutes. You will hear back within five working days.",
              "تقریباً دس منٹ میں UBK میں اپلائی کریں۔ پانچ کاروباری دنوں میں جواب ملے گا۔"))
    req = t("This field is required", "یہ خانہ ضروری ہے")

    def field(name, label, ph, typ="text", hint="", required=True, msg=None):
        r = " required" if required else ""
        h = f'<div class="hint">{hint}</div>' if hint else ""
        return f"""<div class="field"><label for="{name}">{label}</label><input class="form-control" id="{name}" name="{name}" type="{typ}" placeholder="{ph}"{r}>{h}<div class="invalid-msg">{msg or req}</div></div>"""

    tracks = "".join(
        f'<label class="track-option"><input type="radio" name="track" value="{slug}" required data-on="{t("Selected", "منتخب")}" data-off="{t("Select", "منتخب کریں")}"{" checked" if i == 0 else ""}><span><strong>{t(en, ur)}</strong><small>{t("Select", "منتخب کریں")}</small></span></label>'
        for i, (slug, _, _, en, ur) in enumerate(COURSES))
    pays = "".join(
        f'<label class="pay-option"><input type="radio" name="pay" value="{v}"{" checked" if i == 0 else ""}><span>{lbl}</span></label>'
        for i, (v, lbl) in enumerate([("scholarship", t("Scholarship", "اسکالرشپ")), ("sponsored", t("Sponsored", "اسپانسرڈ")), ("self", t("Self-Paid", "سیلف پیڈ"))]))
    body = f"""
  {page_hero(t('Admissions', 'داخلہ'), t('Apply to UBK', 'UBK میں اپلائی کریں'),
             t('It takes about ten minutes to complete. You will hear back within five working days.', 'اسے مکمل کرنے میں تقریباً دس منٹ لگتے ہیں۔ پانچ کاروباری دنوں میں آپ کو جواب مل جائے گا۔'),
             'apply-hero.jpg', t('Student filling in an application', 'درخواست پُر کرتا طالب علم'),
             breadcrumb=f'<a href="index.html">{t("Home", "ہوم")}</a> / <a href="admissions.html">{t("Admissions", "داخلہ")}</a> / {t("Apply", "اپلائی")}')}

  <section class="section bg-soft">
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-4">
          <aside class="apply-aside" data-aos="fade-right">
            <h5>{t('What happens next', 'آگے کیا ہوگا')}</h5>
            <ol>
              <li>{t('We review your application within five working days.', 'ہم پانچ کاروباری دنوں میں آپ کی درخواست کا جائزہ لیتے ہیں۔')}</li>
              <li>{t('You receive an email with the outcome and next steps.', 'آپ کو نتیجے اور اگلے مراحل کے ساتھ ای میل موصول ہوگی۔')}</li>
              <li>{t('If accepted, choose your funding option and confirm your place.', 'منظوری کی صورت میں مالی آپشن منتخب کریں اور اپنی نشست کی تصدیق کریں۔')}</li>
            </ol>
            <div class="social-proof mt-4"><img class="avatars" src="{img('avatars.png')}" alt=""><div><strong>1.5k+</strong>{t('satisfied Students', 'مطمئن طلبہ')}</div></div>
            <p class="mt-3" style="font-size:.75rem">{t('Prefer WhatsApp? Message us at', 'واٹس ایپ پسند ہے؟ ہمیں پیغام بھیجیں')} <a href="https://wa.me/923000000000" class="text-blue fw-semibold" dir="ltr">+92 300 000 0000</a></p>
          </aside>
        </div>
        <div class="col-lg-8">
          <form class="form-ubk js-apply-form" action="application-received.html" novalidate data-aos="fade-up">
            <div class="group-title">{t('About you', 'آپ کے بارے میں')}</div>
            {field('full_name', t('Full name', 'پورا نام'), t('Enter your full name', 'اپنا پورا نام لکھیں'), hint=t('As it appears on your national ID', 'جیسا شناختی کارڈ پر درج ہے'))}
            {field('father_name', t("Father's name", 'والد کا نام'), t("Enter your father's name", 'والد کا نام لکھیں'))}
            {field('dob', t('Date of birth', 'تاریخِ پیدائش'), 'DD / MM / YYYY', typ='date')}
            {field('city', t('City', 'شہر'), t('Your current city', 'آپ کا موجودہ شہر'))}
            {field('phone', t('Phone number', 'فون نمبر'), '+92 3XX XXX XXXX', typ='tel', hint=t('We may call to confirm your interview slot', 'انٹرویو کا وقت طے کرنے کے لیے ہم کال کر سکتے ہیں'), msg=t('Enter a valid phone number', 'درست فون نمبر درج کریں'))}
            {field('whatsapp', t('WhatsApp number', 'واٹس ایپ نمبر'), '+92 3XX XXX XXXX', typ='tel', hint=t('If different from phone number', 'اگر فون نمبر سے مختلف ہو'), required=False)}
            {field('email', t('Email address', 'ای میل ایڈریس'), 'you@example.com', typ='email', hint=t('We will send your outcome to this address', 'نتیجہ اسی ای میل پر بھیجا جائے گا'), msg=t('Enter a valid email address', 'درست ای میل درج کریں'))}

            <div class="group-title">{t('Your background', 'آپ کا تعلیمی پس منظر')}</div>
            {field('madrasa', t('Madrasa or institution name', 'مدرسہ یا ادارے کا نام'), t('Name of your school or madrasa', 'اپنے مدرسے یا ادارے کا نام'))}
            {field('year', t('Year completed', 'فراغت کا سال'), t('e.g. 2024', 'مثلاً 2024'), typ='number')}
            <div class="field">
              <label for="level">{t('Level of computer experience', 'کمپیوٹر کا تجربہ')}</label>
              <select class="form-select" id="level" name="level" required>
                <option value="">{t('Select your level', 'اپنا درجہ منتخب کریں')}</option>
                <option>{t('None — complete beginner', 'بالکل نہیں — مکمل نیا')}</option>
                <option>{t('Basic — I can use a phone and browse the internet', 'بنیادی — موبائل اور انٹرنیٹ استعمال کر سکتا ہوں')}</option>
                <option>{t('Intermediate — I use a computer regularly', 'درمیانہ — باقاعدگی سے کمپیوٹر استعمال کرتا ہوں')}</option>
                <option>{t('Advanced — I have used design or office software', 'اچھا — ڈیزائن یا آفس سافٹ ویئر استعمال کر چکا ہوں')}</option>
              </select>
              <div class="hint">{t('Be honest — all levels are welcome', 'ایمانداری سے بتائیں — ہر درجے کا خیرمقدم ہے')}</div>
              <div class="invalid-msg">{req}</div>
            </div>
            <div class="field">
              <span class="label">{t('Do you own or have access to a laptop?', 'کیا آپ کے پاس لیپ ٹاپ ہے یا اس تک رسائی ہے؟')}</span>
              <div class="form-check"><input class="form-check-input" type="radio" name="laptop" id="lp1" value="yes" required><label class="form-check-label" for="lp1">{t('Yes', 'ہاں')}</label></div>
              <div class="form-check"><input class="form-check-input" type="radio" name="laptop" id="lp2" value="no"><label class="form-check-label" for="lp2">{t('No', 'نہیں')}</label></div>
              <div class="form-check"><input class="form-check-input" type="radio" name="laptop" id="lp3" value="arrange"><label class="form-check-label" for="lp3">{t('Not sure — I can arrange one', 'یقین نہیں — انتظام کر سکتا ہوں')}</label></div>
              <div class="hint">{t('UBK provides lab access but a personal laptop helps', 'UBK لیب کی سہولت دیتا ہے لیکن ذاتی لیپ ٹاپ مفید رہتا ہے')}</div>
              <div class="invalid-msg">{t('Please choose an option', 'براہ کرم ایک آپشن منتخب کریں')}</div>
            </div>

            <div class="field">
              <span class="label">{t('Which track', 'کون سا کورس')}</span>
              <p class="hint mb-3" style="margin-top:-4px">{t('Select the track you want to study. You can change this before the intake starts.', 'وہ کورس منتخب کریں جو آپ پڑھنا چاہتے ہیں۔ بیچ شروع ہونے سے پہلے اسے بدلا جا سکتا ہے۔')}</p>
              <div class="track-options">{tracks}</div>
            </div>

            <div class="field">
              <span class="label">{t('How you plan to pay', 'ادائیگی کا طریقہ')}</span>
              <p class="hint mb-3" style="margin-top:-4px">{t('You can explore all options on the', 'تمام آپشنز کی تفصیل')} <a href="funding.html" class="text-blue">{t('Funding page', 'مالی سہولت کے صفحے')}</a>{t('. This helps us prepare the right paperwork.', ' پر دیکھیں۔ اس سے ہمیں درست کاغذات تیار کرنے میں مدد ملتی ہے۔')}</p>
              <div class="pay-options">{pays}</div>
            </div>

            <div class="group-title mt-4">{t('Anything else', 'مزید کچھ')}</div>
            <div class="field">
              <label for="notes">{t('Is there anything else you would like us to know?', 'کیا آپ ہمیں کچھ اور بتانا چاہیں گے؟')}</label>
              <textarea class="form-control" id="notes" name="notes" rows="4" placeholder="{t('Optional — tell us about your goals, circumstances or questions', 'اختیاری — اپنے اہداف، حالات یا سوالات کے بارے میں بتائیں')}"></textarea>
              <div class="hint">{t('This field is optional', 'یہ خانہ اختیاری ہے')}</div>
            </div>
            <button type="submit" class="btn-ubk btn-orange btn-block">{t('Submit application', 'درخواست جمع کریں')}</button>
            <p class="hint mt-3">{t('By submitting this form you agree to our', 'یہ فارم جمع کرا کر آپ ہماری')} <a href="privacy-policy.html" class="text-blue">{t('Privacy Policy', 'پرائیویسی پالیسی')}</a>{t('. We will not share your information with third parties.', ' سے اتفاق کرتے ہیں۔ ہم آپ کی معلومات کسی تیسرے فریق کو نہیں دیں گے۔')}</p>
          </form>
        </div>
      </div>
    </div>
  </section>
"""
    return meta, body


# ================================================================= APPLICATION RECEIVED

def received():
    meta = (t("Application received", "درخواست موصول ہو گئی"),
            t("Thank you for applying to UBK.", "UBK میں اپلائی کرنے کا شکریہ۔"))
    steps = [
        (t("Check your email", "اپنی ای میل دیکھیں"),
         t("We send a confirmation to your inbox within the next few minutes. Check your spam folder if you do not see it.",
           "چند منٹ میں آپ کو تصدیقی ای میل ملے گی۔ اگر نظر نہ آئے تو اسپام فولڈر دیکھیں۔")),
        (t("Wait for our review", "ہمارے جائزے کا انتظار کریں"),
         t("The admissions team reviews every application within five working days. We may contact you to schedule your interview.",
           "داخلہ ٹیم پانچ کاروباری دنوں میں ہر درخواست کا جائزہ لیتی ہے۔ انٹرویو کا وقت طے کرنے کے لیے ہم آپ سے رابطہ کر سکتے ہیں۔")),
        (t("Receive your outcome", "نتیجہ وصول کریں"),
         t("We email you with the result. If accepted, you choose your funding option and confirm your place on the next intake.",
           "ہم آپ کو نتیجہ ای میل کریں گے۔ منظوری کی صورت میں آپ مالی آپشن منتخب کر کے اگلے بیچ میں اپنی نشست کی تصدیق کریں گے۔")),
    ]
    cards = "".join(f'<div class="col-md-4"><div class="step-card" data-n="{i + 1:02d}" data-aos="fade-up" data-aos-delay="{i * 120}"><div class="n">{i + 1:02d}</div><h5>{h}</h5><p>{p}</p></div></div>' for i, (h, p) in enumerate(steps))
    body = f"""
  <section class="received-hero">
    <div class="container position-relative">
      <svg class="check-anim" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="32"/><path d="M19 33l9 9 17-19"/></svg>
      <h1 class="fade-in-up d-2">{t('Application received', 'آپ کی درخواست موصول ہو گئی')}</h1>
      <p class="fade-in-up d-3">{t('Your reference number is', 'آپ کا ریفرنس نمبر ہے')} <strong class="js-ref" dir="ltr">UBK-2027-XXXXX</strong>{t('. We will review your application and email you within five working days.', '۔ ہم آپ کی درخواست کا جائزہ لے کر پانچ کاروباری دنوں میں آپ کو ای میل کریں گے۔')}</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 class="section-title text-center mb-5" data-aos="fade-up">{t('What happens next', 'آگے کیا ہوگا')}</h2>
      <div class="row g-3">{cards}</div>
    </div>
  </section>

  <section class="section-sm bg-soft">
    <div class="container d-flex justify-content-center gap-3 flex-wrap" data-aos="fade-up">
      <a href="index.html" class="btn-ubk btn-sm-ubk">{t('Back to home', 'ہوم پیج پر جائیں')}</a>
      <a href="courses.html" class="btn-ubk btn-sm-ubk">{t('Browse the tracks', 'کورسز دیکھیں')}</a>
    </div>
  </section>
"""
    return meta, body


# ================================================================= STUDENT WORK

def student_work():
    meta = (t("Student Work", "طلبہ کا کام"),
            t("Real deliverables from real client briefs — completed by UBK students during their training.",
              "حقیقی کلائنٹس کے لیے UBK طلبہ کے تیار کردہ پروجیکٹس۔"))
    cats = {"ecommerce": t("eCommerce", "ای کامرس"), "marketing": t("Digital Marketing", "ڈیجیٹل مارکیٹنگ"),
            "design": t("Graphic Design", "گرافک ڈیزائن"), "video": t("Video Editing", "ویڈیو ایڈیٹنگ")}
    items = [
        ("work-store.jpg", "ecommerce", t("Online Store Setup & Launch", "آن لائن اسٹور سیٹ اپ اور لانچ")),
        ("work-brand.jpg", "design", t("Restaurant Menu & Branding", "ریسٹورنٹ مینو اور برانڈنگ")),
        ("work-social.jpg", "marketing", t("Social Media Campaign for Café", "کیفے کے لیے سوشل میڈیا مہم")),
        ("work-brand.jpg", "video", t("Promotional Video for Gym", "جم کے لیے پروموشنل ویڈیو")),
        ("work-store.jpg", "ecommerce", t("Product Photography & Listings", "پروڈکٹ فوٹوگرافی اور لسٹنگز")),
        ("work-social.jpg", "design", t("Event Poster Series", "ایونٹ پوسٹر سیریز")),
        ("work-social.jpg", "marketing", t("Google Ads Setup for Clinic", "کلینک کے لیے گوگل ایڈز سیٹ اپ")),
        ("work-brand.jpg", "video", t("YouTube Channel Intro Pack", "یوٹیوب چینل انٹرو پیک")),
        ("work-store.jpg", "ecommerce", t("Shopify Migration & Rebrand", "شاپیفائی منتقلی اور ری برانڈ")),
        ("work-store.jpg", "design", t("Logo & Identity Package", "لوگو اور شناختی پیکج")),
        ("work-social.jpg", "marketing", t("Email Marketing Funnel", "ای میل مارکیٹنگ فنل")),
        ("work-brand.jpg", "video", t("Wedding Highlight Reel", "شادی کی ہائی لائٹ ریل")),
    ]
    grid = "".join(f"""
        <div class="col-sm-6 col-lg-4 portfolio-item" data-cat="{c}" data-aos="fade-up" data-aos-delay="{(i % 3) * 100}">
          <a class="portfolio-card" href="#"><div class="media"><img src="{img(im)}" alt="{n}" loading="lazy"></div><div class="cap"><small>{cats[c]}</small><h4>{n}</h4></div></a>
        </div>""" for i, (im, c, n) in enumerate(items))
    filters = f'<button class="filter-btn active" data-filter="all">{t("All", "سب")}</button>' + "".join(
        f'<button class="filter-btn" data-filter="{k}">{v}</button>' for k, v in [("ecommerce", cats["ecommerce"]), ("marketing", cats["marketing"]), ("design", cats["design"]), ("video", cats["video"])])
    body = f"""
  {page_hero(t('Real Client Work', 'حقیقی کلائنٹ ورک'), t('Work our students<br>delivered for paying clients.', 'ہمارے طلبہ کا وہ کام<br>جس کی کلائنٹس نے ادائیگی کی۔'),
             t('Every project below was completed by a UBK student for a real business. Browse by skill track to see what you could be delivering within weeks of enrolling.', 'نیچے دیا گیا ہر پروجیکٹ کسی UBK طالب علم نے ایک حقیقی کاروبار کے لیے مکمل کیا۔ کورس کے لحاظ سے دیکھیں کہ داخلے کے چند ہفتوں بعد آپ کیا کچھ بنا سکتے ہیں۔'),
             'work-hero.jpg', t('Student presenting design work', 'اپنا ڈیزائن پیش کرتا طالب علم'))}

  <section class="section-sm bg-soft py-4">
    <div class="container"><div class="filter-bar" data-aos="fade-up">{filters}</div></div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Student<br>Portfolio', 'طلبہ کا<br>پورٹ فولیو')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('Real deliverables from real client briefs — completed by UBK graduates during their training.', 'حقیقی کلائنٹ بریفس پر تیار شدہ کام — جو UBK طلبہ نے دورانِ تربیت مکمل کیا۔')}</p>
      </div>
      <div class="row g-3">{grid}</div>
    </div>
  </section>

  {cta_trio("pt-0")}
"""
    return meta, body


# ================================================================= FAQ

FAQ_GROUPS = [
    ("eligibility", ("Eligibility", "اہلیت"), [
        ("Who can apply to UBK?", "UBK میں کون اپلائی کر سکتا ہے؟",
         "UBK is open to madrasa graduates of any age who want to learn marketable digital skills. No prior tech experience is required.",
         "UBK ہر عمر کے ان مدارس کے فضلا کے لیے ہے جو مارکیٹ میں قابلِ قدر ڈیجیٹل ہنر سیکھنا چاہتے ہیں۔ پہلے سے ٹیکنالوجی کا تجربہ ضروری نہیں۔"),
        ("Do I need a matric or FA to be eligible?", "کیا اہلیت کے لیے میٹرک یا ایف اے ضروری ہے؟",
         "No. A madrasa qualification is enough. We assess motivation and aptitude, not school certificates.",
         "نہیں۔ مدرسے کی سند کافی ہے۔ ہم اسکول کی اسناد کے بجائے لگن اور صلاحیت دیکھتے ہیں۔"),
        ("Is there an age limit?", "کیا عمر کی کوئی حد ہے؟",
         "There is no upper age limit. Contact admissions if you are unsure whether you meet the minimum age.",
         "زیادہ سے زیادہ عمر کی کوئی حد نہیں۔ کم از کم عمر کے بارے میں شک ہو تو داخلہ ٹیم سے رابطہ کریں۔"),
        ("Can women apply?", "کیا خواتین اپلائی کر سکتی ہیں؟",
         "Yes. Contact admissions for details of class arrangements for women.",
         "جی ہاں۔ خواتین کی کلاسز کے انتظامات کی تفصیل کے لیے داخلہ ٹیم سے رابطہ کریں۔"),
    ]),
    ("money", ("Money", "فیس اور ادائیگی"), [
        ("How much does the programme cost?", "پروگرام کی فیس کتنی ہے؟",
         "Fees depend on the track. Scholarship students pay nothing; see the Funding page for current fees.",
         "فیس کورس کے لحاظ سے مختلف ہے۔ اسکالرشپ والے طلبہ کچھ ادا نہیں کرتے؛ موجودہ فیس کے لیے مالی سہولت کا صفحہ دیکھیں۔"),
        ("Are scholarships available?", "کیا اسکالرشپ دستیاب ہے؟",
         "Yes. Fully funded scholarships are awarded on merit through our application and interview process.",
         "جی ہاں۔ درخواست اور انٹرویو کے ذریعے میرٹ پر مکمل مفت اسکالرشپ دی جاتی ہے۔"),
        ("Can I pay in instalments?", "کیا فیس اقساط میں ادا ہو سکتی ہے؟",
         "Yes. Self-paid students can split the fee into monthly instalments, and sponsored students repay after they start earning.",
         "جی ہاں۔ سیلف پیڈ طلبہ ماہانہ اقساط میں فیس دے سکتے ہیں، اور اسپانسرڈ طلبہ کمائی شروع ہونے کے بعد ادائیگی کرتے ہیں۔"),
        ("Are there any hidden fees?", "کیا کوئی پوشیدہ فیس ہے؟",
         "No. The course fee covers all material, lab access, mentor sessions and your certificate.",
         "نہیں۔ کورس فیس میں تمام مواد، لیب، مینٹر سیشنز اور سرٹیفکیٹ شامل ہیں۔"),
    ]),
    ("studying", ("Studying at UBK", "UBK میں تعلیم"), [
        ("Where are classes held?", "کلاسیں کہاں ہوتی ہیں؟",
         "At the UBK campus in Lahore, with some sessions available online.",
         "لاہور میں UBK کیمپس میں، جبکہ کچھ سیشنز آن لائن بھی دستیاب ہیں۔"),
        ("What are the class timings?", "کلاس کے اوقات کیا ہیں؟",
         "Morning and evening batches run Monday to Saturday so you can study alongside other commitments.",
         "صبح اور شام کے بیچ پیر سے ہفتہ تک ہوتے ہیں تاکہ آپ دوسری مصروفیات کے ساتھ پڑھ سکیں۔"),
        ("How long is each course?", "ہر کورس کتنے عرصے کا ہے؟",
         "Between ten and twelve weeks depending on the track.",
         "کورس کے لحاظ سے دس سے بارہ ہفتے۔"),
        ("Will I work on real projects?", "کیا میں حقیقی پروجیکٹس پر کام کروں گا؟",
         "Yes. Every track includes live briefs from real businesses.",
         "جی ہاں۔ ہر کورس میں حقیقی کاروباروں کے لائیو پروجیکٹس شامل ہیں۔"),
    ]),
    ("certificates", ("Certificates", "سرٹیفکیٹ"), [
        ("Will I receive a certificate?", "کیا مجھے سرٹیفکیٹ ملے گا؟",
         "Yes, on completing attendance, projects and the final assessment.",
         "جی ہاں، حاضری، پروجیکٹس اور آخری جائزہ مکمل کرنے پر۔"),
        ("Is the certificate recognised by employers?", "کیا آجر اس سرٹیفکیٹ کو تسلیم کرتے ہیں؟",
         "Our partner employers recognise it, and your portfolio of real client work is what clients value most.",
         "ہمارے شراکت دار آجر اسے تسلیم کرتے ہیں، اور حقیقی کلائنٹ ورک پر مبنی آپ کا پورٹ فولیو سب سے زیادہ اہمیت رکھتا ہے۔"),
        ("Can I take more than one course?", "کیا میں ایک سے زیادہ کورس کر سکتا ہوں؟",
         "Yes, one after another. Many graduates combine design with marketing, for example.",
         "جی ہاں، ایک کے بعد دوسرا۔ مثلاً کئی طلبہ ڈیزائن کے ساتھ مارکیٹنگ بھی سیکھتے ہیں۔"),
        ("Do you offer industry certifications?", "کیا آپ انڈسٹری سرٹیفیکیشنز بھی کرواتے ہیں؟",
         "We prepare you for relevant platform certifications such as Google Ads and Meta Blueprint.",
         "ہم آپ کو گوگل ایڈز اور میٹا بلیو پرنٹ جیسی متعلقہ سرٹیفیکیشنز کے لیے تیار کرتے ہیں۔"),
    ]),
    ("after", ("After the Course", "کورس کے بعد"), [
        ("Will UBK help me find work?", "کیا UBK کام تلاش کرنے میں مدد کرے گا؟",
         "Yes. We connect graduates with partner employers and help with freelance profiles.",
         "جی ہاں۔ ہم فارغ التحصیل طلبہ کو شراکت دار آجروں سے ملواتے ہیں اور فری لانس پروفائل میں مدد کرتے ہیں۔"),
        ("Can I freelance after graduating?", "کیا فراغت کے بعد میں فری لانس کام کر سکتا ہوں؟",
         "Absolutely — freelance setup and your first client pitch are part of the course.",
         "بالکل — فری لانس سیٹ اپ اور پہلے کلائنٹ کو پیشکش کورس کا حصہ ہیں۔"),
        ("Do graduates stay connected?", "کیا فارغ التحصیل طلبہ رابطے میں رہتے ہیں؟",
         "Yes, through our alumni network, WhatsApp community and monthly meet-ups.",
         "جی ہاں، ہمارے الومنائی نیٹ ورک، واٹس ایپ کمیونٹی اور ماہانہ ملاقاتوں کے ذریعے۔"),
        ("What if I need more help after finishing?", "اگر کورس کے بعد مزید مدد درکار ہو تو؟",
         "Mentors stay in touch after you graduate, and our team is always a message away.",
         "فراغت کے بعد بھی مینٹرز رابطے میں رہتے ہیں، اور ہماری ٹیم ہر وقت ایک پیغام کی دوری پر ہے۔"),
    ]),
]


def faq():
    meta = (t("FAQ", "سوالات"),
            t("Everything you need to know before you apply to UBK.", "UBK میں اپلائی کرنے سے پہلے ضروری معلومات۔"))
    cats = "".join(f'<a href="#{gid}" class="{"active" if i == 0 else ""}">{t(*name)}</a>' for i, (gid, name, _) in enumerate(FAQ_GROUPS))
    groups = ""
    for gi, (gid, name, qs) in enumerate(FAQ_GROUPS):
        acc = "".join(
            f'<div class="acc-item{" open" if gi == 0 and i == 0 else ""}"><button class="acc-head">{t(q, qu)}<i class="bi bi-caret-down-fill caret"></i></button><div class="acc-body">{t(a, au)}</div></div>'
            for i, (q, qu, a, au) in enumerate(qs))
        groups += f'<div class="faq-group{" active" if gi == 0 else ""}" id="{gid}" data-aos="fade-up"><h5>{t(*name)}</h5><div class="ubk-acc bullets">{acc}</div></div>'
    body = f"""
  {page_hero(t('Questions', 'سوالات'), t('Everything you need to<br>know before you apply.', 'اپلائی کرنے سے پہلے<br>ضروری معلومات۔'),
             t('Browse by category or scroll through — if your question is not here, get in touch and we will answer it personally.', 'زمرے کے لحاظ سے دیکھیں یا نیچے اسکرول کریں — اگر آپ کا سوال یہاں نہیں تو ہم سے رابطہ کریں، ہم خود جواب دیں گے۔'),
             'campus-mentoring.jpg', t('Student talking with a scholar', 'استاد سے بات کرتا طالب علم'))}
  {faq_cards_section()}

  <section class="section pt-0">
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-4"><nav class="faq-cats">{cats}</nav></div>
        <div class="col-lg-8">{groups}</div>
      </div>
    </div>
  </section>

  {cta_trio("pt-0")}
"""
    return meta, body


# ================================================================= CONTACT

def contact():
    meta = (t("Contact", "رابطہ"),
            t("Visit the UBK campus in Lahore, call us or send a message.", "لاہور میں UBK کیمپس آئیں، کال کریں یا پیغام بھیجیں۔"))
    req = t("This field is required", "یہ خانہ ضروری ہے")
    info = [
        (t("Address", "پتا"), t("UBK Campus, Lahore, Pakistan", "UBK کیمپس، لاہور، پاکستان")),
        (t("Phone", "فون"), '<a href="tel:+923000000000" dir="ltr">+92 300 000 0000</a>'),
        (t("WhatsApp", "واٹس ایپ"), '<a href="https://wa.me/923000000000" dir="ltr">+92 300 000 0000</a>'),
        (t("Email", "ای میل"), '<a href="mailto:info@ubk.edu.pk">info@ubk.edu.pk</a>'),
        (t("Visiting Hours", "ملاقات کے اوقات"), t("Monday – Saturday, 9:00 AM – 5:00 PM", "پیر تا ہفتہ، صبح 9 بجے – شام 5 بجے")),
    ]
    rows = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in info)
    opts = "".join(f"<option>{t(en, ur)}</option>" for _, _, _, en, ur in COURSES)
    body = f"""
  {page_hero(t('Contact', 'رابطہ'), t('Come and see<br>the campus.', 'تشریف لائیں اور<br>کیمپس دیکھیں۔'),
             t('We are in Lahore and our doors are open — drop by, call ahead, or send us a message.', 'ہم لاہور میں ہیں اور ہمارے دروازے کھلے ہیں — تشریف لائیں، پہلے کال کریں یا ہمیں پیغام بھیجیں۔'),
             'contact-hero.jpg', t('Student at the UBK campus entrance', 'UBK کیمپس کے دروازے پر طالب علم'))}

  <section class="section">
    <div class="container">
      <div class="row g-5 align-items-center">
        <div class="col-lg-6" data-aos="fade-right"><table class="info-table">{rows}</table></div>
        <div class="col-lg-6" data-aos="fade-left"><div class="contact-media"><img src="{img('contact-campus.jpg')}" alt="{t('UBK campus building', 'UBK کیمپس کی عمارت')}" loading="lazy"></div></div>
      </div>
    </div>
  </section>

  <section class="section bg-soft">
    <div class="container">
      <div class="section-head mb-4">
        <h2 class="section-title" data-aos="fade-up">{t('Send Us<br>a Question', 'ہم سے<br>سوال پوچھیں')}</h2>
        <p class="section-lead" data-aos="fade-up">{t('Fill in the form below and we will reply within one working day.', 'نیچے فارم پُر کریں، ہم ایک کاروباری دن میں جواب دیں گے۔')}</p>
      </div>
      <form class="form-ubk js-contact-form" novalidate data-success="{t('Thank you! Your message has been sent.', 'شکریہ! آپ کا پیغام بھیج دیا گیا ہے۔')}" data-aos="fade-up">
        <div class="row g-3">
          <div class="col-md-6 field"><label for="c_name">{t('Full Name', 'پورا نام')}</label><input class="form-control" id="c_name" name="name" placeholder="{t('Enter your full name', 'اپنا پورا نام لکھیں')}" required><div class="invalid-msg">{req}</div></div>
          <div class="col-md-6 field"><label for="c_phone">{t('Phone Number', 'فون نمبر')}</label><input class="form-control" id="c_phone" name="phone" type="tel" placeholder="+92 3XX XXX XXXX" required><div class="invalid-msg">{t('Enter a valid phone number', 'درست فون نمبر درج کریں')}</div></div>
          <div class="col-md-6 field"><label for="c_email">{t('Email Address', 'ای میل ایڈریس')}</label><input class="form-control" id="c_email" name="email" type="email" placeholder="you@example.com" required><div class="invalid-msg">{t('Enter a valid email address', 'درست ای میل درج کریں')}</div></div>
          <div class="col-md-6 field"><label for="c_track">{t('Which track interests you?', 'آپ کس کورس میں دلچسپی رکھتے ہیں؟')}</label><select class="form-select" id="c_track" name="track"><option value="">{t('Select a track', 'کورس منتخب کریں')}</option>{opts}<option>{t('Not sure yet', 'ابھی طے نہیں کیا')}</option></select></div>
          <div class="col-12 field"><label for="c_msg">{t('Your Question', 'آپ کا سوال')}</label><textarea class="form-control" id="c_msg" name="message" rows="4" placeholder="{t('Tell us about yourself...', 'اپنے بارے میں بتائیں...')}" required></textarea><div class="invalid-msg">{req}</div></div>
          <div class="col-12"><button type="submit" class="btn-ubk btn-orange btn-sm-ubk">{t('Send Message', 'پیغام بھیجیں')}</button></div>
        </div>
      </form>
    </div>
  </section>

  {cta_trio("pt-5")}
"""
    return meta, body
