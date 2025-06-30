from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def blog():
    user_data = None
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Сохранение данных в словарь
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

    return render_template('blog.html', user_data=user_data)
