"""Build the UBK static site in English (/) and Urdu (/ur/).

Usage:  python _build/build.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import STATE, head, header, footer  # noqa: E402
import pages_main as pm  # noqa: E402
import pages_more as pmo  # noqa: E402
import pages_legal as pl  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = {
    "index.html": pm.home,
    "about.html": pm.about,
    "courses.html": pm.courses,
    "graphic-design.html": lambda: pm.course_detail("graphic-design"),
    "ecommerce.html": lambda: pm.course_detail("ecommerce"),
    "digital-marketing.html": lambda: pm.course_detail("digital-marketing"),
    "video-editing.html": lambda: pm.course_detail("video-editing"),
    "funding.html": pmo.funding,
    "admissions.html": pmo.admissions,
    "apply.html": pmo.apply,
    "application-received.html": pmo.received,
    "student-work.html": pmo.student_work,
    "faq.html": pmo.faq,
    "contact.html": pmo.contact,
    "privacy-policy.html": pl.privacy,
    "terms.html": pl.terms,
}


def build():
    count = 0
    for lang, folder in (("en", ROOT), ("ur", os.path.join(ROOT, "ur"))):
        os.makedirs(folder, exist_ok=True)
        STATE["lang"] = lang
        for filename, fn in PAGES.items():
            STATE["page"] = filename
            (title, description), body = fn()
            html = head(title, description) + header() + body + footer()
            with open(os.path.join(folder, filename), "w", encoding="utf-8", newline="\n") as f:
                f.write(html)
            count += 1
    print(f"Built {count} pages.")


if __name__ == "__main__":
    build()
