from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(120))
    tagline       = db.Column(db.String(200))
    bio           = db.Column(db.Text)
    about         = db.Column(db.Text)
    email         = db.Column(db.String(120))
    location      = db.Column(db.String(120))
    photo_url     = db.Column(db.String(500))
    years_exp     = db.Column(db.Integer, default=0)
    organizations = db.Column(db.Integer, default=0)
    projects_done = db.Column(db.Integer, default=0)
    education     = db.Column(db.Text)   # stored as JSON string

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Skill(db.Model):
    __tablename__ = 'skills'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    type        = db.Column(db.String(20), default='technical')  # technical | professional
    level       = db.Column(db.Integer, default=80)
    description = db.Column(db.String(300))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Experience(db.Model):
    __tablename__ = 'experience'
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(120))
    company     = db.Column(db.String(120))
    period      = db.Column(db.String(80))
    description = db.Column(db.Text)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Project(db.Model):
    __tablename__ = 'projects'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(120))
    category    = db.Column(db.String(80))
    description = db.Column(db.Text)
    image_url   = db.Column(db.String(500))
    link        = db.Column(db.String(500))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Education(db.Model):
    __tablename__ = 'education'
    id     = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(80))
    school = db.Column(db.String(150))
    major  = db.Column(db.String(150))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Contact(db.Model):
    __tablename__ = 'contacts'
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(120))
    email      = db.Column(db.String(120))
    message    = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        d = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        d['created_at'] = self.created_at.isoformat() if self.created_at else None
        return d
