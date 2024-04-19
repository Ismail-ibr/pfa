from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

from pfa import app

@app.route("/login",methods=['GET','POST']) 
def login():
    if request.method=='POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'



def do_the_login():
    print(url_for('static',filename='index.html'))
 
def show_the_login_form():
    return render_template('index.html')


