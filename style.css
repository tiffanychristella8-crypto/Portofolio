/* api.js — centralized fetch helper for Admin */
const BASE = '';  // same origin

async function apiGet(path) {
  const res = await fetch(BASE + path, { credentials: 'include' });
  if (res.status === 401) { window.location.href = '/admin'; return null; }
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

async function apiPost(path, body) {
  const res = await fetch(BASE + path, {
    method: 'POST', credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (res.status === 401) { window.location.href = '/admin'; return null; }
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

async function apiPut(path, body) {
  const res = await fetch(BASE + path, {
    method: 'PUT', credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (res.status === 401) { window.location.href = '/admin'; return null; }
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

async function apiDelete(path) {
  const res = await fetch(BASE + path, { method: 'DELETE', credentials: 'include' });
  if (res.status === 401) { window.location.href = '/admin'; return null; }
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

/* Upload file ke Cloudinary via backend proxy */
async function uploadImage(file) {
  const fd = new FormData();
  fd.append('file', file);
  const res = await fetch(BASE + '/api/upload', {
    method: 'POST', credentials: 'include', body: fd,
  });
  if (res.status === 401) { window.location.href = '/admin'; return null; }
  if (!res.ok) throw new Error('Upload gagal');
  const data = await res.json();
  return data.url;
}

/* Check auth on every page load of dashboard */
async function requireAuth() {
  try {
    const res = await fetch('/api/me', { credentials: 'include' });
    if (!res.ok) {
      window.location.href = '/admin';
      return null;
    }
    return await res.json();
  } catch {
    window.location.href = '/admin';
    return null;
  }
}
