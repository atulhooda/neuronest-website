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
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.section .wrap > *, .stats').forEach(el => {
  el.classList.add('reveal');
  io.observe(el);
});

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
track.innerHTML += track.innerHTML.replace(/alt="[^"]*"/g, 'alt="" aria-hidden="true"');

// Booking form: chips + WhatsApp hand-off
const form = document.getElementById('bookForm');
const summary = document.getElementById('summary');
const msg = document.getElementById('formMsg');
const picks = { concern: [], age: [], time: [] };
const multi = { concern: true };

form.querySelectorAll('.chips').forEach(group => {
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

form.addEventListener('submit', e => {
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
