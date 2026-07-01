document.addEventListener('DOMContentLoaded', () => {
  // If already logged in, redirect to dashboard
  fetch('/api/me', { credentials: 'include' })
    .then(res => { if (res.ok) window.location.href = '/admin/dashboard'; })
    .catch(() => {});
});

document.getElementById('login-form').addEventListener('submit', async e => {
  e.preventDefault();
  const err = document.getElementById('login-error');
  const btn = e.target.querySelector('.btn-login');
  btn.textContent = 'MEMUAT...';
  btn.disabled = true;
  err.textContent = '';

  const body = {
    username: document.getElementById('username').value.trim(),
    password: document.getElementById('password').value,
  };

  try {
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(body),
    });
    const data = await res.json();
    if (res.ok) {
      window.location.href = '/admin/dashboard';
    } else {
      err.textContent = data.error || 'Username atau password salah.';
    }
  } catch {
    err.textContent = 'Tidak dapat terhubung ke server.';
  }
  btn.textContent = 'MASUK';
  btn.disabled = false;
});
