from flask import Blueprint, request, jsonify, session
from model import db, Skill
from functools import wraps

skills_bp = Blueprint('skills', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@skills_bp.route('/api/skills', methods=['GET'])
def get_skills():
    return jsonify([s.to_dict() for s in Skill.query.all()])

@skills_bp.route('/api/skills', methods=['POST'])
@require_login
def create_skill():
    d = request.get_json()
    s = Skill(name=d.get('name'), type=d.get('type','technical'),
              level=d.get('level', 80), description=d.get('description'))
    db.session.add(s); db.session.commit()
    return jsonify(s.to_dict()), 201

@skills_bp.route('/api/skills/<int:sid>', methods=['PUT'])
@require_login
def update_skill(sid):
    s = Skill.query.get_or_404(sid)
    d = request.get_json()
    for k, v in d.items():
        if hasattr(s, k): setattr(s, k, v)
    db.session.commit()
    return jsonify(s.to_dict())

@skills_bp.route('/api/skills/<int:sid>', methods=['DELETE'])
@require_login
def delete_skill(sid):
    s = Skill.query.get_or_404(sid)
    db.session.delete(s); db.session.commit()
    return jsonify({'message': 'Deleted'})
