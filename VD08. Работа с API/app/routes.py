from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms import base_form, zenquotes_io, api_ninjas_com, quoteslate_vercel_app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/zenquotes.io', endpoint='base_form')
def zenquotes_io():
    form = zenquotes_io()
    if form.validate_on_submit():
        return render_template(zenquotes_io.html)
    return render_template('base_form.html', form=form, title='Register')

'''
@app.route('/api-ninjas.com', endpoint='base_form')
def api_ninjas_com():
    form = api_ninjas_com()
    if form.validate_on_submit():
        return render_template(url_for('api_ninjas_com'))
    return render_template('base_form.html', form=form, title='Register')


@app.route('/quoteslate.vercel.app', endpoint='base_form')
def quoteslate_vercel_app():
    form = zenquotes_io()
    if form.validate_on_submit():
        return render_template(url_for('quoteslate_vercel_app'))
    return render_template('base_form.html', form=form, title='Register')
'''