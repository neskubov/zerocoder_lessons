from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, load_user
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, EditProfile

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Введены неверные данные')
    return render_template('login.html', form=form, title='Login')

@app.route('/editProfile', methods=['GET', 'POST'])
def editProfile(user):
    form = EditProfile()
    if form.validate_on_submit():
        print(1)
        hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        if form.new_username.data:
            user.username = form.new_username.data
        if form.new_email.data:
            user.email = form.new_email.data
        if form.new_password.data:
            user.password = hashed_password
        db.session.commit()
        flash('Данные успешно изменены!', 'success')
        return redirect('editProfile.html')

    return render_template('editProfile.html', form=form, title='editProfile')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')