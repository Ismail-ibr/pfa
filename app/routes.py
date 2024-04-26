from app import app
from flask import render_template
from app.form import UserInputForm

@app.route("/")
def homepage():
    form=UserInputForm()
    return render_template("homepage.html",title ='Home page',form=form)


@app.route("/layout")
def layout():
    return render_template("layout.html",title='layout')
    