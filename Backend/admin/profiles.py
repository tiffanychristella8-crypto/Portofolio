from flask import Blueprint, request, jsonify, session
from model import db, Profile
from functools import wraps

profiles_bp = Blueprint('profiles', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized - silakan login terlebih dahulu'}), 401
        return f(*args, **kwargs)
    return decorated

@profiles_bp.route('/api/profiles', methods=['GET'])
def get_profiles():
    return jsonify([p.to_dict() for p in Profile.query.all()])

@profiles_bp.route('/api/profiles', methods=['POST'])
@require_login
def create_profile():
    d = request.get_json()
    p = Profile(
        name=d.get('name'), tagline=d.get('tagline'),
        bio=d.get('bio'), about=d.get('about'),
        email=d.get('email'), location=d.get('location'),
        photo_url=d.get('photo_url'), years_exp=d.get('years_exp', 0),
        organizations=d.get('organizations', 0),
        projects_done=d.get('projects_done', 0),
        education=d.get('education'),
    )
    db.session.add(p); db.session.commit()
    return jsonify(p.to_dict()), 201

@profiles_bp.route('/api/profiles/<int:pid>', methods=['PUT'])
@require_login
def update_profile(pid):
    p = Profile.query.get_or_404(pid)
    d = request.get_json()
    for k, v in d.items():
        if hasattr(p, k): setattr(p, k, v)
    db.session.commit()
    return jsonify(p.to_dict())

@profiles_bp.route('/api/profiles/<int:pid>', methods=['DELETE'])
@require_login
def delete_profile(pid):
    p = Profile.query.get_or_404(pid)
    db.session.delete(p); db.session.commit()
    return jsonify({'message': 'Deleted'})
