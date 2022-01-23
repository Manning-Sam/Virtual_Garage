from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from flask_login import LoginManager
from flask_login import UserMixin

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Secrets Module (Given by Python)
import secrets

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(150), nullable = True, default='')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    
    # drone = db.relationship('Drone', backref = 'owner', lazy = True)

    def __init__(self,username = '',email='', password = ''):
        self.id = self.set_id()
        self.username = username
        self.email = email
        self.password = self.set_password(password)
        
        

    def set_token(self,length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(150), nullable = True, default='')
    model = db.Column(db.String(150), nullable = True, default = '')
    year = db.Column(db.String(4), nullable = True, default = '')
    color = db.Column(db.String(150), nullable = True, default='')
    image = db.Column(db.String(500),nullable = True, default = '')
    created_by = db.Column(db.String)

    def __init__(self,year = '',make='',model = '',color='', id = ''):
        self.id = self.set_id()
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        

    def set_id(self):
        return str(uuid.uuid4())


    
