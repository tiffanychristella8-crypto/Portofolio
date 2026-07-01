/* ============================================================
   dashboard.js — Full CRUD for Portfolio Admin
   ============================================================ */

/* -------- utils -------- */
const $  = id => document.getElementById(id);
const qs = sel => document.querySelector(sel);

function showToast(msg, type = 'success') {
  const t = $('toast');
  t.textContent = msg;
  t.className = `toast ${type} show`;
  setTimeout(() => { t.className = 'toast'; }, 3000);
}

function openModal(id) { $(id).classList.add('open'); }
function closeModal(id) { $(id).classList.remove('open'); }

document.querySelectorAll('[data-close]').forEach(btn => {
  btn.addEventListener('click', () => closeModal(btn.dataset.close));
});
document.querySelectorAll('.modal-overlay').forEach(m => {
  m.addEventListener('click', e => { if (e.target === m) closeModal(m.id); });
});

/* -------- NAV -------- */
const pages = ['dashboard','profiles','skills','education','experience','projects','contacts'];

document.querySelectorAll('.sidebar-nav a[data-page]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const page = link.dataset.page;
    document.querySelectorAll('.sidebar-nav a').forEach(a => a.classList.remove('active'));
    link.classList.add('active');
    pages.forEach(p => {
      const el = $(`page-${p}`);
      if (el) el.classList.toggle('active', p === page);
    });
    $('topbar-title').textContent = link.textContent.trim().replace(/^./, '').trim();
    loaders[page] && loaders[page]();
  });
});

$('logout-btn').addEventListener('click', e => {
  e.preventDefault();
  fetch('/api/logout', { method: 'POST', credentials: 'include' })
    .finally(() => { window.location.href = '/admin'; });
});

/* ============================================================
   PROFILES
   ============================================================ */
