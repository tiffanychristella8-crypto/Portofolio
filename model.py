/* =====================================================
   script.js — Portfolio Frontend
   Fetches all data from Flask backend API (/api/...)
   ===================================================== */

const API = '';  // same origin

/* ---- Utility ---- */
const $ = id => document.getElementById(id);

async function apiFetch(path) {
  try {
    const res = await fetch(API + path);
    if (!res.ok) throw new Error(res.status);
    return await res.json();
  } catch (e) {
    console.error('API error:', path, e);
    return null;
  }
}

/* ===================== PROFILE ===================== */
async function loadProfile() {
  const data = await apiFetch('/api/profiles');
  if (!data || !data.length) return;
  const p = data[0];

  // Hero section
  if ($('hero-eyebrow')) $('hero-eyebrow').textContent = p.tagline || 'Information Systems Professional';
  if ($('hero-name')) {
    const nameParts = (p.name || '').split(' ');
    if (nameParts.length >= 2) {
      $('hero-name').innerHTML = `${nameParts[0]} <em>${nameParts[1]}</em><br>${nameParts.slice(2).join(' ')}`;
    } else {
      $('hero-name').textContent = p.name || '';
    }
  }
  if ($('hero-bio')) $('hero-bio').textContent = p.bio || '';
  if (p.photo_url && $('hero-photo')) $('hero-photo').src = p.photo_url;

  // About section
  if ($('about-text')) $('about-text').textContent = p.about || p.bio || '';

  // Contact info
  if ($('contact-email')) $('contact-email').textContent = p.email || '';
  if ($('contact-location')) $('contact-location').textContent = p.location || '';

  // Nav & footer
  if ($('nav-name')) $('nav-name').textContent = p.name ? p.name.split(' ').slice(0, 2).join(' ') : 'Portfolio';
  if ($('footer-name')) $('footer-name').textContent = `© ${new Date().getFullYear()} ${p.name || ''}`;

  // Stats (years_exp, organizations, projects_done)
  if ($('stats-row')) {
    const stats = [
      { num: p.years_exp || '3', label: 'Years Exp' },
      { num: p.organizations || '2', label: 'Organizations' },
      { num: p.projects_done || '10', label: 'Projects Done' },
    ];
    $('stats-row').innerHTML = stats.map(s => `
      <div class="stat-item">
        <div class="stat-num">${s.num}<sup>+</sup></div>
        <div class="stat-label">${s.label}</div>
      </div>`).join('');
  }

}

/* ===================== SKILLS ===================== */
async function loadSkills() {
  const data = await apiFetch('/api/skills');
  if (!data) return;

  const technical = data.filter(s => s.type === 'technical');
  const professional = data.filter(s => s.type === 'professional');

  const icons = ['📊', '💬', '⏱️', '🎯', '🤝'];

  if ($('technical-skills')) {
    $('technical-skills').innerHTML = technical.length ? technical.map(s => `
      <div class="skill-bar-item">
        <div class="skill-bar-header">
          <span>${s.name}</span>
          <span>${s.level}%</span>
        </div>
        <div class="skill-bar-track">
          <div class="skill-bar-fill" data-width="${s.level}" style="width:0%"></div>
        </div>
      </div>`).join('')
      : '<p style="color:#888;font-size:.85rem">No technical skills data yet.</p>';
  }

  if ($('professional-skills')) {
    $('professional-skills').innerHTML = professional.length ? professional.map((s, i) => `
      <div class="pro-skill-item">
        <div class="pro-skill-icon">${icons[i % icons.length]}</div>
        <div>
          <div class="pro-skill-name">${s.name}</div>
          <div class="pro-skill-desc">${s.description || ''}</div>
        </div>
      </div>`).join('')
      : '<p style="color:#888;font-size:.85rem">No professional skills data yet.</p>';
  }

  // Animate bars on scroll
  animateBars();
}

function animateBars() {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        document.querySelectorAll('.skill-bar-fill').forEach(bar => {
          bar.style.width = bar.dataset.width + '%';
        });
        observer.disconnect();
      }
    });
  }, { threshold: 0.3 });
  const sec = document.getElementById('skills');
  if (sec) observer.observe(sec);
}

