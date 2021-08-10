from TaskManager import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    emailAddress = db.Column(db.String(length=50), nullable=False, unique=True)
    passwordHash = db.Column(db.String(length=60), nullable=False)
    Todos = db.relationship('Todo', backref='owned_user', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id