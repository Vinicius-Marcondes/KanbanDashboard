# Python
from datetime import datetime

# Apps
from apps.db import db


class Roles(db.Model):
    """
    Roles permissions
    """
    role_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10))
    user_id = db.relationship('UserMixin', backref='roles')


class UserMixin(db.Model):
    """
    Default structure for any user
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow())

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.roles.admin


class User(UserMixin):
    full_name = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
