"""Shared state, layout (head / header / footer) for the UBK static site generator.

Every piece of copy is written as t("English", "اردو") so both language
versions stay side by side. build.py renders each page once per language.
"""

STATE = {"lang": "en", "page": "index.html"}


def t(en, ur):
    return ur if STATE["lang"] == "ur" else en


def is_ur():
    return STATE["lang"] == "ur"


def asset(path):
    """Path to a file under /assets, relative to the current language folder."""
    return ("../" if is_ur() else "") + "assets/" + path


def img(name):
    return asset("images/" + name)


def link(page):
    return page


# ---------------------------------------------------------------- navigation

COURSES = [
    # slug, file, icon, EN, UR
    ("graphic-design", "graphic-design.html", "bi-palette", "Graphic Design", "گرافک ڈیزائن"),
    ("ecommerce", "ecommerce.html", "bi-bag-check", "eCommerce", "ای کامرس"),
    ("digital-marketing", "digital-marketing.html", "bi-megaphone", "Digital Marketing", "ڈیجیٹل مارکیٹنگ"),
    ("video-editing", "video-editing.html", "bi-camera-reels", "Video Editing", "ویڈیو ایڈیٹنگ"),
]

COURSE_FILES = [c[1] for c in COURSES]


def nav_active(key):
    page = STATE["page"]
    groups = {
        "home": ["index.html"],
        "about": ["about.html"],
        "courses": ["courses.html"] + COURSE_FILES,
        "funding": ["funding.html"],
        "admissions": ["admissions.html", "apply.html", "application-received.html"],
    }
    return " active" if page in groups.get(key, []) else ""


LOGO_SVG = """<svg viewBox="0 0 64 44" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M32 2 2 15l30 13 30-13L32 2Z" fill="currentColor"/><path d="M13 21v12c0 5 8.5 9 19 9s19-4 19-9V21l-19 8.3L13 21Z" fill="currentColor"/><path d="M58 17v14" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><circle cx="58" cy="33" r="2.6" fill="currentColor"/></svg>"""


def brand(on_dark=False):
    color = "#fff" if on_dark else "#1b2596"
    cls = "brand on-dark" if on_dark else "brand"
    return f"""<a class="{cls}" href="{link('index.html')}" aria-label="UBK home">
      <span style="color:{color}">{LOGO_SVG}</span>
      <span class="brand-text"><strong>UBK</strong><small>Skill Development Systems</small></span>
    </a>"""


def head(title, description):
    rtl = is_ur()
    bs_css = "bootstrap.rtl.min.css" if rtl else "bootstrap.min.css"
    lang = "ur" if rtl else "en"
    direction = "rtl" if rtl else "ltr"
    fonts = (
        "https://fonts.googleapis.com/css2?family=Baloo+Bhaijaan+2:wght@500;600;700;800"
        "&family=Noto+Naskh+Arabic:wght@400;500;600;700&family=Inter:wght@400;500;600;700"
        "&family=Schibsted+Grotesk:wght@500;600;700;800&display=swap"
        if rtl else
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700"
        "&family=Schibsted+Grotesk:wght@500;600;700;800&family=Noto+Naskh+Arabic:wght@500&display=swap"
    )
    full_title = f"{title} | UBK" if STATE["page"] != "index.html" else title
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1b2596">
  <link rel="icon" href="{asset('images/favicon.svg')}" type="image/svg+xml">
  <link rel="alternate" hreflang="en" href="{('../' if rtl else '') + STATE['page']}">
  <link rel="alternate" hreflang="ur" href="{('' if rtl else 'ur/') + STATE['page']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts}" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/{bs_css}">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css">
  <link rel="stylesheet" href="{asset('css/style.css')}">
</head>
<body>
  <div class="preloader" aria-hidden="true"><div class="text-center"><span class="cap d-inline-block" style="color:#1b2596">{LOGO_SVG}</span><div class="bar mx-auto"></div></div></div>
  <div class="scroll-progress"></div>
"""


def header():
    en_href = ("../" if is_ur() else "") + STATE["page"]
    ur_href = ("" if is_ur() else "ur/") + STATE["page"]
    dd_items = "".join(
        f'<li><a class="dropdown-item" href="{f}"><i class="bi {ic}"></i>{t(en, ur)}</a></li>'
        for _, f, ic, en, ur in COURSES
    )
    return f"""
  <header class="site-header">
    <nav class="navbar navbar-expand-lg">
      <div class="container">
        {brand()}
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="{t('Toggle navigation', 'مینو کھولیں')}">
          <span class="hamburger"><span></span><span></span><span></span></span>
        </button>
        <div class="collapse navbar-collapse" id="mainNav">
          <ul class="navbar-nav main-nav mx-auto">
            <li class="nav-item"><a class="nav-link{nav_active('home')}" href="index.html">{t('Home', 'ہوم')}</a></li>
            <li class="nav-item"><a class="nav-link{nav_active('about')}" href="about.html">{t('About', 'تعارف')}</a></li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle{nav_active('courses')}" href="courses.html" role="button" data-bs-toggle="dropdown" aria-expanded="false">{t('Courses', 'کورسز')}</a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="courses.html"><i class="bi bi-grid"></i>{t('All Skill Tracks', 'تمام کورسز')}</a></li>
                {dd_items}
              </ul>
            </li>
            <li class="nav-item"><a class="nav-link{nav_active('funding')}" href="funding.html">{t('Funding Options', 'مالی سہولت')}</a></li>
            <li class="nav-item"><a class="nav-link{nav_active('admissions')}" href="admissions.html">{t('Admissions', 'داخلہ')}</a></li>
          </ul>
          <div class="nav-actions d-flex align-items-center gap-4">
            <div class="lang-switch">
              <i class="bi bi-globe2"></i>
              <a href="{en_href}" class="{'' if is_ur() else 'current'}" hreflang="en" lang="en">EN</a>
              <span class="sep"></span>
              <a href="{ur_href}" class="ur {'current' if is_ur() else ''}" hreflang="ur" lang="ur">اردو</a>
            </div>
            <a href="apply.html" class="btn-ubk btn-sm-ubk">{t('Apply Now', 'ابھی اپلائی کریں')} <i class="bi bi-arrow-right"></i></a>
          </div>
        </div>
      </div>
    </nav>
  </header>
  <main>
