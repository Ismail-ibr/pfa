from app import db
import datetime
from flask_login import UserMixin


class Users(db.Model):
    idU=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(10),nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    phone=db.Column(db.Integer,unique=True,nullable=False)
    balance=db.Column(db.Float,nullable=False,default=0.0)
    transactions=db.relationship('Transaction',backref='user',lazy=True)
    def __str__(self):
        return str(self.idU),str(self.name),str(self.password),str(self.email),str(self.phone)
    def get_id(self):
        return str(self.idU) 
    @property
    def is_active(self):
        return True
    def get_name(self):
        return self.name
class Category(db.Model):
    idC=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=True)
    transactions=db.relationship('Transaction',backref='category',lazy=True) 
    def __str__(self):
        return str(self.idC),str(self.name)
    def get_id(self):
        return self.idC
    def get_name(self):
        return self.name
class Transaction(db.Model):
    idT=db.Column(db.Integer,primary_key=True)
    amount=db.Column(db.Float,nullable=False)
    idC=db.Column(db.Integer,db.ForeignKey('category.idC'),nullable=False)
    idU=db.Column(db.Integer,db.ForeignKey('users.idU'),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.idT),str(self.amount),self.category,self.user,str(self.date)
    def get_id(self):
        return self.idT
    def get_amount(self):
        return self.amount
    def get_cat(self):
        categ=Category.query.filter_by(idC=self.idC).first()
        return categ.get_name()
    def get_date(self):
        return self.date
    @property
    def is_active(self):
        return True