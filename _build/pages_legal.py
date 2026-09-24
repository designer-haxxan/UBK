"""Privacy Policy and Terms & Conditions."""

from core import t, page_hero


def _legal(sections):
    out = ""
    for head, paras in sections:
        out += f"<h2>{head}</h2>" + "".join(f"<p>{p}</p>" for p in paras)
    return f'<section class="section"><div class="container"><article class="legal" data-aos="fade-up">{out}</article></div></section>'


def privacy():
    meta = (t("Privacy Policy", "پرائیویسی پالیسی"),
            t("How UBK collects, uses and protects your personal information.", "UBK آپ کی ذاتی معلومات کیسے جمع، استعمال اور محفوظ کرتا ہے۔"))
    email = '<a href="mailto:info@ubk.edu.pk">info@ubk.edu.pk</a>'
    s = [
        (t("1. Introduction", "1۔ تعارف"), [
            t('Ummah Bridge for Knowledge ("UBK", "we", "us") is committed to protecting your personal information. This Privacy Policy explains what data we collect, how we use it, and your rights regarding that data.',
              'اُمّہ برج فار نالج ("UBK"، "ہم") آپ کی ذاتی معلومات کے تحفظ کے لیے پُرعزم ہے۔ یہ پرائیویسی پالیسی بتاتی ہے کہ ہم کون سا ڈیٹا جمع کرتے ہیں، اسے کیسے استعمال کرتے ہیں اور اس کے بارے میں آپ کے حقوق کیا ہیں۔'),
            t("By using our website or submitting an application, you agree to the practices described in this policy.",
              "ہماری ویب سائٹ استعمال کر کے یا درخواست جمع کرا کر آپ اس پالیسی میں بیان کردہ طریقوں سے اتفاق کرتے ہیں۔")]),
        (t("2. Information We Collect", "2۔ ہم کون سی معلومات جمع کرتے ہیں"), [
            t("We collect personal information that you provide directly to us, including your full name, phone number, email address, date of birth, and educational background when you apply or submit a contact form.",
              "جب آپ اپلائی کرتے ہیں یا رابطہ فارم جمع کراتے ہیں تو ہم وہ معلومات جمع کرتے ہیں جو آپ خود فراہم کرتے ہیں، جیسے پورا نام، فون نمبر، ای میل، تاریخِ پیدائش اور تعلیمی پس منظر۔"),
            t("We also collect technical data automatically, such as your browser type, device, IP address, and pages visited, through standard server logs.",
              "ہم معیاری سرور لاگز کے ذریعے کچھ تکنیکی معلومات خود بخود بھی جمع کرتے ہیں، جیسے براؤزر کی قسم، ڈیوائس، آئی پی ایڈریس اور دیکھے گئے صفحات۔")]),
        (t("3. How We Use Your Information", "3۔ ہم آپ کی معلومات کیسے استعمال کرتے ہیں"), [
            t("We use your personal information to process applications, communicate with you about your enrolment, and provide course materials and support during your training.",
              "ہم آپ کی معلومات درخواستوں پر کارروائی، داخلے کے بارے میں رابطے، اور دورانِ تربیت کورس مواد اور معاونت فراہم کرنے کے لیے استعمال کرتے ہیں۔"),
            t("We may also use aggregated, non-identifying data to improve our website and programmes.",
              "ہم اپنی ویب سائٹ اور پروگراموں کی بہتری کے لیے مجموعی اور شناخت سے پاک ڈیٹا بھی استعمال کر سکتے ہیں۔")]),
        (t("4. Sharing Your Information", "4۔ معلومات کا اشتراک"), [
            t("We do not sell, rent, or trade your personal data to third parties. We may share information with scholarship sponsors solely to confirm your enrolment status, and only with your prior consent.",
              "ہم آپ کا ذاتی ڈیٹا کسی تیسرے فریق کو فروخت، کرائے پر یا تبادلے میں نہیں دیتے۔ اسکالرشپ اسپانسرز کے ساتھ صرف آپ کے داخلے کی تصدیق کے لیے، اور صرف آپ کی پیشگی اجازت سے، معلومات شیئر کی جا سکتی ہیں۔")]),
        (t("5. Data Security", "5۔ ڈیٹا کا تحفظ"), [
            t("We take reasonable measures to protect your information from unauthorised access, alteration, or disclosure. However, no method of transmission over the internet is entirely secure, and we cannot guarantee absolute security.",
              "ہم آپ کی معلومات کو غیر مجاز رسائی، تبدیلی یا افشا سے بچانے کے لیے مناسب اقدامات کرتے ہیں۔ تاہم انٹرنیٹ پر ترسیل کا کوئی طریقہ مکمل طور پر محفوظ نہیں، اس لیے ہم مطلق تحفظ کی ضمانت نہیں دے سکتے۔")]),
        (t("6. Your Rights", "6۔ آپ کے حقوق"), [
            t(f"You may request access to, correction of, or deletion of your personal data at any time by contacting us at {email}. We will respond to your request within thirty working days.",
              f"آپ کسی بھی وقت {email} پر رابطہ کر کے اپنے ذاتی ڈیٹا تک رسائی، اس کی درستی یا حذف کرنے کی درخواست کر سکتے ہیں۔ ہم تیس کاروباری دنوں میں جواب دیں گے۔")]),
        (t("7. Cookies", "7۔ کوکیز"), [
            t("Our website uses essential cookies to ensure basic functionality. We do not use advertising or tracking cookies. You may disable cookies in your browser settings, though some features may not work as intended.",
              "ہماری ویب سائٹ بنیادی کارکردگی کے لیے ضروری کوکیز استعمال کرتی ہے۔ ہم اشتہاری یا ٹریکنگ کوکیز استعمال نہیں کرتے۔ آپ براؤزر کی سیٹنگز میں کوکیز بند کر سکتے ہیں، البتہ کچھ فیچرز متاثر ہو سکتے ہیں۔")]),
        (t("8. Changes to This Policy", "8۔ پالیسی میں تبدیلیاں"), [
            t('We may update this Privacy Policy from time to time. Any changes will be posted on this page with a revised "Last updated" date. Continued use of our website after changes constitutes acceptance of the updated policy.',
              'ہم وقتاً فوقتاً اس پالیسی میں ترمیم کر سکتے ہیں۔ تمام تبدیلیاں نئی "آخری تازہ کاری" کی تاریخ کے ساتھ اسی صفحے پر شائع ہوں گی۔ تبدیلی کے بعد ویب سائٹ کا استعمال جاری رکھنا نئی پالیسی کی قبولیت سمجھا جائے گا۔')]),
        (t("9. Contact", "9۔ رابطہ"), [
            t(f"If you have any questions about this Privacy Policy, please contact us at {email} or visit our campus in Lahore.",
              f"اس پالیسی کے بارے میں کسی بھی سوال کے لیے {email} پر رابطہ کریں یا لاہور میں ہمارے کیمپس تشریف لائیں۔")]),
    ]
    body = page_hero(t("Legal", "قانونی"), t("Privacy Policy", "پرائیویسی پالیسی"), t("Last updated: 1 August 2026", "آخری تازہ کاری: 1 اگست 2026"),
                     "privacy-hero.jpg", t("Student at a laptop", "لیپ ٹاپ پر طالب علم")) + _legal(s)
    return meta, body


