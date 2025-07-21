from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, load_user
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, EditProfile

hashed_password = bcrypt.generate_password_hash('qwertyuio').decode('utf-8')
print(hashed_password)