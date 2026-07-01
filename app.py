from flask import Flask, send_from_directory, jsonify, session
from config import Config
from model import db
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_UTAMA = os.path.join(BASE_DIR, "Frontend", "utama")
FRONTEND_ADMIN = os.path.join(BASE_DIR, "Frontend", "admin")


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    db.init_app(app)

    # Register blueprints
    from Backend.utama.utama import utama_bp
    from Backend.admin.profiles import profiles_bp
    from Backend.admin.skills import skills_bp
    from Backend.admin.experience import experience_bp
    from Backend.admin.projects import projects_bp
    from Backend.admin.login import login_bp
    from Backend.admin.upload import upload_bp
    from Backend.admin.dashboard import dashboard_bp
    from Backend.admin.education import education_bp

    app.register_blueprint(utama_bp)
    app.register_blueprint(profiles_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(education_bp)

    # Main frontend
    @app.route("/")
    def index():
        return send_from_directory(FRONTEND_UTAMA, "index.html")

    @app.route("/css/<path:filename>")
    def serve_utama_css(filename):
        return send_from_directory(os.path.join(FRONTEND_UTAMA, "css"), filename)

    @app.route("/js/<path:filename>")
    def serve_utama_js(filename):
        return send_from_directory(os.path.join(FRONTEND_UTAMA, "js"), filename)

    @app.route("/assets/<path:filename>")
    def serve_utama_assets(filename):
        return send_from_directory(FRONTEND_UTAMA, filename)

    @app.route("/tiff.jpg")
    def serve_profile_image():
        return send_from_directory(FRONTEND_UTAMA, "tiff.jpg")

    # Admin frontend
    @app.route("/admin")
    @app.route("/admin/")
    def admin_login():
        return send_from_directory(FRONTEND_ADMIN, "login.html")

    @app.route("/admin/dashboard")
    def admin_dashboard():
        return send_from_directory(FRONTEND_ADMIN, "dashboard.html")

    @app.route("/admin/css/<path:filename>")
    def serve_admin_css(filename):
        return send_from_directory(os.path.join(FRONTEND_ADMIN, "css"), filename)

    @app.route("/admin/js/<path:filename>")
    def serve_admin_js(filename):
        return send_from_directory(os.path.join(FRONTEND_ADMIN, "js"), filename)

    # Session check endpoint
    @app.route("/api/me")
    def me():
        if session.get("user_id"):
            return jsonify({
                "username": session.get("username"),
                "id": session.get("user_id")
            })
        return jsonify({"error": "Unauthorized"}), 401

    with app.app_context():
        try:
            db.create_all()
            _seed_admin()
            print("Database connected and ready!")
        except Exception as e:
            print(f"Database connection failed: {e}")
            print("App running in offline mode - API endpoints may fail")

    return app


def _seed_admin():
    """Create default admin user if none exists."""
    try:
        from model import User
        from werkzeug.security import generate_password_hash

        if not User.query.first():
            admin = User(
                username="admin",
                password=generate_password_hash("admin123")
            )
            db.session.add(admin)
            db.session.commit()
            print("Default admin created: admin / admin123")
    except Exception as e:
        print(f"Seed admin failed: {e}")


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5000)