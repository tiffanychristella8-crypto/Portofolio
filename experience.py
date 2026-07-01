import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'portofolio-secret-key-2024')
    
    # Session config - PENTING agar session bisa bekerja
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE   = False   # Set True jika pakai HTTPS
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = 86400  # 24 jam

    # TiDB (MySQL-compatible)
    TIDB_HOST     = os.getenv('TIDB_HOST')
    TIDB_PORT     = os.getenv('TIDB_PORT', '4000')
    TIDB_USER     = os.getenv('TIDB_USER')
    TIDB_PASSWORD = os.getenv('TIDB_PASSWORD')
    TIDB_DATABASE = os.getenv('TIDB_DATABASE', 'portofolio_db')

    # SSL cert path untuk TiDB
    _cert = os.path.join(os.path.dirname(__file__), 'certs', 'ca-cert.pem')
    _ssl_args = f"&ssl_ca={_cert}&ssl_verify_cert=true&ssl_verify_identity=true" if os.path.exists(_cert) else ""

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('TIDB_USER')}:{os.getenv('TIDB_PASSWORD')}"
        f"@{os.getenv('TIDB_HOST')}:{os.getenv('TIDB_PORT', '4000')}"
        f"/{os.getenv('TIDB_DATABASE', 'portofolio_db')}"
        f"?charset=utf8mb4{_ssl_args}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

    # Cloudinary
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY    = os.getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')

    # Resend (email)
    RESEND_API_KEY = os.getenv('RESEND_API_KEY')
    ADMIN_EMAIL    = os.getenv('ADMIN_EMAIL', 'tiffanychristella@gmail.com')
