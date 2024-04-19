from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pfaDB.db'
app.config['SECRET_KEY']='1234'
db=SQLAlchemy(app)
from pfa import routes


