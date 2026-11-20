"""Team members: cards on the About page with a full-profile modal."""

from core import t, img

TEAM = [
    {
        "id": "mudassar-arif",
        "photo": "team-mudassar-arif.jpg",
        "name": ("Mudassar Arif", "مدثر عارف"),
        "role": ("Manager – Skill Development System", "مینیجر – اسکل ڈویلپمنٹ سسٹم"),
        "short": ("10+ years in administration, operations and program management.",
                  "انتظامیہ، آپریشنز اور پروگرام مینجمنٹ میں 10 سال سے زائد کا تجربہ۔"),
        "bio": [
            ("Mudassar Arif is an experienced education and program management professional with over 10 years of experience in administration, operations, and program management.",
             "مدثر عارف تعلیم اور پروگرام مینجمنٹ کے تجربہ کار ماہر ہیں، جنہیں انتظامیہ، آپریشنز اور پروگرام مینجمنٹ میں 10 سال سے زائد کا تجربہ حاصل ہے۔"),
            ("Currently serving as Manager of the Skill Development System at UBK College of Advanced Studies Jhang, he is responsible for managing and coordinating skill development initiatives, overseeing training programs, and promoting practical learning opportunities for students and young professionals.",
             "اس وقت وہ UBK کالج آف ایڈوانسڈ اسٹڈیز جھنگ میں اسکل ڈویلپمنٹ سسٹم کے مینیجر کی حیثیت سے خدمات انجام دے رہے ہیں۔ وہ مہارت سازی کے منصوبوں کے انتظام و رابطہ، تربیتی پروگراموں کی نگرانی، اور طلبہ و نوجوان پیشہ ور افراد کے لیے عملی سیکھنے کے مواقع کے فروغ کے ذمہ دار ہیں۔"),
            ("With a Master's degree and a strong background in institutional administration and program coordination, he is committed to bridging the gap between education and employment through market-oriented skills, professional training, and capacity-building initiatives.",
             "ماسٹرز ڈگری اور ادارہ جاتی انتظامیہ و پروگرام کوآرڈینیشن کے مضبوط پس منظر کے ساتھ، وہ مارکیٹ کے مطابق مہارتوں، پیشہ ورانہ تربیت اور استعداد سازی کے ذریعے تعلیم اور روزگار کے درمیان فاصلہ کم کرنے کے لیے پُرعزم ہیں۔"),
            ("His vision is to empower individuals with practical knowledge, professional competencies, and digital skills, enabling them to become confident, skilled, and productive members of society.",
             "ان کا وژن افراد کو عملی علم، پیشہ ورانہ صلاحیتوں اور ڈیجیٹل مہارتوں سے آراستہ کرنا ہے، تاکہ وہ معاشرے کے پُراعتماد، ہنرمند اور مفید رکن بن سکیں۔"),
        ],
        "facts": [
            (("Institution", "ادارہ"), ("UBK College of Advanced Studies Jhang", "UBK کالج آف ایڈوانسڈ اسٹڈیز جھنگ")),
            (("Experience", "تجربہ"), ("10+ years", "10+ سال")),
            (("Qualification", "تعلیم"), ("Master's Degree", "ماسٹرز ڈگری")),
            (("Expertise", "مہارت"), ("Administration, Operations Management, Program Management, Skill Development & Training Coordination",
                                      "انتظامیہ، آپریشنز مینجمنٹ، پروگرام مینجمنٹ، مہارت سازی اور تربیتی کوآرڈینیشن")),
        ],
    },
    {
        "id": "qaswar-hayat",
        "photo": "team-qaswar-hayat.jpg",
        "name": ("Mr. Qaswar Hayat", "جناب قسور حیات"),
        "role": ("Trainer – Digital Marketing, E-commerce & AI", "ٹرینر – ڈیجیٹل مارکیٹنگ، ای کامرس اور اے آئی"),
        "short": ("Founder & Director of AI Commerce Mastery, 5+ years across local and international markets.",
                  "اے آئی کامرس ماسٹری کے بانی و ڈائریکٹر، مقامی اور عالمی مارکیٹس میں 5 سال سے زائد کا تجربہ۔"),
        "bio": [
            ("Mr. Qaswar Hayat is a trainer and business growth consultant with over five years of experience in digital marketing, e-commerce, and business operations across local and international markets. He is the Founder and Director of AI Commerce Mastery (ACM), a training initiative focused on the practical use of digital marketing, e-commerce, and artificial intelligence.",
             "جناب قسور حیات ٹرینر اور بزنس گروتھ کنسلٹنٹ ہیں، جنہیں مقامی اور بین الاقوامی مارکیٹس میں ڈیجیٹل مارکیٹنگ، ای کامرس اور کاروباری آپریشنز کا پانچ سال سے زائد تجربہ حاصل ہے۔ وہ اے آئی کامرس ماسٹری (ACM) کے بانی و ڈائریکٹر ہیں، جو ڈیجیٹل مارکیٹنگ، ای کامرس اور مصنوعی ذہانت کے عملی استعمال پر مرکوز ایک تربیتی منصوبہ ہے۔"),
            ("As a trainer in the IT Department at UBK College of Advanced Studies Jhang, he uses case studies and hands-on projects to teach students how to plan digital campaigns, manage online business operations, and automate routine tasks with AI. He draws on his experience as Founder and Operations Director of Organic Hub, where he led retail and online operations from 2018 to 2024.",
             "UBK کالج آف ایڈوانسڈ اسٹڈیز جھنگ کے آئی ٹی ڈیپارٹمنٹ میں بطور ٹرینر، وہ کیس اسٹڈیز اور عملی پروجیکٹس کے ذریعے طلبہ کو ڈیجیٹل مہمات کی منصوبہ بندی، آن لائن کاروبار کے انتظام اور اے آئی کے ذریعے روزمرہ کاموں کو خودکار بنانا سکھاتے ہیں۔ اس میں ان کا وہ تجربہ شامل ہے جو انہوں نے آرگینک ہب کے بانی اور آپریشنز ڈائریکٹر کے طور پر 2018 سے 2024 تک ریٹیل اور آن لائن آپریشنز کی قیادت کرتے ہوئے حاصل کیا۔"),
            ("He holds an MA in Islamiyat and Arabic and has completed Dars-e-Nizami. He studied Software Engineering at Standard University and received training in Digital Skills from As-Sa'adah International Academy and in E-commerce and Global Digital Marketing from Bright Future Italy. His goal is to help students build practical skills they can use in employment, freelancing, and entrepreneurship.",
             "انہوں نے اسلامیات اور عربی میں ایم اے کیا ہے اور درسِ نظامی مکمل کیا ہے۔ انہوں نے اسٹینڈرڈ یونیورسٹی سے سافٹ ویئر انجینئرنگ کی تعلیم حاصل کی، السعادہ انٹرنیشنل اکیڈمی سے ڈیجیٹل اسکلز اور برائٹ فیوچر اٹلی سے ای کامرس اور گلوبل ڈیجیٹل مارکیٹنگ کی تربیت لی۔ ان کا مقصد طلبہ کو ایسی عملی مہارتیں سکھانا ہے جنہیں وہ ملازمت، فری لانسنگ اور کاروبار میں استعمال کر سکیں۔"),
        ],
        "facts": [
            (("Department", "شعبہ"), ("IT Department, Skill Development System", "آئی ٹی ڈیپارٹمنٹ، اسکل ڈویلپمنٹ سسٹم")),
            (("Institution", "ادارہ"), ("UBK College of Advanced Studies Jhang", "UBK کالج آف ایڈوانسڈ اسٹڈیز جھنگ")),
            (("Experience", "تجربہ"), ("5+ years across local and international markets", "مقامی اور بین الاقوامی مارکیٹس میں 5+ سال")),
            (("Professional Roles", "پیشہ ورانہ ذمہ داریاں"), ("Business Growth Consultant and Founder & Director of AI Commerce Mastery (ACM)",
                                                             "بزنس گروتھ کنسلٹنٹ، اور اے آئی کامرس ماسٹری (ACM) کے بانی و ڈائریکٹر")),
            (("Qualifications", "تعلیم"), ("MA in Islamiyat and Arabic, Dars-e-Nizami, and Software Engineering studies at Standard University",
                                           "ایم اے اسلامیات و عربی، درسِ نظامی، اور اسٹینڈرڈ یونیورسٹی سے سافٹ ویئر انجینئرنگ کی تعلیم")),
            (("Professional Training", "پیشہ ورانہ تربیت"), ("Digital Skills, As-Sa'adah International Academy. E-commerce and Global Digital Marketing, Bright Future Italy.",
                                                            "ڈیجیٹل اسکلز، السعادہ انٹرنیشنل اکیڈمی۔ ای کامرس اور گلوبل ڈیجیٹل مارکیٹنگ، برائٹ فیوچر اٹلی۔")),
            (("Expertise", "مہارت"), ("Digital Marketing, Local and Global E-commerce, AI Automation, Business Growth, and Brand Development",
                                      "ڈیجیٹل مارکیٹنگ، مقامی و عالمی ای کامرس، اے آئی آٹومیشن، بزنس گروتھ اور برانڈ ڈویلپمنٹ")),
        ],
    },
    {
        # Profile text still to come — the bio supplied was a copy of Qaswar Hayat's.
        "id": "hamza",
        "photo": "team-hamza.jpg",
        "name": ("Mr. Hamza", "جناب حمزہ"),
        "role": ("Trainer – Skill Development System", "ٹرینر – اسکل ڈویلپمنٹ سسٹم"),
        "short": ("UBK College of Advanced Studies Jhang", "UBK کالج آف ایڈوانسڈ اسٹڈیز جھنگ"),
        "bio": [],
        "facts": [],
    },
]


