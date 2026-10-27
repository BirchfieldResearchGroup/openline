/* One selection per specification, shared by its figures and its table rows: a part of a
   conductor, or a point a structure holds a wire at. Labels keep one size on screen. */
(() => {
  const figures = [...document.querySelectorAll('.openline-figure')];
  const scopes = new Set(figures.map(figure => figure.closest('.openline-spec') || figure));

  for (const scope of scopes) {
    const marked = [...scope.querySelectorAll('.openline-figure [data-ol-key]')];
    const keys = new Map();  // each key's first named item: what a reader hears it called
    for (const item of marked) {
      if (item.hasAttribute('aria-label') && !keys.has(item.dataset.olKey)) keys.set(item.dataset.olKey, item);
    }
    for (const label of scope.querySelectorAll('span.ol-selection')) {
      const target = keys.get(label.dataset.olKey);
      if (!target) continue;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'ol-selection';
      button.dataset.olKey = label.dataset.olKey;
      if (target.dataset.olWire) button.dataset.olWire = target.dataset.olWire;
      button.textContent = label.textContent;
      button.setAttribute('aria-label', target.getAttribute('aria-label') || `Inspect ${label.textContent}`);
      button.setAttribute('aria-pressed', 'false');
      label.replaceWith(button);
    }
    const controls = [...scope.querySelectorAll('[data-ol-key][role="button"], button.ol-selection')];
    const painted = [...marked, ...scope.querySelectorAll('button.ol-selection')];
    const rows = [...scope.querySelectorAll('tr')]
      .map(row => [row, row.querySelector('[data-ol-key]')?.dataset.olKey])
      .filter(([, key]) => key);
    const status = scope.querySelector('.ol-selection-status');
    let pinned = null;

    // Any drawing of a part selects it under the pointer; its first is the button keys reach.
    const keyOf = target => target instanceof Element
      ? target.closest('svg [data-ol-key], button.ol-selection')?.dataset.olKey ?? null
      : null;
    function paint(key) {
      for (const item of painted) item.classList.toggle('ol-active', item.dataset.olKey === key);
      for (const item of controls) item.setAttribute('aria-pressed', String(item.dataset.olKey === pinned));
      for (const [row, rowKey] of rows) row.classList.toggle('ol-active', rowKey === key);
      if (status) status.textContent = key ? keys.get(key)?.getAttribute('aria-label') ?? '' : '';
    }
    function pin(key) {
      pinned = pinned === key ? null : key;
      paint(pinned);
    }
    for (const name of ['pointerover', 'focusin']) {
      scope.addEventListener(name, event => {
        const key = keyOf(event.target);
        if (key) paint(key);
      });
    }
    for (const name of ['pointerout', 'focusout']) {
      scope.addEventListener(name, event => {
        if (keyOf(event.target)) paint(keyOf(event.relatedTarget) ?? pinned);
      });
    }
    scope.addEventListener('click', event => {
      const key = keyOf(event.target);
      if (key) pin(key);
    });
    scope.addEventListener('keydown', event => {
      if (event.altKey || event.ctrlKey || event.metaKey) return;
      const key = keyOf(event.target);
      if (event.key === 'Escape' && (key || pinned)) {
        pinned = null;
        paint(null);
        event.preventDefault();
        return;
      }
      if (!key) return;
      if (['Enter', ' '].includes(event.key) && event.target.tagName.toLowerCase() !== 'button') {
        event.preventDefault();
        pin(key);
      }
      const owner = event.target.closest('svg');
      if (owner && ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) {
        const ring = [...owner.querySelectorAll('[role="button"]')];
        const step = ['ArrowRight', 'ArrowDown'].includes(event.key) ? 1 : -1;
        const next = ring[(ring.indexOf(event.target.closest('[role="button"]')) + step + ring.length) % ring.length];
        event.preventDefault();
        next?.focus({ preventScroll: true });
      }
    });
  }

  for (const figure of figures) {
    for (const svg of figure.querySelectorAll('.ol-diagram')) {
      const anchors = [...svg.querySelectorAll('.ol-anchor')];
      const resize = () => {
        const scale = Math.abs(svg.getScreenCTM()?.a || 1);
        svg.style.setProperty('--ol-label-size', `${14 / scale}px`);
        for (const anchor of anchors) {
          anchor.querySelector('.ol-hit')?.setAttribute('r', String(12 / scale));
          anchor.querySelector('.ol-ring')?.setAttribute('r', String(8 / scale));
          anchor.querySelector('.ol-dot')?.setAttribute('transform', `scale(${0.6 / scale})`);
        }
      };
      new ResizeObserver(resize).observe(svg);
      resize();
    }
    const toggle = figure.querySelector('.ol-dimensions-toggle');
    if (toggle) {
      toggle.hidden = false;
      toggle.setAttribute('aria-pressed', 'false');
      figure.dataset.dimensions = 'false';
      toggle.addEventListener('click', () => {
        const show = figure.dataset.dimensions !== 'true';
        figure.dataset.dimensions = String(show);
        toggle.setAttribute('aria-pressed', String(show));
      });
    }
  }
})();
