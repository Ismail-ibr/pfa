from pfa import app
from flask import render_template

@app.route("/")
def index():
    return render_template("login.html",title ='login')


@app.route("/layout")
def layout():
    return render_template("layout.html",title='layout')

