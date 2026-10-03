(function () {
  const LANGS = {
    de: { code: 'DE', name: 'Deutsch' },
    fr: { code: 'FR', name: 'Français' },
    en: { code: 'EN', name: 'English' },
    es: { code: 'ES', name: 'Español' },
    lb: { code: 'LB', name: 'Lëtzebuergesch' },
    pt: { code: 'PT', name: 'Português' }
  };
  const DEFAULT_LANG = 'fr';
  const STORAGE_KEY = 'as-landing-lang';

  const btn = document.getElementById('langBtn');
  const menu = document.getElementById('langMenu');
  const options = Array.from(menu.querySelectorAll('.lang-option'));
  const main = document.getElementById('main');

  /* ---------- Translation ---------- */
  function applyLang(lang) {
    const dict = window.I18N[lang] || window.I18N[DEFAULT_LANG];

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const val = dict[el.dataset.i18n];
      if (val !== undefined) el.textContent = val;
    });
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const val = dict[el.dataset.i18nHtml];
      if (val !== undefined) el.innerHTML = val;
    });

    document.documentElement.lang = lang;
    document.title = dict['meta.title'] || document.title;

    btn.querySelector('#langBtnCode').textContent = LANGS[lang].code;
    btn.querySelector('#langBtnName').textContent = LANGS[lang].name;
    options.forEach(o => o.setAttribute('aria-selected', String(o.dataset.lang === lang)));

    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
    const url = new URL(location.href);
    url.searchParams.set('lang', lang);
    history.replaceState(null, '', url);
  }

  function switchLang(lang) {
    if (!LANGS[lang]) return;
    if (document.startViewTransition && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.startViewTransition(() => applyLang(lang));
    } else {
      main.classList.add('switching');
      setTimeout(() => { applyLang(lang); main.classList.remove('switching'); }, 150);
    }
  }

  function initialLang() {
    const fromUrl = new URLSearchParams(location.search).get('lang');
    if (fromUrl && LANGS[fromUrl]) return fromUrl;
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved && LANGS[saved]) return saved;
    } catch (e) {}
    const nav = (navigator.language || '').slice(0, 2).toLowerCase();
    return LANGS[nav] ? nav : DEFAULT_LANG;
  }

  /* ---------- Dropdown ---------- */
  function openMenu() {
    menu.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    const current = options.find(o => o.getAttribute('aria-selected') === 'true') || options[0];
    current.focus();
  }
  function closeMenu(returnFocus) {
    menu.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    if (returnFocus) btn.focus();
  }

  btn.addEventListener('click', () => (menu.classList.contains('open') ? closeMenu(false) : openMenu()));

  options.forEach((opt, i) => {
    opt.addEventListener('click', () => { switchLang(opt.dataset.lang); closeMenu(true); });
    opt.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); opt.click(); }
      if (e.key === 'ArrowDown') { e.preventDefault(); options[(i + 1) % options.length].focus(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); options[(i - 1 + options.length) % options.length].focus(); }
    });
  });

  document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('open')) closeMenu(true); });
  document.addEventListener('click', e => { if (!e.target.closest('.lang-switch')) closeMenu(false); });

  /* ---------- Top bar on scroll ---------- */
  const topbar = document.getElementById('topbar');
  const onScroll = () => topbar.classList.toggle('scrolled', window.scrollY > 30);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Reveal + language rings ---------- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('visible');
      entry.target.querySelectorAll('.ring').forEach(r => r.style.setProperty('--p', r.dataset.p));
      io.unobserve(entry.target);
    });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  applyLang(initialLang());
})();