async function loadProfiles() {
  try {
    const data = await apiGet('/api/profiles');
    if (!data) return;
    const tb = $('profiles-table');
    tb.innerHTML = data.length ? data.map(p => `
      <tr>
        <td><img class="td-img" src="${p.photo_url || 'https://via.placeholder.com/50x40?text=N/A'}" alt=""/></td>
        <td>${p.name || ''}</td>
        <td>${p.tagline || ''}</td>
        <td>${p.email || ''}</td>
        <td>${p.location || ''}</td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editProfile(${JSON.stringify(p).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteProfile(${p.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="6" style="color:#aaa;text-align:center;padding:2rem">Belum ada data profil</td></tr>';
  } catch(e) { showToast('Gagal memuat profil', 'error'); }
}

$('btn-add-profile').addEventListener('click', () => {
  $('modal-profile-title').textContent = 'Tambah Profile';
  ['p-id','p-name','p-tagline','p-bio','p-about','p-email','p-location','p-years','p-orgs','p-proj','p-photo-url','p-education']
    .forEach(id => { const el = $(id); if(el) el.value = ''; });
  $('p-photo-preview').style.display = 'none';
  openModal('modal-profile');
});

window.editProfile = p => {
  $('modal-profile-title').textContent = 'Edit Profile';
  $('p-id').value = p.id || '';
  $('p-name').value = p.name || '';
  $('p-tagline').value = p.tagline || '';
  $('p-bio').value = p.bio || '';
  $('p-about').value = p.about || '';
  $('p-email').value = p.email || '';
  $('p-location').value = p.location || '';
  $('p-years').value = p.years_exp || '';
  $('p-orgs').value = p.organizations || '';
  $('p-proj').value = p.projects_done || '';
  $('p-photo-url').value = p.photo_url || '';
  $('p-education').value = p.education || '';
  const prev = $('p-photo-preview');
  if (p.photo_url) { prev.src = p.photo_url; prev.style.display = 'block'; }
  else { prev.style.display = 'none'; }
  openModal('modal-profile');
};

$('p-photo-file').addEventListener('change', async e => {
  const file = e.target.files[0];
  if (!file) return;
  try {
    showToast('Mengupload foto...');
    const url = await uploadImage(file);
    if (!url) return;
    $('p-photo-url').value = url;
    const prev = $('p-photo-preview');
    prev.src = url; prev.style.display = 'block';
    showToast('Foto berhasil diupload ke Cloudinary ✓');
  } catch { showToast('Gagal upload foto', 'error'); }
});

$('save-profile').addEventListener('click', async () => {
  const id = $('p-id').value;
  const body = {
    name: $('p-name').value, tagline: $('p-tagline').value,
    bio: $('p-bio').value, about: $('p-about').value,
    email: $('p-email').value, location: $('p-location').value,
    years_exp: $('p-years').value, organizations: $('p-orgs').value,
    projects_done: $('p-proj').value, photo_url: $('p-photo-url').value,
    education: $('p-education').value,
  };
  try {
    if (id) { await apiPut(`/api/profiles/${id}`, body); showToast('Profile diperbarui ✓'); }
    else { await apiPost('/api/profiles', body); showToast('Profile ditambahkan ✓'); }
    closeModal('modal-profile'); loadProfiles();
  } catch { showToast('Gagal menyimpan', 'error'); }
});

window.deleteProfile = async id => {
  if (!confirm('Hapus profile ini?')) return;
  try { await apiDelete(`/api/profiles/${id}`); showToast('Dihapus ✓'); loadProfiles(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   SKILLS
   ============================================================ */
async function loadSkills() {
  try {
    const data = await apiGet('/api/skills');
    if (!data) return;
    $('stat-skills').textContent = data.length;

    const techSkills = data.filter(s => s.type === 'technical');
    const proSkills  = data.filter(s => s.type === 'professional');

    const tbTech = $('skills-tech-table');
    tbTech.innerHTML = techSkills.length ? techSkills.map(s => `
      <tr>
        <td><strong>${s.name}</strong></td>
        <td>
          <div class="skill-bar-wrap">
            <div class="skill-bar"><div class="skill-bar-fill" style="width:${s.level}%"></div></div>
            <span class="skill-pct">${s.level}%</span>
          </div>
        </td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editSkill(${JSON.stringify(s).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteSkill(${s.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="3" style="color:#aaa;text-align:center;padding:1.5rem">Belum ada technical skill</td></tr>';

    const tbPro = $('skills-pro-table');
    tbPro.innerHTML = proSkills.length ? proSkills.map(s => `
      <tr>
        <td><strong>${s.name}</strong></td>
        <td style="color:var(--ink-light);font-size:0.82rem">${s.description || '—'}</td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editSkill(${JSON.stringify(s).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteSkill(${s.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="3" style="color:#aaa;text-align:center;padding:1.5rem">Belum ada professional skill</td></tr>';

  } catch { showToast('Gagal memuat skills', 'error'); }
}

$('btn-add-skill').addEventListener('click', () => {
  $('modal-skill-title').textContent = 'Tambah Skill';
  $('s-id').value = ''; $('s-name').value = '';
  $('s-type').value = 'technical'; $('s-level').value = 80;
  $('s-level-val').textContent = '80%'; $('s-desc').value = '';
  openModal('modal-skill');
});

window.editSkill = s => {
  $('modal-skill-title').textContent = 'Edit Skill';
  $('s-id').value = s.id; $('s-name').value = s.name;
  $('s-type').value = s.type; $('s-level').value = s.level || 80;
  $('s-level-val').textContent = (s.level || 80) + '%';
  $('s-desc').value = s.description || '';
  openModal('modal-skill');
};

$('save-skill').addEventListener('click', async () => {
  const id = $('s-id').value;
  const body = { name: $('s-name').value, type: $('s-type').value, level: $('s-level').value, description: $('s-desc').value };
  try {
    if (id) { await apiPut(`/api/skills/${id}`, body); showToast('Skill diperbarui ✓'); }
    else { await apiPost('/api/skills', body); showToast('Skill ditambahkan ✓'); }
    closeModal('modal-skill'); loadSkills();
  } catch { showToast('Gagal menyimpan', 'error'); }
});

window.deleteSkill = async id => {
  if (!confirm('Hapus skill ini?')) return;
  try { await apiDelete(`/api/skills/${id}`); showToast('Dihapus ✓'); loadSkills(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   EXPERIENCE
   ============================================================ */
async function loadExperience() {
  try {
    const data = await apiGet('/api/experience');
    if (!data) return;
    $('stat-exp').textContent = data.length;
    const tb = $('exp-table');
    tb.innerHTML = data.length ? data.map(e => `
      <tr>
        <td>${e.title || ''}</td>
        <td>${e.company || ''}</td>
        <td>${e.period || ''}</td>
        <td>${(e.description||'').substring(0,80)}${e.description&&e.description.length>80?'...':''}</td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editExp(${JSON.stringify(e).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteExp(${e.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="5" style="color:#aaa;text-align:center;padding:2rem">Belum ada data pengalaman</td></tr>';
  } catch { showToast('Gagal memuat experience', 'error'); }
}

$('btn-add-exp').addEventListener('click', () => {
  $('modal-exp-title').textContent = 'Tambah Pengalaman';
  ['e-id','e-title','e-company','e-period','e-desc'].forEach(id => { const el=$(id); if(el) el.value=''; });
  openModal('modal-exp');
});

window.editExp = e => {
  $('modal-exp-title').textContent = 'Edit Pengalaman';
  $('e-id').value = e.id; $('e-title').value = e.title || '';
  $('e-company').value = e.company || ''; $('e-period').value = e.period || '';
  $('e-desc').value = e.description || '';
  openModal('modal-exp');
};

$('save-exp').addEventListener('click', async () => {
  const id = $('e-id').value;
  const body = { title: $('e-title').value, company: $('e-company').value, period: $('e-period').value, description: $('e-desc').value };
  try {
    if (id) { await apiPut(`/api/experience/${id}`, body); showToast('Pengalaman diperbarui ✓'); }
    else { await apiPost('/api/experience', body); showToast('Pengalaman ditambahkan ✓'); }
    closeModal('modal-exp'); loadExperience();
  } catch { showToast('Gagal menyimpan', 'error'); }
});

window.deleteExp = async id => {
  if (!confirm('Hapus pengalaman ini?')) return;
  try { await apiDelete(`/api/experience/${id}`); showToast('Dihapus ✓'); loadExperience(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   PROJECTS
   ============================================================ */
async function loadProjects() {
  try {
    const data = await apiGet('/api/projects');
    if (!data) return;
    $('stat-projects').textContent = data.length;
    const tb = $('projects-table');
    tb.innerHTML = data.length ? data.map(p => `
      <tr>
        <td><img class="td-img" src="${p.image_url || 'https://via.placeholder.com/50x40?text=N/A'}" alt=""/></td>
        <td>${p.name || ''}</td>
        <td>${p.category || ''}</td>
        <td>${(p.description||'').substring(0,60)}${p.description&&p.description.length>60?'...':''}</td>
        <td>${p.link ? `<a href="${p.link}" target="_blank" style="color:var(--accent)">↗</a>` : '—'}</td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editProject(${JSON.stringify(p).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteProject(${p.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="6" style="color:#aaa;text-align:center;padding:2rem">Belum ada data proyek</td></tr>';
  } catch { showToast('Gagal memuat proyek', 'error'); }
}

$('btn-add-project').addEventListener('click', () => {
  $('modal-project-title').textContent = 'Tambah Proyek';
  ['pr-id','pr-name','pr-category','pr-desc','pr-link','pr-image-url'].forEach(id => { const el=$(id); if(el) el.value=''; });
  $('pr-img-preview').style.display = 'none';
  openModal('modal-project');
});

window.editProject = p => {
  $('modal-project-title').textContent = 'Edit Proyek';
  $('pr-id').value = p.id; $('pr-name').value = p.name || '';
  $('pr-category').value = p.category || ''; $('pr-desc').value = p.description || '';
  $('pr-link').value = p.link || ''; $('pr-image-url').value = p.image_url || '';
  const prev = $('pr-img-preview');
  if (p.image_url) { prev.src = p.image_url; prev.style.display = 'block'; }
  else { prev.style.display = 'none'; }
  openModal('modal-project');
};

$('pr-img-file').addEventListener('change', async e => {
  const file = e.target.files[0];
  if (!file) return;
  try {
    showToast('Mengupload gambar...');
    const url = await uploadImage(file);
    if (!url) return;
    $('pr-image-url').value = url;
    const prev = $('pr-img-preview');
    prev.src = url; prev.style.display = 'block';
    showToast('Gambar berhasil diupload ke Cloudinary ✓');
  } catch { showToast('Gagal upload gambar', 'error'); }
});

$('save-project').addEventListener('click', async () => {
  const id = $('pr-id').value;
  const body = { name: $('pr-name').value, category: $('pr-category').value, description: $('pr-desc').value, link: $('pr-link').value, image_url: $('pr-image-url').value };
  try {
    if (id) { await apiPut(`/api/projects/${id}`, body); showToast('Proyek diperbarui ✓'); }
    else { await apiPost('/api/projects', body); showToast('Proyek ditambahkan ✓'); }
    closeModal('modal-project'); loadProjects();
  } catch { showToast('Gagal menyimpan', 'error'); }
});

window.deleteProject = async id => {
  if (!confirm('Hapus proyek ini?')) return;
  try { await apiDelete(`/api/projects/${id}`); showToast('Dihapus ✓'); loadProjects(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   CONTACTS (read + delete only)
   ============================================================ */
async function loadContacts() {
  try {
    const data = await apiGet('/api/contacts');
    if (!data) return;
    $('stat-messages').textContent = data.length;
    const tb = $('contacts-table');
    tb.innerHTML = data.length ? data.map(c => `
      <tr>
        <td>${c.name || ''}</td>
        <td>${c.email || ''}</td>
        <td>${(c.message||'').substring(0,80)}${c.message&&c.message.length>80?'...':''}</td>
        <td>${c.created_at ? new Date(c.created_at).toLocaleString('id-ID') : '—'}</td>
        <td><div class="td-actions">
          <button class="btn-del" onclick="deleteContact(${c.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="5" style="color:#aaa;text-align:center;padding:2rem">Belum ada pesan masuk</td></tr>';
  } catch { showToast('Gagal memuat pesan', 'error'); }
}

window.deleteContact = async id => {
  if (!confirm('Hapus pesan ini?')) return;
  try { await apiDelete(`/api/contacts/${id}`); showToast('Dihapus ✓'); loadContacts(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   EDUCATION
   ============================================================ */
async function loadEducation() {
  try {
    const data = await apiGet('/api/education');
    if (!data) return;
    const tb = $('edu-table');
    tb.innerHTML = data.length ? data.map(e => `
      <tr>
        <td><span style="font-size:0.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)">${e.period || ''}</span></td>
        <td><strong>${e.school || ''}</strong></td>
        <td>${e.major || '—'}</td>
        <td><div class="td-actions">
          <button class="btn-edit" onclick="editEdu(${JSON.stringify(e).replace(/"/g,'&quot;')})">Edit</button>
          <button class="btn-del" onclick="deleteEdu(${e.id})">Hapus</button>
        </div></td>
      </tr>`).join('')
      : '<tr><td colspan="4" style="color:#aaa;text-align:center;padding:2rem">Belum ada data pendidikan</td></tr>';
  } catch { showToast('Gagal memuat education', 'error'); }
}

$('btn-add-edu').addEventListener('click', () => {
  $('modal-edu-title').textContent = 'Tambah Pendidikan';
  ['ed-id','ed-period','ed-school','ed-major'].forEach(id => { const el=$(id); if(el) el.value=''; });
  openModal('modal-edu');
});

window.editEdu = e => {
  $('modal-edu-title').textContent = 'Edit Pendidikan';
  $('ed-id').value = e.id;
  $('ed-period').value = e.period || '';
  $('ed-school').value = e.school || '';
  $('ed-major').value = e.major || '';
  openModal('modal-edu');
};

$('save-edu').addEventListener('click', async () => {
  const id = $('ed-id').value;
  const body = { period: $('ed-period').value, school: $('ed-school').value, major: $('ed-major').value };
  try {
    if (id) { await apiPut(`/api/education/${id}`, body); showToast('Pendidikan diperbarui ✓'); }
    else { await apiPost('/api/education', body); showToast('Pendidikan ditambahkan ✓'); }
    closeModal('modal-edu'); loadEducation();
  } catch { showToast('Gagal menyimpan', 'error'); }
});

window.deleteEdu = async id => {
  if (!confirm('Hapus data pendidikan ini?')) return;
  try { await apiDelete(`/api/education/${id}`); showToast('Dihapus ✓'); loadEducation(); }
  catch { showToast('Gagal menghapus', 'error'); }
};

/* ============================================================
   LOAD DASHBOARD STATS
   ============================================================ */
async function loadDashboardStats() {
  try {
    const data = await apiGet('/api/stats');
    if (!data) return;
    if ($('stat-skills')) $('stat-skills').textContent = data.skills;
    if ($('stat-exp')) $('stat-exp').textContent = data.experience;
    if ($('stat-projects')) $('stat-projects').textContent = data.projects;
    if ($('stat-messages')) $('stat-messages').textContent = data.contacts;
    // Education count — fetch separately
    const eduData = await apiGet('/api/education');
    if (eduData && $('stat-edu')) $('stat-edu').textContent = eduData.length;
  } catch {}
}

/* ============================================================
   INIT
   ============================================================ */
const loaders = {
  dashboard: () => { loadDashboardStats(); loadContacts(); },
  profiles: loadProfiles,
  skills: loadSkills,
  education: loadEducation,
  experience: loadExperience,
  projects: loadProjects,
  contacts: loadContacts,
};

// Guard: cek login dulu baru load data
(async () => {
  const user = await requireAuth();
  if (!user) return;
  // Tampilkan nama user di topbar
  if ($('admin-username')) $('admin-username').textContent = user.username;
  // Load halaman dashboard pertama kali
  loadDashboardStats();
  loadContacts();
})();
