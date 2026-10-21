
(function () {
  var root = document.documentElement;
  var themeBtn = document.getElementById('themeBtn');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var cur = root.getAttribute('data-theme');
    if (!cur) {
      var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      cur = dark ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('aprep-theme', next); } catch (e) {}
  });

  var menuBtn = document.getElementById('menuBtn');
  var scrim = document.getElementById('scrim');
  function closeNav() {
    document.body.classList.remove('navopen');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }
  if (menuBtn) menuBtn.addEventListener('click', function () {
    var open = document.body.classList.toggle('navopen');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  if (scrim) scrim.addEventListener('click', closeNav);

  // Wide tables and code blocks scroll inside their own box, never the page.
  var prose = document.querySelector('.prose');
  if (prose) {
    prose.querySelectorAll('table').forEach(function (t) {
      if (t.parentElement && t.parentElement.classList.contains('tablewrap')) return;
      var w = document.createElement('div');
      w.className = 'tablewrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }

  // Highlight the heading currently in view.
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = map[en.target.id];
        if (!a) return;
        if (en.isIntersecting) {
          tocLinks.forEach(function (x) { x.classList.remove('active'); });
          a.classList.add('active');
        }
      });
    }, { rootMargin: '-70px 0px -75% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) obs.observe(el);
    });
  }

  // ---- search: the index is fetched only when the box is first used ----
  var q = document.getElementById('q');
  var results = document.getElementById('results');
  if (!q || !results) return;
  var base = q.getAttribute('data-base') || '';
  var loading = false, sel = -1, shown = [];

  var waiting = [];
  function loadIndex(cb) {
    if (window.APREP_INDEX) { if (cb) cb(); return; }
    if (cb) waiting.push(cb);          // queue, so a second caller is never dropped
    if (loading) return;
    loading = true;
    var s = document.createElement('script');
    s.src = base + 'assets/search-index.js';
    s.onload = function () {
      loading = false;
      var q = waiting; waiting = [];
      q.forEach(function (f) { f(); });
    };
    s.onerror = function () {
      loading = false; waiting = [];
      results.innerHTML = '<div class="empty">Search index did not load.</div>';
      results.hidden = false;
    };
    document.head.appendChild(s);
  }
  q.addEventListener('focus', function () { loadIndex(null); });

  function score(item, terms) {
    var t = item.t.toLowerCase(), h = item.h.toLowerCase(), b = item.b.toLowerCase(), s = 0;
    for (var i = 0; i < terms.length; i++) {
      var w = terms[i];
      if (!w) continue;
      var hit = 0;
      if (t.indexOf(w) !== -1) { s += t.indexOf(w) === 0 ? 60 : 40; hit = 1; }
      if (h.indexOf(w) !== -1) { s += 14; hit = 1; }
      if (b.indexOf(w) !== -1) { s += 4; hit = 1; }
      if (!hit) return 0;
    }
    return s;
  }

  function render() {
    var v = q.value.trim().toLowerCase();
    if (!v) { results.hidden = true; shown = []; return; }
    if (!window.APREP_INDEX) {
      results.innerHTML = '<div class="empty">Loading index…</div>';
      results.hidden = false;
      loadIndex(render);
      return;
    }
    var terms = v.split(/\s+/);
    var out = [];
    for (var i = 0; i < window.APREP_INDEX.length; i++) {
      var sc = score(window.APREP_INDEX[i], terms);
      if (sc > 0) out.push([sc, window.APREP_INDEX[i]]);
    }
    out.sort(function (a, b) { return b[0] - a[0]; });
    out = out.slice(0, 40);
    shown = out.map(function (o) { return o[1]; });
    sel = -1;
    if (!out.length) {
      results.innerHTML = '<div class="empty">Nothing matches “' +
        q.value.replace(/[<>&]/g, '') + '”.</div>';
    } else {
      results.innerHTML = out.map(function (o) {
        var it = o[1];
        return '<a href="' + base + it.u + '"><div class="rt">' + it.t +
               '</div><div class="rm">' + it.l + ' · ' + it.s + '</div></a>';
      }).join('');
    }
    results.hidden = false;
  }

  q.addEventListener('input', render);
  q.addEventListener('keydown', function (e) {
    var links = results.querySelectorAll('a');
    if (e.key === 'Escape') { results.hidden = true; q.blur(); return; }
    if (!links.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      sel += (e.key === 'ArrowDown' ? 1 : -1);
      if (sel < 0) sel = links.length - 1;
      if (sel >= links.length) sel = 0;
      for (var i = 0; i < links.length; i++) links[i].classList.toggle('sel', i === sel);
      links[sel].scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter' && sel >= 0) {
      e.preventDefault();
      window.location.href = links[sel].getAttribute('href');
    }
  });
  document.addEventListener('click', function (e) {
    if (!results.contains(e.target) && e.target !== q) results.hidden = true;
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== q &&
        !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
      e.preventDefault(); q.focus();
    }
  });
})();