def terms():
    meta = (t("Terms and Conditions", "شرائط و ضوابط"),
            t("The terms that apply when you use the UBK website or enrol in a UBK programme.", "UBK ویب سائٹ کے استعمال اور پروگرام میں داخلے کی شرائط۔"))
    s = [
        (t("1. Acceptance of Terms", "1۔ شرائط کی قبولیت"), [
            t("By accessing the UBK website or submitting an application, you agree to be bound by these Terms and Conditions. If you do not agree, please do not use our services.",
              "UBK ویب سائٹ استعمال کر کے یا درخواست جمع کرا کر آپ ان شرائط و ضوابط کے پابند ہونے سے اتفاق کرتے ہیں۔ اگر آپ متفق نہیں تو براہ کرم ہماری خدمات استعمال نہ کریں۔")]),
        (t("2. Eligibility", "2۔ اہلیت"), [
            t("UBK programmes are open to madrasa graduates of any age. Applicants must provide accurate personal information during the application process. UBK reserves the right to withdraw an offer if submitted information is found to be false.",
              "UBK کے پروگرام ہر عمر کے مدارس کے فضلا کے لیے ہیں۔ امیدواروں کو درخواست میں درست معلومات فراہم کرنا ہوں گی۔ غلط معلومات ثابت ہونے پر UBK آفر واپس لینے کا حق رکھتا ہے۔")]),
        (t("3. Enrolment and Fees", "3۔ داخلہ اور فیس"), [
            t("Enrolment is confirmed only after your application has been accepted and any applicable fees have been paid or a scholarship has been approved. Fee structures are published on the Funding page and may be updated between intakes.",
              "داخلہ صرف اس وقت کنفرم ہوتا ہے جب آپ کی درخواست منظور ہو جائے اور متعلقہ فیس ادا ہو جائے یا اسکالرشپ منظور ہو جائے۔ فیس کا ڈھانچہ مالی سہولت کے صفحے پر موجود ہے اور بیچز کے درمیان تبدیل ہو سکتا ہے۔"),
            t("Instalment plans, where offered, must be honoured on the agreed schedule. Failure to pay may result in suspension from the programme.",
              "جہاں اقساط کی سہولت دی جائے، وہاں طے شدہ شیڈول کی پابندی ضروری ہے۔ ادائیگی نہ ہونے پر پروگرام سے معطلی ہو سکتی ہے۔")]),
        (t("4. Attendance and Conduct", "4۔ حاضری اور طرزِ عمل"), [
            t("Students are expected to attend all scheduled sessions. Repeated absence without notice may lead to removal from the programme. All students must treat staff, instructors, and fellow students with respect.",
              "طلبہ سے تمام طے شدہ سیشنز میں حاضری کی توقع ہے۔ بغیر اطلاع بار بار غیر حاضری پر پروگرام سے اخراج ہو سکتا ہے۔ تمام طلبہ پر عملے، اساتذہ اور ساتھی طلبہ کا احترام لازم ہے۔"),
            t("UBK reserves the right to dismiss any student whose conduct disrupts the learning environment.",
              "UBK کسی بھی ایسے طالب علم کو خارج کرنے کا حق رکھتا ہے جس کا رویہ تعلیمی ماحول میں خلل ڈالے۔")]),
        (t("5. Intellectual Property", "5۔ دانشورانہ ملکیت"), [
            t("All course materials, including slides, exercises, templates, and recordings, are the intellectual property of UBK and may not be copied, distributed, or resold without written permission.",
              "تمام کورس مواد، بشمول سلائیڈز، مشقیں، ٹیمپلیٹس اور ریکارڈنگز، UBK کی دانشورانہ ملکیت ہیں اور تحریری اجازت کے بغیر نقل، تقسیم یا فروخت نہیں کیے جا سکتے۔"),
            t("Work you produce during the programme as part of client projects remains yours, though UBK may feature anonymised examples in its portfolio with your consent.",
              "پروگرام کے دوران کلائنٹ پروجیکٹس میں آپ کا تیار کردہ کام آپ کا ہی رہے گا، البتہ آپ کی اجازت سے UBK اس کی گمنام مثالیں اپنے پورٹ فولیو میں دکھا سکتا ہے۔")]),
        (t("6. Certificates", "6۔ سرٹیفکیٹس"), [
            t("Certificates of completion are issued to students who fulfil all programme requirements, including attendance, project submission, and assessment criteria. UBK certificates are issued by UBK alone and do not represent accreditation by any government body.",
              "تکمیل کا سرٹیفکیٹ ان طلبہ کو دیا جاتا ہے جو حاضری، پروجیکٹ جمع کرانے اور جائزے سمیت تمام تقاضے پورے کریں۔ یہ سرٹیفکیٹ صرف UBK جاری کرتا ہے اور کسی سرکاری ادارے کی منظوری کی نمائندگی نہیں کرتا۔")]),
        (t("7. Limitation of Liability", "7۔ ذمہ داری کی حد"), [
            t("UBK provides training and career guidance in good faith but does not guarantee employment, freelance income, or any specific outcome after graduation. Individual results depend on effort, market conditions, and other factors outside our control.",
              "UBK نیک نیتی سے تربیت اور کیریئر رہنمائی فراہم کرتا ہے لیکن فراغت کے بعد ملازمت، فری لانس آمدنی یا کسی مخصوص نتیجے کی ضمانت نہیں دیتا۔ انفرادی نتائج محنت، مارکیٹ کے حالات اور ہمارے اختیار سے باہر دیگر عوامل پر منحصر ہیں۔")]),
        (t("8. Changes to Terms", "8۔ شرائط میں تبدیلی"), [
            t("We may revise these Terms and Conditions from time to time. The current version will always be available on this page. Continued participation in any UBK programme after changes are posted constitutes acceptance of the revised terms.",
              "ہم وقتاً فوقتاً ان شرائط میں ترمیم کر سکتے ہیں۔ موجودہ ورژن ہمیشہ اسی صفحے پر دستیاب ہوگا۔ تبدیلیاں شائع ہونے کے بعد پروگرام میں شرکت جاری رکھنا نئی شرائط کی قبولیت سمجھا جائے گا۔")]),
        (t("9. Governing Law", "9۔ نافذ العمل قانون"), [
            t("These Terms and Conditions are governed by the laws of Pakistan. Any disputes will be subject to the jurisdiction of the courts of Lahore.",
              "یہ شرائط و ضوابط پاکستان کے قوانین کے تابع ہیں۔ کسی بھی تنازع کی صورت میں لاہور کی عدالتوں کا دائرہ اختیار ہوگا۔")]),
    ]
    body = page_hero(t("Legal", "قانونی"), t("Terms and<br>Conditions", "شرائط و<br>ضوابط"), t("Last updated: 1 August 2026", "آخری تازہ کاری: 1 اگست 2026"),
                     "hero-design.jpg", t("Student at a workstation", "ورک اسٹیشن پر طالب علم")) + _legal(s)
    return meta, body
