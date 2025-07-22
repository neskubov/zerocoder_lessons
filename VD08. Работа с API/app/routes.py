from flask import render_template, redirect, url_for, flash
import requests
from app import app
from app.forms import base_form, zenquotes_io_form #, api_ninjas_com_form, quoteslate_vercel_app_form

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/base', methods=['GET', 'POST'])
def base():
    form = base_form()
    if form.validate_on_submit():
        return render_template('base_form.html')
    return render_template('base_form.html', form=form, title='resourse')


def fetch_random_quote(url, api_key=''):
    try:
        response = requests.get(url, headers={'X-Api-Key': str(api_key)})
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        if data and isinstance(data, list):
            quote  = 'quote' if bool(api_key) else 'q'
            author  = 'author' if bool(api_key) else 'a'
            quote = data[0].get(quote, 'No quote found')  # Текст цитаты
            author = data[0].get(author, 'Unknown')  # Автор цитаты
            return {'quote': quote, 'author': author}
        else:
            return {'error': 'Invalid response from ZenQuotes API'}
    except requests.exceptions.RequestException as e:
        return {'error': f'Error fetching quote: {str(e)}'}


@app.route('/zenquotes.io', methods=['GET'])
def zenquotes_io():
    url = 'https://zenquotes.io/api/random'
    form = zenquotes_io_form()
    if form.submit():
        quote_data = fetch_random_quote(url)
        if 'error' in quote_data:
            return render_template('zenquotes_io.html', form=form, quote='Ошибка', author=quote_data['error'], title=url)
        return render_template('zenquotes_io.html', form=form, quote=quote_data['quote'], author=quote_data['author'], title=url)
    return render_template('zenquotes_io.html', form=form, title=url)


@app.route('/api-ninjas.com', methods=['GET', 'POST'])
def api_ninjas_com():
    url = 'https://api.api-ninjas.com/v1/quotes'
    form = base_form()
    if form.validate_on_submit():
        api_key = form.api_key.data
        print(api_key)
        quote_data = fetch_random_quote(url, api_key)
        print(quote_data)
        if 'error' in quote_data:
            return render_template('zenquotes_io.html', form=form, api_key=True, quote='Ошибка', author=quote_data['error'], title=url)
        return render_template('zenquotes_io.html', form=form, api_key=True, quote=quote_data['quote'], author=quote_data['author'], title=url)
    return render_template('zenquotes_io.html', form=form, api_key=True, title=url)


@app.route('/quoteslate.vercel.app', methods=['GET', 'POST'])
def quoteslate_vercel_app():
    url = 'https://quoteslate.vercel.app/api/quotes/random'
    form = base_form()
    if form.validate_on_submit():
        api_key = form.api_key.data
        print(api_key)
        quote_data = fetch_random_quote(url, api_key)
        print(quote_data)
        if 'error' in quote_data:
            return render_template('zenquotes_io.html', form=form, api_key=True, quote='Ошибка',
                                   author=quote_data['error'], title=url)
        return render_template('zenquotes_io.html', form=form, api_key=True, quote=quote_data['quote'],
                               author=quote_data['author'], title=url)
    return render_template('zenquotes_io.html', form=form, api_key=True, title=url)

