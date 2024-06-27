from app import app,db
from flask import render_template,redirect,url_for,flash,session,request
from flask_login import login_user,logout_user,current_user
from app.form import SignUpForm,LoginForm,AddTransactionForm,ModifyTransaction,filterbymonth
from app.models import Users,Transaction,Category
from sqlalchemy import desc,extract
from datetime import datetime
import matplotlib.pyplot as plt
import io

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
        category=Category.query.all()
        choice=request.form.get('cat_filter')
        print(str(choice))
        if choice is None:
            flash("no transaction in this category")
            transactions=Transaction.query.filter_by(idU=session['user_id']).order_by(desc(Transaction.date))
        elif str(choice)=="All":
            transactions=Transaction.query.filter_by(idU=session['user_id']).order_by(desc(Transaction.date))
        else:
            transactions=Transaction.query.filter_by(idU=session['user_id'],idC=choice).order_by(desc(Transaction.date))
        form=AddTransactionForm()
        month_filter=filterbymonth()
        modify=ModifyTransaction()
        if modify.validate_on_submit() and modify.submit.data:
            it=modify.id.data
            amount=modify.amount.data
            categ=Category.query.filter_by(name=modify.category.data).first()
            if not categ:
                categ=Category(name=modify.category.data)
                try:
                    db.session.add(categ)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    flash('error: {}'.format(str(e)),'danger')
            try:
                Transaction.query.filter_by(idT=it).update({
                    'amount': amount,
                    'idC': categ.get_id()
                    })
                db.session.commit()
                flash('Transaction modified successfully','success')
                return redirect(url_for('dashboard'))
            except Exception as e:
                db.session.rollback()
                flash('an error has occured while adding transaction, please try again :{}'.format(str(e)),'danger')
        if month_filter.validate_on_submit() and month_filter.submit.data:
            transactions=Transaction.query.filter_by(idU=session['user_id']).filter(extract('month',Transaction.date)==month_filter.date.data).order_by(desc(Transaction.date))
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
                return redirect(url_for('dashboard'))
            except Exception as e:
                db.session.rollback()
                flash('an error has occured while adding transaction, please try again :{}'.format(str(e)),'danger')
        return render_template('dashboard.html',title="dashboard",modif=modify,filter_date=month_filter,category=category,Transac=transactions,transactform=form,style='./static/dashboard.css',script='./static/dashboard.js')
    else:
        flash('please login', 'warning')
        return redirect(url_for('homepage'))
        
    
@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    flash('You have been logged out','info')
    return redirect(url_for('homepage'))

@app.route('/profile',methods=['Get','Post'])
def Profile():
    return render_template('profile.html',title="Profile",style='./static/profile.css',script='./static/profile.js')



@app.route('/graphs',methods=['GET','POST'])
def graphs():
    if 'user_id' in session:
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
                return redirect(url_for('graphs'))
            except Exception as e:
                db.session.rollback()
                flash('an error has occured while adding transaction, please try again :{}'.format(str(e)),'danger')
    return render_template('graphs.html',title="dashboard",transactform=form,style='./static/dashboard.css',script='./static/dashboard.js')

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    fig.savefig(output, format='png')
    output.seek(0)
    return send_file(output, mimetype='image/png')

def create_figure():
    transactions=Transaction.query.filter_by(idU=session['user_id']).order_by(desc(Transaction.date))
    fig, ax = plt.subplots()
    ax.plot(transactions)
    ax.set(xlabel='month',ylabel='amount spent',title='amount spent by month')
    ax.grid
    return create_figure
