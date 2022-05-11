from flask_login import logout_user
from app import app,db
from flask import redirect, render_template, url_for, redirect, flash
from .forms import LogIn, Signup

@app.route('/')
@app.route('/home')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route("/laugh")
def laugh():
    return render_template('laugh.html')      

@app.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    signup_form = Signup()
    if signup_form.validate_on_submit():
        flash(f'Successfully signed in for {signup_form.username.data}', category='success')
        return redirect(url_for('login'))   
    return render_template("signup.html", form=signup_form)  

@app.route("/login", methods=['POST', 'GET'])
def login():
    form=LogIn()
    if form.validate_on_submit():
        if form.username.data=='' and form.password.data=='':
            flash(f'Login success for {form.username  .data}', category='success')    
            return redirect(url_for('pitch'))  
        else:  
            flash(f'Login unsuccessfull {form.username.data}', category='danger')    
            return redirect(url_for('index'))
    return render_template('login.html', form=LogIn)    

@app.route("/pitch")
def pitch():
    return render_template('pitch.html')    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index.html'))
