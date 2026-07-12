/* ==========================================================================
   ResQAI — Global JavaScript (main.js)
   Loaded on every page via base.html.
   Handles: active nav highlighting, navbar scroll effect, toast helper,
   Bootstrap tooltip init, and back-to-top scroll logic.
   Page-specific logic lives inside each template's {% block extra_scripts %}.
   ========================================================================== */

'use strict';

/* ──────────────────────────────────────────────────────────────────────────
   1. NAVBAR — shrink / elevate on scroll
   ────────────────────────────────────────────────────────────────────────── */
(function initNavbarScroll() {
  const navbar = document.querySelector('.resq-navbar');
  if (!navbar) return;
  const handler = () => {
    if (window.scrollY > 20) {
      navbar.style.boxShadow = '0 2px 16px rgba(0,0,0,.45)';
    } else {
      navbar.style.boxShadow = 'none';
    }
  };
  window.addEventListener('scroll', handler, { passive: true });
  handler(); // run once on load
})();

/* ──────────────────────────────────────────────────────────────────────────
   2. BOOTSTRAP TOOLTIPS — auto-init on [data-bs-toggle="tooltip"]
   ────────────────────────────────────────────────────────────────────────── */
(function initTooltips() {
  if (typeof bootstrap === 'undefined') return;
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
    new bootstrap.Tooltip(el, { trigger: 'hover focus', boundary: 'window' });
  });
})();

/* ──────────────────────────────────────────────────────────────────────────
   3. TOAST HELPER — ResQAI.toast(message, type)
      type: 'success' | 'danger' | 'warning' | 'info'  (default: 'info')
   ────────────────────────────────────────────────────────────────────────── */
const ResQAI = window.ResQAI || {};

ResQAI.toast = function (message, type = 'info') {
  const colours = {
    success: '#34d399',
    danger:  '#dc3545',
    warning: '#ffc107',
    info:    '#0dcaf0',
  };
  const colour = colours[type] || colours.info;

  // Container
  let container = document.getElementById('resq-toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'resq-toast-container';
    Object.assign(container.style, {
      position: 'fixed', bottom: '1.5rem', right: '1.5rem',
      zIndex: '9999', display: 'flex', flexDirection: 'column', gap: '.5rem',
    });
    document.body.appendChild(container);
  }

  // Toast element
  const toast = document.createElement('div');
  Object.assign(toast.style, {
    background: '#1c2128',
    border: `1px solid ${colour}40`,
    borderLeft: `4px solid ${colour}`,
    borderRadius: '8px',
    padding: '.65rem 1rem',
    color: '#e6edf3',
    fontSize: '.82rem',
    maxWidth: '320px',
    boxShadow: '0 4px 20px rgba(0,0,0,.4)',
    opacity: '0',
    transform: 'translateX(20px)',
    transition: 'opacity .25s ease, transform .25s ease',
  });
  toast.textContent = message;
  container.appendChild(toast);

  // Animate in
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      toast.style.opacity = '1';
      toast.style.transform = 'translateX(0)';
    });
  });

  // Animate out after 3 s
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(20px)';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
};

window.ResQAI = ResQAI;

/* ──────────────────────────────────────────────────────────────────────────
   4. BACK-TO-TOP BUTTON — appears after scrolling 400px
   ────────────────────────────────────────────────────────────────────────── */
(function initBackToTop() {
  const btn = document.createElement('button');
  btn.id = 'resq-back-top';
  btn.title = 'Back to top';
  btn.innerHTML = '<i class="bi bi-chevron-up"></i>';
  Object.assign(btn.style, {
    position: 'fixed', bottom: '1.5rem', left: '1.5rem',
    zIndex: '990', width: '38px', height: '38px',
    background: '#1c2128', border: '1px solid #30363d',
    borderRadius: '50%', color: '#8b949e', fontSize: '1rem',
    cursor: 'pointer', opacity: '0', pointerEvents: 'none',
    transition: 'opacity .25s ease, background .18s ease',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
  });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  btn.addEventListener('mouseenter', () => { btn.style.background = '#21262d'; btn.style.color = '#e6edf3'; });
  btn.addEventListener('mouseleave', () => { btn.style.background = '#1c2128'; btn.style.color = '#8b949e'; });
  document.body.appendChild(btn);

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.style.opacity = '1'; btn.style.pointerEvents = 'auto';
    } else {
      btn.style.opacity = '0'; btn.style.pointerEvents = 'none';
    }
  }, { passive: true });
})();