/* ===================== EDUCATION ===================== */
async function loadEducation() {
  const data = await apiFetch('/api/education');

  const container = document.getElementById('education-list');

  if (!container) return;

  if (!data || data.length === 0) {
    container.innerHTML =
      '<p style="color:#888">No education data yet.</p>';
    return;
  }

  container.innerHTML = data.map(e => `
  <div class="edu-item">
    <div class="edu-year">${e.period || ''}</div>
    <div class="edu-school">${e.school || ''}</div>
    <div class="edu-major">${e.major || ''}</div>
  </div>
`).join('');
}

/* ===================== EXPERIENCE ===================== */
async function loadExperience() {
  const data = await apiFetch('/api/experience');
  if (!data) return;

  if ($('exp-list')) {
    $('exp-list').innerHTML = data.length ? data.map(e => `
      <div class="exp-item">
        <div class="exp-period">${e.period || ''}</div>
        <div>
          <div class="exp-title">${e.title || ''}</div>
          <div class="exp-company">${e.company || ''}</div>
        </div>
        <div class="exp-desc">${e.description || ''}</div>
      </div>`).join('')
      : '<p style="color:#888;font-size:.85rem">No experience data yet.</p>';
  }
}

/* ===================== PROJECTS ===================== */
async function loadProjects() {
  const data = await apiFetch('/api/projects');
  if (!data) return;

  if ($('projects-grid')) {
    $('projects-grid').innerHTML = data.length ? data.slice(0, 6).map(p => `
      <div class="project-card">
        <img class="project-card-img" src="${p.image_url || 'https://via.placeholder.com/400x220?text=Project'}" alt="${p.name || 'Project'}"/>
        <div class="project-cat">${p.category || 'Project'}</div>
        <div class="project-name">${p.name || ''}</div>
        <div class="project-desc">${p.description || ''}</div>
        ${p.link ? `<a class="project-link" href="${p.link}" target="_blank">VIEW DETAIL →</a>` : ''}
      </div>`).join('')
      : '<p style="color:#888;font-size:.85rem">No projects data yet.</p>';
  }
}

/* ===================== CONTACT FORM ===================== */
function initContactForm() {
  const form = $('contact-form');
  if (!form) return;

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const btn = form.querySelector('.btn-submit');
    const msg = $('form-msg');
    btn.textContent = 'SENDING...';
    btn.disabled = true;

    const body = {
      name: form.name.value,
      email: form.email.value,
      message: form.message.value,
    };

    try {
      const res = await fetch(API + '/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
      const result = await res.json();
      if (res.ok) {
        msg.textContent = '✓ Pesan berhasil dikirim! Terima kasih.';
        msg.style.color = '#4caf50';
        form.reset();
      } else {
        msg.textContent = result.error || 'Gagal mengirim pesan.';
        msg.style.color = '#e53935';
      }
    } catch (err) {
      msg.textContent = 'Terjadi kesalahan. Coba lagi.';
      msg.style.color = '#e53935';
    }

    btn.textContent = 'SEND INQUIRY';
    btn.disabled = false;
    setTimeout(() => { msg.textContent = ''; }, 5000);
  });
}

/* ===================== NAV SCROLL ===================== */
function initNav() {
  window.addEventListener('scroll', () => {
    const nav = $('navbar');
    if (!nav) return;
    nav.style.boxShadow = window.scrollY > 40 ? '0 2px 16px rgba(0,0,0,.07)' : 'none';
  });

  // Mobile hamburger
  const ham = $('hamburger');
  const links = document.querySelector('.nav-links');
  if (ham && links) {
    ham.addEventListener('click', () => {
      links.style.display = links.style.display === 'flex' ? 'none' : 'flex';
      links.style.flexDirection = 'column';
      links.style.position = 'absolute';
      links.style.top = '60px';
      links.style.right = '0';
      links.style.background = '#F6F5F3';
      links.style.padding = '1rem 2rem';
      links.style.borderBottom = '1px solid #e0ddd8';
      links.style.width = '100%';
    });
  }
}

/* ===================== INIT ===================== */
document.addEventListener('DOMContentLoaded', () => {
  loadProfile();
  loadSkills();
  loadEducation();
  loadExperience();
  loadProjects();
  initContactForm();
  initNav();
});

// Keyboard shortcut: Ctrl+Shift+A → admin
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.shiftKey && e.key === 'A') {
    e.preventDefault();
    window.location.href = '/admin';
  }
});
