/* =========================================================
   UBK — site interactions (jQuery)
   ========================================================= */
(function ($) {
  "use strict";

  var isRTL = document.documentElement.dir === "rtl";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Preloader ---------- */
  $(window).on("load", function () {
    setTimeout(function () { $(".preloader").addClass("hide"); }, 250);
  });
  // Safety net if load never fires (slow images)
  setTimeout(function () { $(".preloader").addClass("hide"); }, 3500);

  $(function () {

    /* ---------- AOS ---------- */
    if (window.AOS) {
      AOS.init({ duration: 900, easing: "ease-out-cubic", once: true, offset: 60, disable: reduceMotion });
      // Lazy images and sliders change the page height after AOS measures it,
      // so re-measure whenever an image finishes loading.
      var aosTimer;
      var refreshAOS = function () {
        clearTimeout(aosTimer);
        aosTimer = setTimeout(function () { AOS.refresh(); }, 120);
      };
      $("img").each(function () { if (!this.complete) $(this).one("load error", refreshAOS); });
      $(window).on("load resize", refreshAOS);
    }

    /* ---------- Header: shrink + hide on scroll down ---------- */
    var $header = $(".site-header"), lastY = 0;
    var $progress = $(".scroll-progress"), $toTop = $(".to-top"), $ring = $(".to-top circle");
    function onScroll() {
      var y = $(window).scrollTop();
      var max = $(document).height() - $(window).height();
      var pct = max > 0 ? y / max : 0;
      $header.toggleClass("scrolled", y > 20);
      if (!$(".navbar-collapse").hasClass("show")) {
        $header.toggleClass("hide-up", y > lastY && y > 400);
      }
      lastY = y;
      $progress.css("width", (pct * 100) + "%");
      $toTop.toggleClass("show", y > 600);
      $ring.css("stroke-dashoffset", 150.8 - 150.8 * pct);
    }
    $(window).on("scroll", onScroll);
    onScroll();

    /* ---------- Back to top ---------- */
    $(document).on("click", ".js-top", function (e) {
      e.preventDefault();
      $("html, body").animate({ scrollTop: 0 }, 700);
    });

    /* ---------- Counters ---------- */
    function countUp($el) {
      var target = parseFloat($el.data("count"));
      var suffix = $el.data("suffix") || "";
      var pad = String($el.data("count")).length;
      var padZero = $el.data("pad") === true || $el.data("pad") === "true";
      $({ n: 0 }).animate({ n: target }, {
        duration: 1800,
        easing: "swing",
        step: function (now) {
          var v = Math.floor(now);
          $el.text((padZero ? String(v).padStart(2, "0") : v) + suffix);
        },
        complete: function () {
          $el.text((padZero ? String(target).padStart(Math.max(2, pad), "0") : target) + suffix);
        }
      });
    }

    /* ---------- In-view observer (counters, timeline, tables) ---------- */
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var $t = $(en.target);
          if ($t.is("[data-count]")) countUp($t);
          else $t.addClass("in");
          io.unobserve(en.target);
        });
      }, { threshold: 0.35 });
      $("[data-count], .skills-line, .compare-table").each(function () { io.observe(this); });
    } else {
      $("[data-count]").each(function () { countUp($(this)); });
      $(".skills-line, .compare-table").addClass("in");
    }

    /* ---------- Skills timeline dots aligned to rows ---------- */
    $(".skills-line").each(function () {
      var $line = $(this), rows = $line.data("rows") || 6, html = "";
      for (var i = 0; i < rows; i++) {
        var top = ((i + 0.5) / rows) * 100;
        html += '<span style="top:' + top + '%;transition-delay:' + (0.25 * i + 0.3) + 's"></span>';
      }
      $line.append(html);
    });

    /* ---------- Accordions ---------- */
    $(document).on("click", ".ubk-acc .acc-head", function () {
      var $item = $(this).closest(".acc-item");
      var $acc = $item.closest(".ubk-acc");
      if ($acc.data("single") !== false) {
        $acc.find(".acc-item.open").not($item).removeClass("open").find(".acc-body").stop().slideUp(350);
      }
      $item.toggleClass("open");
      $item.find(".acc-body").stop().slideToggle(350);
      $(this).attr("aria-expanded", $item.hasClass("open"));
    });
    $(".ubk-acc .acc-item.open .acc-body").show();

    /* ---------- FAQ cards ---------- */
    $(document).on("click", ".faq-card", function () {
      var $c = $(this);
      $c.closest(".faq-grid").find(".faq-card").not($c).removeClass("open");
      $c.toggleClass("open");
    });

    /* ---------- Sliders (Slick) ---------- */
    if ($.fn.slick) {
      $(".work-slider").each(function () {
        var $s = $(this);
        $s.slick({
          slidesToShow: 2.6, slidesToScroll: 1, infinite: false, arrows: false, dots: false,
          rtl: isRTL, speed: 700, cssEase: "cubic-bezier(.22,1,.36,1)", swipeToSlide: true,
          responsive: [
            { breakpoint: 992, settings: { slidesToShow: 2.1 } },
            { breakpoint: 576, settings: { slidesToShow: 1.15 } }
          ]
        });
        var $nav = $s.closest("section").find(".slider-nav");
        $nav.find(".prev").on("click", function () { $s.slick("slickPrev"); });
        $nav.find(".next").on("click", function () { $s.slick("slickNext"); });
      });

      $(".testimonial-slider").slick({
        slidesToShow: 1, arrows: false, dots: true, autoplay: true, autoplaySpeed: 5500,
        fade: true, speed: 800, rtl: isRTL, adaptiveHeight: false
      });
    }

    /* ---------- 3D tilt on track cards ---------- */
    if (!reduceMotion && window.matchMedia("(hover: hover)").matches) {
      $(".track-card").on("mousemove", function (e) {
        var r = this.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        $(this).css("transform", "perspective(900px) rotateY(" + (x * 8) + "deg) rotateX(" + (-y * 8) + "deg) translateY(-6px)");
      }).on("mouseleave", function () {
        $(this).css("transform", "");
      });

      // Subtle parallax on hero bento
      $(".hero-home").on("mousemove", function (e) {
        var cx = e.clientX / window.innerWidth - 0.5;
        var cy = e.clientY / window.innerHeight - 0.5;
        $(".hero-bento .col-a").css("transform", "translate(" + (cx * -10) + "px," + (cy * -8) + "px)");
        $(".hero-bento .col-b").css("transform", "translate(" + (cx * 10) + "px," + (cy * 8) + "px)");
      });
    }

    /* ---------- Portfolio filter ---------- */
    $(".filter-btn").on("click", function () {
      var f = $(this).data("filter");
      $(this).addClass("active").siblings().removeClass("active");
      $(".portfolio-item").each(function () {
        var $i = $(this), show = f === "all" || $i.data("cat") === f;
        if (show) {
          $i.removeClass("is-gone");
          requestAnimationFrame(function () { $i.removeClass("is-hidden"); });
        } else {
          $i.addClass("is-hidden");
          setTimeout(function () { if ($i.hasClass("is-hidden")) $i.addClass("is-gone"); }, 450);
        }
      });
    });

    /* ---------- FAQ page category scrollspy ---------- */
    var $cats = $(".faq-cats a");
    if ($cats.length) {
      $cats.on("click", function (e) {
        e.preventDefault();
        var $t = $($(this).attr("href"));
        $("html, body").animate({ scrollTop: $t.offset().top - 100 }, 600);
      });
      $(window).on("scroll", function () {
        var y = $(window).scrollTop() + 160, current = null;
        $(".faq-group").each(function () { if ($(this).offset().top <= y) current = this.id; });
        if (current) {
          $cats.removeClass("active").filter('[href="#' + current + '"]').addClass("active");
          $(".faq-group").removeClass("active").filter("#" + current).addClass("active");
        }
      });
    }

    /* ---------- Apply form: preselect track from ?track= ---------- */
    var params = new URLSearchParams(window.location.search);
    var preTrack = params.get("track");
    if (preTrack) {
      $('input[name="track"][value="' + preTrack + '"]').prop("checked", true);
    }
    $('input[name="track"]').on("change", function () {
      $('input[name="track"]').each(function () {
        $(this).next("span").find("small").text($(this).is(":checked") ? $(this).data("on") : $(this).data("off"));
      });
    }).filter(":checked").trigger("change");

    /* ---------- Form validation ---------- */
    function validate($form) {
      var ok = true;
      $form.find("[required]").each(function () {
        var $f = $(this), val = $.trim($f.val() || ""), valid = val.length > 0;
        if ($f.attr("type") === "email") valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
        if ($f.attr("type") === "tel") valid = val.replace(/\D/g, "").length >= 10;
        if ($f.is(":radio")) valid = $form.find('[name="' + $f.attr("name") + '"]:checked').length > 0;
        var $field = $f.closest(".field");
        $field.toggleClass("has-error", !valid);
        $f.toggleClass("is-invalid", !valid && !$f.is(":radio"));
        if (!valid) ok = false;
      });
      if (!ok) {
        var $first = $form.find(".has-error").first();
        $("html, body").animate({ scrollTop: $first.offset().top - 120 }, 500);
      }
      return ok;
    }
    $(document).on("input change", ".form-ubk [required]", function () {
      var $f = $(this);
      $f.removeClass("is-invalid").closest(".field").removeClass("has-error");
    });

    $(".js-apply-form").on("submit", function (e) {
      e.preventDefault();
      var $form = $(this);
      if (!validate($form)) return;
      var $btn = $form.find("[type=submit]");
      $btn.prop("disabled", true).html('<span class="spinner-border spinner-border-sm"></span>');
      setTimeout(function () { window.location.href = $form.attr("action"); }, 900);
    });

    $(".js-contact-form").on("submit", function (e) {
      e.preventDefault();
      var $form = $(this);
      if (!validate($form)) return;
      var $btn = $form.find("[type=submit]"), label = $btn.html();
      $btn.prop("disabled", true).html('<span class="spinner-border spinner-border-sm"></span>');
      setTimeout(function () {
        $form[0].reset();
        $btn.prop("disabled", false).html(label);
        toast($form.data("success"));
      }, 900);
    });

    function toast(msg) {
      var $t = $('<div class="ubk-toast"><i class="bi bi-check-circle-fill"></i><span></span></div>');
      $t.find("span").text(msg);
      $("body").append($t);
      setTimeout(function () { $t.addClass("show"); }, 30);
      setTimeout(function () { $t.removeClass("show"); setTimeout(function () { $t.remove(); }, 600); }, 3600);
    }

    /* ---------- Application received: confetti + reference ---------- */
    var $ref = $(".js-ref");
    if ($ref.length) {
      var ref = "UBK-2027-" + Math.floor(10000 + Math.random() * 89999);
      $ref.text(ref);
      if (!reduceMotion) {
        var colors = ["#ee4b0b", "#ffffff", "#16a36a", "#ffb088", "#8f98ff"];
        var $hero = $(".received-hero");
        for (var i = 0; i < 60; i++) {
          $('<span class="confetti"></span>').css({
            left: Math.random() * 100 + "%",
            background: colors[i % colors.length],
            animationDuration: (2.2 + Math.random() * 2.4) + "s",
            animationDelay: (Math.random() * 0.9) + "s",
            transform: "rotate(" + Math.random() * 360 + "deg)"
          }).appendTo($hero);
        }
      }
    }

    /* ---------- Desktop: "Courses" opens on hover, click goes to the page ---------- */
    $(".main-nav .dropdown-toggle").on("click", function (e) {
      if (window.innerWidth >= 992) {
        e.preventDefault();
        e.stopImmediatePropagation();
        window.location.href = $(this).attr("href");
      }
    });

    /* ---------- Close mobile nav on link click ---------- */
    $(".navbar-collapse .nav-link:not(.dropdown-toggle)").on("click", function () {
      var c = bootstrap.Collapse.getInstance($(".navbar-collapse")[0]);
      if (c) c.hide();
    });
  });
})(jQuery);
