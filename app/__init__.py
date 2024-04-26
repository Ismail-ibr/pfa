from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/pfa'
app.config['SECRET_KEY']='b$12$fs9E/RQW1s8X0jPDPIwjBuKmX85DIDTvsuE0T.EJ1GuHkFqteWAnC'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

#from app.models import Users,Transaction,Category
#migrate=Migrate(app,db)


from app import routes