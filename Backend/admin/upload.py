import os
import cloudinary
import cloudinary.uploader
from flask import Blueprint, request, jsonify, current_app

upload_bp = Blueprint('upload', __name__)

def init_cloudinary():
    cloudinary.config(
        cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key    = os.getenv('CLOUDINARY_API_KEY'),
        api_secret = os.getenv('CLOUDINARY_API_SECRET'),
        secure     = True
    )

@upload_bp.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file'}), 400
    file = request.files['file']
    if not file.filename:
        return jsonify({'error': 'Nama file kosong'}), 400

    init_cloudinary()
    try:
        result = cloudinary.uploader.upload(
            file,
            folder='portfolio',
            resource_type='image'
        )
        return jsonify({'url': result['secure_url'], 'public_id': result['public_id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
