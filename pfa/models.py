from pfa import db
import datetime

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    name=db.Column(db.String(30),nullable=False)
    password=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    phone=db.Column(db.integer(10),nullable=False)
    
    def __str__(self):
        return self.id
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    name=db.Column(db.String(30,nullable=True))
    
    def __str__(self):
        return self.id
    
    
class Transaction(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    amount=db.Column(db.Float,nullable=False)
    category=db.Column(db.Integer,nullable=False,foreign_key=Category.id)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    
    def __str__(self):
        return self.id