def _modal(m):
    paras = "".join(f"<p>{t(en, ur)}</p>" for en, ur in m["bio"])
    facts = "".join(f"<tr><th>{t(*k)}</th><td>{t(*v)}</td></tr>" for k, v in m["facts"])
    table = f'<h6 class="mt-4">{t("Professional Information", "پیشہ ورانہ معلومات")}</h6><table class="team-facts">{facts}</table>' if facts else ""
    return f"""
  <div class="modal fade team-modal" id="team-{m['id']}" tabindex="-1" aria-labelledby="team-{m['id']}-title" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="{t('Close', 'بند کریں')}"></button>
        <div class="row g-0">
          <div class="col-md-4"><img class="team-modal-photo" src="{img(m['photo'])}" alt="{t(*m['name'])}"></div>
          <div class="col-md-8"><div class="modal-body">
            <span class="eyebrow">{t('Our Team', 'ہماری ٹیم')}</span>
            <h3 id="team-{m['id']}-title">{t(*m['name'])}</h3>
            <p class="team-role">{t(*m['role'])}</p>
            <div class="team-bio">{paras}</div>
            {table}
          </div></div>
        </div>
      </div>
    </div>
  </div>"""


def team_section(cls=""):
    cards, modals = "", ""
    for i, m in enumerate(TEAM):
        has_profile = bool(m["bio"])
        btn = (f'<button class="btn-ubk btn-sm-ubk" data-bs-toggle="modal" data-bs-target="#team-{m["id"]}">{t("View profile", "پروفائل دیکھیں")} <i class="bi bi-arrow-right"></i></button>'
               if has_profile else "")
        cards += f"""
        <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="{i * 120}">
          <article class="team-card">
            <div class="team-photo"><img src="{img(m['photo'])}" alt="{t(*m['name'])}" loading="lazy"></div>
            <div class="team-body">
              <h3>{t(*m['name'])}</h3>
              <p class="team-role">{t(*m['role'])}</p>
              <p class="team-short">{t(*m['short'])}</p>
              {btn}
            </div>
          </article>
        </div>"""
        if has_profile:
            modals += _modal(m)
    return f"""
  <section class="section {cls}" id="team">
    <div class="container">
      <div class="section-head">
        <h2 class="section-title" data-aos="fade-up">{t('Meet the<br>Team', 'ہماری<br>ٹیم')}</h2>
        <p class="section-lead" data-aos="fade-up" data-aos-delay="100">{t('The people who run the Skill Development System and train our scholars every day.', 'وہ افراد جو اسکل ڈویلپمنٹ سسٹم چلاتے ہیں اور روزانہ ہمارے طلبہ کو تربیت دیتے ہیں۔')}</p>
      </div>
      <div class="row g-4 justify-content-center">{cards}</div>
    </div>
  </section>
  {modals}
"""
