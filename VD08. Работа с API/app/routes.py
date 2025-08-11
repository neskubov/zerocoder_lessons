from flask import render_template
import requests
from app import app
from app.forms import form_with_key, form_without_key

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

def fetch_random_quote(url, api_key='', quote='q', author='a'):
    try:
        headers = {
            'X-Api-Key': str(api_key),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        print(type(data))

        if data and isinstance(data, list):
            quote = data[0].get(quote, 'No quote found')  # Текст цитаты
            author = data[0].get(author, 'Unknown')  # Автор цитаты
            return {'quote': quote, 'author': author}
        elif data and isinstance(data, dict):
            return {'quote': data[quote], 'author': data[author]}
        else:
            return {'error': 'Invalid response from ZenQuotes API'}
    except requests.exceptions.RequestException as e:
        return {'error': f'Error fetching quote: {str(e)}'}


@app.route('/zenquotes.io', methods=['GET', 'POST'])
def zenquotes_io():
    url = 'https://zenquotes.io/api/random'
    form = form_without_key()
    if form.submit():
        quote_data = fetch_random_quote(url)
        if 'error' in quote_data:
            return render_template('zenquotes_io.html', form=form, quote='Ошибка', author=quote_data['error'], title=url)
        return render_template('zenquotes_io.html', form=form, quote=quote_data['quote'], author=quote_data['author'], title=url)
    return render_template('zenquotes_io.html', form=form, title=url)


@app.route('/api-ninjas.com', methods=['GET', 'POST'])
def api_ninjas_com():
    url = 'https://api.api-ninjas.com/v1/quotes'
    form = form_with_key()
    if form.validate_on_submit():
        api_key = form.api_key.data
        quote_data = fetch_random_quote(url, api_key, 'quote', 'author')
        if 'error' in quote_data:
            return render_template('api-ninjas.com.html', form=form, api_key=True, quote='Ошибка', author=quote_data['error'], title=url)
        return render_template('api-ninjas.com.html', form=form, api_key=True, quote=quote_data['quote'], author=quote_data['author'], title=url)
    return render_template('api-ninjas.com.html', form=form, api_key=True, title=url)


@app.route('/quoteslate.vercel.app', methods=['GET', 'POST'])
def quoteslate_vercel_app():
    url = 'https://quoteslate.vercel.app/api/quotes/random'
    form = form_without_key()
    if form.submit():
        quote_data = fetch_random_quote(url, quote='quote', author='author')
        print(quote_data)
        if 'error' in quote_data:
            return render_template('quoteslate_vercel_app.html', form=form,  quote='Ошибка',
                                   author=quote_data['error'], title=url)
        return render_template('quoteslate_vercel_app.html', form=form,  quote=quote_data['quote'],
                               author=quote_data['author'], title=url)
    return render_template('quoteslate_vercel_app.html', form=form,  title=url)


