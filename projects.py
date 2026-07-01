from flask import Blueprint, request, jsonify, session
from model import User
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Data tidak valid'}), 400
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'error': 'Username dan password wajib diisi'}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session.permanent = True
        session['user_id']  = user.id
        session['username'] = user.username
        return jsonify({'message': 'Login berhasil', 'username': user.username})
    
    return jsonify({'error': 'Username atau password salah'}), 401


@login_bp.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout berhasil'})


@login_bp.route('/api/me', methods=['GET'])
def me():
    if session.get('user_id'):
        return jsonify({'id': session['user_id'], 'username': session['username']})
    return jsonify({'error': 'Belum login'}), 401
