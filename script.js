const nav = document.querySelector('.nav');
const burger = document.querySelector('.nav__burger');

// Sticky nav border + mobile menu
addEventListener('scroll', () => nav.classList.toggle('is-scrolled', scrollY > 10), { passive: true });
burger.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  burger.setAttribute('aria-expanded', open);
});
document.querySelectorAll('.nav__mobile a').forEach(a =>
  a.addEventListener('click', () => {
    nav.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
  })
);

// Fade sections in as they scroll into view
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('is-in');
      io.unobserve(e.target);
      // Drop the stagger delay once shown so hovers react instantly
      setTimeout(() => e.target.style.removeProperty('--d'), 1400);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.section .wrap > *, .stats').forEach(el => {
  el.classList.add('reveal');
  io.observe(el);
});
// Items inside grids and lists pop in one after another
document.querySelectorAll('.cards, .team__grid, .timeline, .kit__list, .faq__list').forEach(group => {
  [...group.children].forEach((el, i) => {
    el.classList.add('reveal');
    el.style.setProperty('--d', `${i * 120}ms`);
    io.observe(el);
  });
});

const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
const colors = ['#d9502a', '#f2b33d', '#2f8f7a', '#3f7fd0', '#e98bb0'];
const pick = arr => arr[Math.floor(Math.random() * arr.length)];

// Hero headline: split into words that pop in one by one
const h1 = document.querySelector('.display');
let wi = 0;
[...h1.childNodes].forEach(node => {
  if (node.nodeType === 3) {
    const frag = document.createDocumentFragment();
    node.textContent.split(/(\s+)/).forEach(part => {
      if (!part.trim()) return frag.append(part);
      const s = document.createElement('span');
      s.className = 'w';
      s.style.setProperty('--i', wi++);
      s.textContent = part;
      frag.append(s);
    });
    node.replaceWith(frag);
  } else if (node.classList?.contains('accent')) {
    node.classList.add('w');
    node.style.setProperty('--i', wi++);
  }
});

// Hero: bubbles and stars drifting upwards
if (!calm) {
  const hero = document.querySelector('.hero, .page-hero');
  for (let i = 0; i < (hero.classList.contains('hero') ? 14 : 8); i++) {
    const b = document.createElement('span');
    const kind = Math.random();
    b.className = 'bubble' + (kind < .3 ? ' bubble--star' : kind < .55 ? ' bubble--ring' : '');
    b.setAttribute('aria-hidden', 'true');
    b.style.cssText = `left:${Math.random() * 100}%;--s:${10 + Math.random() * 26}px;--c:${pick(colors)};` +
      `--t:${12 + Math.random() * 12}s;--delay:${-Math.random() * 20}s;--sway:${(Math.random() - .5) * 120}px;--o:${.35 + Math.random() * .35}`;
    hero.append(b);
  }
}

// Numbers count up when they scroll into view
const countIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    countIO.unobserve(e.target);
    const num = e.target.firstChild;
    const end = parseInt(num.textContent, 10);
    if (calm || !end) return;
    const t0 = performance.now();
    const tick = now => {
      const p = Math.min((now - t0) / 1200, 1);
      num.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
}, { threshold: .6 });
document.querySelectorAll('.stats__nums b, .team__stat b').forEach(b => countIO.observe(b));

// Footer wordmark: letters wave on hover
const mark = document.querySelector('.footer__mark');
const word = mark.lastChild;
const letters = document.createElement('span');
letters.append(...[...word.textContent].map((ch, i) => {
  const s = document.createElement('span');
  s.className = 'l';
  s.style.setProperty('--i', i);
  s.textContent = ch;
  return s;
}));
word.replaceWith(letters);

// Confetti burst wherever you click
if (!calm) {
  addEventListener('click', e => {
    if (e.target.closest('input, textarea')) return;
    for (let i = 0; i < 12; i++) {
      const c = document.createElement('span');
      const angle = (Math.PI * 2 * i) / 12 + Math.random() * .4;
      const dist = 40 + Math.random() * 50;
      c.className = 'confetti';
      c.style.cssText = `left:${e.clientX}px;top:${e.clientY}px;background:${pick(colors)};` +
        `--x:${Math.cos(angle) * dist}px;--y:${Math.sin(angle) * dist}px;--r:${Math.random() * 540}deg;` +
        (Math.random() < .4 ? 'border-radius:50%;' : '');
      document.body.append(c);
      c.addEventListener('animationend', () => c.remove());
    }
  });
}

// Clinic rooms: swap the photo when a room is picked
const roomImg = document.getElementById('roomImg');
const rooms = document.querySelectorAll('.room');
rooms.forEach(room => {
  new Image().src = `assets/images/${room.dataset.img}`;
  room.addEventListener('click', () => {
    if (room.classList.contains('is-on')) return;
    rooms.forEach(r => {
      r.classList.toggle('is-on', r === room);
      r.setAttribute('aria-selected', r === room);
    });
    roomImg.classList.add('is-fading');
    setTimeout(() => {
      roomImg.src = `assets/images/${room.dataset.img}`;
      roomImg.alt = room.dataset.alt;
      roomImg.classList.remove('is-fading');
    }, 300);
  });
});

// Duplicate the photo strip so the scroll loops seamlessly
const track = document.querySelector('.strip__track');
if (track) track.innerHTML += track.innerHTML.replace(/alt="[^"]*"/g, 'alt="" aria-hidden="true"');

// Booking form: chips + WhatsApp hand-off
const form = document.getElementById('bookForm');
const summary = document.getElementById('summary');
const msg = document.getElementById('formMsg');
const picks = { concern: [], age: [], time: [] };
const multi = { concern: true };

// Only the home page has the form
form?.querySelectorAll('.chips').forEach(group => {
  const name = group.dataset.name;
  group.addEventListener('click', e => {
    const chip = e.target.closest('.chip');
    if (!chip) return;
    if (!multi[name]) group.querySelectorAll('.chip').forEach(c => c !== chip && c.classList.remove('is-on'));
    chip.classList.toggle('is-on');
    picks[name] = [...group.querySelectorAll('.is-on')].map(c => c.textContent);
    summary.textContent = picks.concern.length ? picks.concern.join(', ') : 'Not sure yet';
  });
});

form?.addEventListener('submit', e => {
  e.preventDefault();
  const required = [...form.querySelectorAll('[required]')];
  required.forEach(i => i.classList.toggle('is-bad', !i.value.trim()));
  if (required.some(i => !i.value.trim())) {
    msg.textContent = 'Please fill in the fields marked *.';
    msg.classList.add('is-bad');
    return;
  }
  msg.textContent = 'We use this only to arrange your visit.';
  msg.classList.remove('is-bad');

  const f = new FormData(form);
  const lines = [
    'Hello NeuroNest, I would like to book a visit.',
    `Patient: ${f.get('child')}${picks.age.length ? ` (${picks.age[0]})` : ''}`,
    `Concern: ${picks.concern.join(', ') || 'Not sure'}`,
    picks.time.length && `Preferred time: ${picks.time[0]}`,
    `Name: ${f.get('parent')}`,
    `Phone: ${f.get('phone')}`,
    f.get('notes').trim() && `Notes: ${f.get('notes').trim()}`,
  ].filter(Boolean);
  window.open(`https://wa.me/918180095783?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
});

document.getElementById('year').textContent = new Date().getFullYear();
