from flask import Blueprint, request, jsonify, session
from model import db, Experience
from functools import wraps

experience_bp = Blueprint('experience', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@experience_bp.route('/api/experience', methods=['GET'])
def get_experience():
    return jsonify([e.to_dict() for e in Experience.query.all()])

@experience_bp.route('/api/experience', methods=['POST'])
@require_login
def create_experience():
    d = request.get_json()
    e = Experience(title=d.get('title'), company=d.get('company'),
                   period=d.get('period'), description=d.get('description'))
    db.session.add(e); db.session.commit()
    return jsonify(e.to_dict()), 201

@experience_bp.route('/api/experience/<int:eid>', methods=['PUT'])
@require_login
def update_experience(eid):
    e = Experience.query.get_or_404(eid)
    d = request.get_json()
    for k, v in d.items():
        if hasattr(e, k): setattr(e, k, v)
    db.session.commit()
    return jsonify(e.to_dict())

@experience_bp.route('/api/experience/<int:eid>', methods=['DELETE'])
@require_login
def delete_experience(eid):
    e = Experience.query.get_or_404(eid)
    db.session.delete(e); db.session.commit()
    return jsonify({'message': 'Deleted'})
