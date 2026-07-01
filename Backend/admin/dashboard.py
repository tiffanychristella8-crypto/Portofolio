import os
import requests
from flask import Blueprint, request, jsonify, session
from model import db, Contact
from functools import wraps

dashboard_bp = Blueprint('dashboard', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@dashboard_bp.route('/api/stats', methods=['GET'])
@require_login
def get_stats():
    """Dashboard summary stats for admin."""
    from model import Profile, Skill, Experience, Project
    return jsonify({
        'profiles'   : Profile.query.count(),
        'skills'     : Skill.query.count(),
        'experience' : Experience.query.count(),
        'projects'   : Project.query.count(),
        'contacts'   : Contact.query.count(),
    })

@dashboard_bp.route('/api/contacts', methods=['GET'])
@require_login
def get_contacts():
    return jsonify([c.to_dict() for c in Contact.query.order_by(Contact.created_at.desc()).all()])

@dashboard_bp.route('/api/contact', methods=['POST'])
def submit_contact():
    """Public endpoint: visitor submits contact form."""
    d = request.get_json()
    name    = d.get('name', '').strip()
    email   = d.get('email', '').strip()
    message = d.get('message', '').strip()

    if not all([name, email, message]):
        return jsonify({'error': 'Semua field wajib diisi'}), 400

    contact = Contact(name=name, email=email, message=message)
    db.session.add(contact)
    db.session.commit()

    # Send email via Resend (optional)
    resend_key  = os.getenv('RESEND_API_KEY')
    admin_email = os.getenv('ADMIN_EMAIL', 'tiffanychristella@gmail.com')

    if resend_key:
        try:
            payload = {
                "from": "Portfolio Contact <onboarding@resend.dev>",
                "to": [admin_email],
                "subject": f"Pesan baru dari {name}",
                "html": f"""
                <h2>Pesan Baru dari Portfolio</h2>
                <p><strong>Nama:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Pesan:</strong></p>
                <p>{message}</p>
                """
            }
            headers = {
                "Authorization": f"Bearer {resend_key}",
                "Content-Type": "application/json"
            }
            res = requests.post("https://api.resend.com/emails", json=payload, headers=headers, timeout=10)
            if res.status_code not in (200, 201):
                print(f"Resend error: {res.text}")
        except Exception as e:
            print(f"Email error: {e}")

    return jsonify({'message': 'Pesan berhasil dikirim!'})

@dashboard_bp.route('/api/contacts/<int:cid>', methods=['DELETE'])
@require_login
def delete_contact(cid):
    c = Contact.query.get_or_404(cid)
    db.session.delete(c); db.session.commit()
    return jsonify({'message': 'Deleted'})
