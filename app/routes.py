from app import app,db
from flask import render_template,redirect,url_for,flash,session
from flask_login import login_user,logout_user,current_user
from app.form import SignUpForm,LoginForm,AddTransactionForm
from app.models import Users,Transaction,Category

@app.route("/",methods=['GET','POST'])
def homepage():
    form=SignUpForm()
    login=LoginForm()
    if form.validate_on_submit() and form.submit.data:
        name=form.name.data
        email=form.email.data
        phone=form.phonenumber.data
        passw=form.password.data
        user=Users(name=name,email=email,phone=phone,password=passw)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Successfelly registered!, Welcome {}'.format(name),'success')
            render_template('homepage.html',form=form,login=login,title='Home page',style='./static/style.css',script='./static/script.js')
        except Exception as e:
            db.session.rollback()
            flash('an error occured while registering: {}'.format(str(e)), 'danger')
    if login.validate_on_submit() and login.submit.data:
        user=Users.query.filter_by(name=login.name.data).first()
        if user and user.password==login.password.data:
            session['user_id']=user.get_id()
            login_user(user)
            flash('login sucessful','success')
            return redirect(url_for('dashboard'))
        else: 
            flash('Login unsuccessful. Please try again','danger')
    return render_template("homepage.html",title ='Home page',form=form,login=login,style='./static/style.css',script='./static/script.js')


@app.route("/layout")
def layout():
    return render_template("layout.html",title='layout',style='./static/style.css',script='./static/script.js')
    
@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    if'user_id' in session:
        transactions=Transaction.query.filter_by(idU=session['user_id']).all()
        form=AddTransactionForm()
        if form.validate_on_submit() and form.submit.data:
            amount=form.amount.data
            categ=Category.query.filter_by(name=form.category.data).first()
            date=form.date.data
            if not categ:
                categ=Category(name=form.category.data)
                try:
                    db.session.add(categ)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    flash('error: {}'.format(str(e)),'danger')
            transact=Transaction(amount=amount,idC=categ.get_id(),idU=session['user_id'],date=date)
            try:
                db.session.add(transact)
                db.session.commit()
                flash('Transaction added successfully','success')
            except Exception as e:
                db.session.rollback()
                flash('an error has occured while adding transaction, please try again :{}'.format(str(e)),'danger')
        return render_template('dashboard.html',title="dashboard",Transac=transactions,transactform=form,style='./static/dashboard.css',script='./static/dashboard.js')
    else:
        flash('please login', 'warning')
        return redirect(url_for('homepage'))
        
    
@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    flash('You have been logged out','info')
    return redirect(url_for('homepage'))
