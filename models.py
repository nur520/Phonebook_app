from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

# set variables for class instantiation
login_maager = LoginManager()
ma = Marshmallow()
db = SQLALchemy()

@login_maager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Colum(db.String, primay_key = True)
    first_name =db.Colum(db.String(150),nullable = True,default = '')
    last_name = db.Colum(db.String(150),nullable = True,default = '')
    email = db.Colum(db.String(150),nullable = False)
    password = db.Colum(db.String, nullable = True,default = '')
    g_auth_verify = db.Colum(db.Boolean, default = False)
    token = db.Colum(db.String, default = '', unique = True)
    date_created = db.Colum(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name = '', last_name = '',password = '',token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.firs_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify


    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User{self.emal} has been added to the database'
    
class Contact(db.Model):
    id = db.Colum(db.String, primary_key = True)
    name = db.Colum(db.String(150), nullable = False)
    email = db.Colum(db.String(200))
    phone_number = db.Colum(db.String(20))
    address = db.Colum(db.String(200))
    user_token = db.Colum(db.String, db.ForeignKey('user.token'), nullable = False)


    def __init__(self, name, address, email,phone_number, user_token,id = ''):
        self_id = self.set_id()
        self.name = name
        self.email = email
        self.address = address
        self.user_token = user_token
        self.phone_number = phone_number
        

    def __repr__(self):
            return f'The following contact has been added to the phonebook: {self.name}'

    def set_id(self):
            return(secrets.token_urlsafe())
    
class ContactSchema(ma.Schema):
    class Meta:
        ffields = ['id', 'name', 'phone_number, email, address']

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many = True)

    









