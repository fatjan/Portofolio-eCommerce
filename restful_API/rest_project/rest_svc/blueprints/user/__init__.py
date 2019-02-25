import random, logging
from blueprints import db
from flask_restful import fields


class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type = db.Column(db.String(255), nullable=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    
    #unique=True kalau mau atribut nya unik, yang lain ga boleh ada yang sama

    response_field = {
        'id' : fields.Integer,
        'user_type' : fields.String,
        'username' : fields.String,
        'password' : fields.String,
        'address' : fields.String,
    }

    def __init__(self, id, user_type, username, password, address):
        self.id = id
        self.user_type = user_type
        self.username = username
        self.password = password
        self.address = address
       
    def __repr__(self): #initiate table model
        return '<User %r>' % self.id #the __repr__ must have a string type as return
  