"""


def footer():
    learn = "".join(
        f'<li><a href="{f}">{t(en, ur)}</a></li>' for _, f, _, en, ur in
        [("", "courses.html", "", "Courses", "کورسز")] + COURSES
    ) + f'<li><a href="student-work.html">{t("Student Work", "طلبہ کا کام")}</a></li>'
    return f"""
  </main>

  <footer class="site-footer">
    <div class="footer-watermark">UBK</div>
    <div class="container position-relative">
      <div class="row g-4">
        <div class="col-lg-5">
          {brand(on_dark=True)}
          <h2 class="tagline">{t('Build Skills.<br>Build<br>Independence.', 'ڈیجیٹل اسکلز سیکھیں۔<br>خود مختار بنیں۔')}</h2>
        </div>
        <div class="col-lg-4 col-md-8">
          <div class="row g-4">
            <div class="col-5"><h6>{t('Learn', 'سیکھیں')}</h6><ul>{learn}</ul></div>
            <div class="col-4"><h6>{t('Apply', 'داخلہ')}</h6><ul>
              <li><a href="admissions.html">{t('Admissions', 'داخلہ')}</a></li>
              <li><a href="apply.html">{t('Apply Now', 'ابھی اپلائی کریں')}</a></li>
              <li><a href="funding.html">{t('Funding', 'مالی سہولت')}</a></li>
              <li><a href="faq.html">{t('FAQ', 'سوالات')}</a></li>
            </ul></div>
            <div class="col-3"><h6>UBK</h6><ul>
              <li><a href="about.html">{t('About', 'تعارف')}</a></li>
              <li><a href="contact.html">{t('Contact', 'رابطہ')}</a></li>
            </ul></div>
          </div>
        </div>
        <div class="col-lg-3 col-md-4 d-flex flex-column align-items-lg-end">
          <div class="socials">
            <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
            <a href="#" aria-label="X"><i class="bi bi-twitter-x"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
            <a href="#" aria-label="YouTube"><i class="bi bi-youtube"></i></a>
            <a href="#" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
          </div>
          <a href="#" class="back-top js-top"><span class="pill">{t('Back To Top', 'اوپر جائیں')}</span><span class="circle"><i class="bi bi-arrow-up"></i></span></a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>{t('© 2026 UBK Skill Development Systems. All rights reserved.', '© 2026 UBK مہارت ترقیاتی نظام۔ جملہ حقوق محفوظ ہیں۔')}</span>
        <a href="privacy-policy.html">{t('Privacy Policy', 'پرائیویسی پالیسی')}</a>
        <a href="terms.html">{t('Terms', 'شرائط')}</a>
      </div>
    </div>
  </footer>

  <button class="to-top js-top" aria-label="{t('Back to top', 'اوپر جائیں')}">
    <svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="24"/></svg>
    <i class="bi bi-arrow-up"></i>
  </button>

  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
  <script src="{asset('js/main.js')}"></script>
</body>
</html>
"""


def page_hero(eyebrow, title, text, image, alt, button=None, breadcrumb=None):
    btn = ""
    if button:
        label, href = button
        btn = f'<a href="{href}" class="btn-ubk btn-orange fade-in-up d-3">{label}</a>'
    crumb = ""
    if breadcrumb:
        crumb = f'<div class="breadcrumb-ubk fade-in-up">{breadcrumb}</div>'
    body = f'<p class="fade-in-up d-2">{text}</p>' if text else ""
    return f"""
  <section class="page-hero">
    <div class="container position-relative">
      <div class="row align-items-center">
        <div class="col-lg-6">
          {crumb}
          <span class="eyebrow fade-in-up d-1">{eyebrow}</span>
          <h1 class="reveal-block fade-in-up d-1">{title}</h1>
          {body}
          {btn}
        </div>
        <div class="col-lg-5 offset-lg-1">
          <div class="media pop d-2"><img src="{img(image)}" alt="{alt}"></div>
        </div>
      </div>
    </div>
  </section>
"""
