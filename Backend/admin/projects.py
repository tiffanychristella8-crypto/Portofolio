from flask import Blueprint, request, jsonify, session
from model import db, Project
from functools import wraps

projects_bp = Blueprint('projects', __name__)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

@projects_bp.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify([p.to_dict() for p in Project.query.all()])

@projects_bp.route('/api/projects', methods=['POST'])
@require_login
def create_project():
    d = request.get_json()
    p = Project(name=d.get('name'), category=d.get('category'),
                description=d.get('description'), image_url=d.get('image_url'),
                link=d.get('link'))
    db.session.add(p); db.session.commit()
    return jsonify(p.to_dict()), 201

@projects_bp.route('/api/projects/<int:pid>', methods=['PUT'])
@require_login
def update_project(pid):
    p = Project.query.get_or_404(pid)
    d = request.get_json()
    for k, v in d.items():
        if hasattr(p, k): setattr(p, k, v)
    db.session.commit()
    return jsonify(p.to_dict())

@projects_bp.route('/api/projects/<int:pid>', methods=['DELETE'])
@require_login
def delete_project(pid):
    p = Project.query.get_or_404(pid)
    db.session.delete(p); db.session.commit()
    return jsonify({'message': 'Deleted'})
