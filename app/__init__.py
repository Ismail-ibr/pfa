from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='b$12$fs9E/RQW1s8X0jPDPIwjBuKmX85DIDTvsuE0T.EJ1GuHkFqteWAnC'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/pfa'
app.config['SQLACLHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from app.models import Users,Transaction,Category
migrate=Migrate(app,db)

login_manager= LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

from app import routes