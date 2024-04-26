from app import db
import datetime


class Users(db.Model):
    idU=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    phone=db.Column(db.Integer,unique=True,nullable=False)
    transactions=db.relationship('Transaction',backref='user',lazy=True)
    def __str__(self):
        return str(self.idU)

class Category(db.Model):
    idC=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=True)
    transactions=db.relationship('Transaction',backref='category',lazy=True)
    
    def __str__(self):
        return str(self.idC)
    
    
class Transaction(db.Model):
    idT=db.Column(db.Integer,primary_key=True)
    amount=db.Column(db.Float,nullable=False)
    category=db.Column(db.Integer,db.ForeignKey('category.idC'),nullable=False)
    user=db.Column(db.Integer,db.ForeignKey('users.idU'),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.idT)

