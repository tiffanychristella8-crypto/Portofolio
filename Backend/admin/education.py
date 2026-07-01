from flask import Blueprint, request, jsonify, session
from model import db, Education
from functools import wraps

education_bp = Blueprint('education', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@education_bp.route('/api/education', methods=['GET'])
def get_education():
    return jsonify([e.to_dict() for e in Education.query.all()])

@education_bp.route('/api/education', methods=['POST'])
@require_login
def create_education():
    d = request.get_json()
    e = Education(period=d.get('period'), school=d.get('school'), major=d.get('major'))
    db.session.add(e); db.session.commit()
    return jsonify(e.to_dict()), 201

@education_bp.route('/api/education/<int:eid>', methods=['PUT'])
@require_login
def update_education(eid):
    e = Education.query.get_or_404(eid)
    d = request.get_json()
    for k, v in d.items():
        if hasattr(e, k): setattr(e, k, v)
    db.session.commit()
    return jsonify(e.to_dict())

@education_bp.route('/api/education/<int:eid>', methods=['DELETE'])
@require_login
def delete_education(eid):
    e = Education.query.get_or_404(eid)
    db.session.delete(e); db.session.commit()
    return jsonify({'message': 'Deleted'})
