import hashlib
import os

def generate_random_hash(algorithm='sha256'):
    """
    Генерирует случайный хэш с использованием указанного алгоритма.
    """
    # Генерируем случайные байты
    random_data = os.urandom(64)

    # Получаем объект хэш-функции
    hash_function = hashlib.new(algorithm)

    # Обновляем хэш объект случайными данными
    hash_function.update(random_data)

    # Возвращаем хэш в виде шестнадцатеричной строки
    return hash_function.hexdigest()


class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, name_product, price):
        self.items[name_product] = price

    def del_product(self, product_id):
        del self.items[product_id]

    def get_price(self, name_product):
        return self.items.get(name_product)

    def update_price(self, name_product, new_price):
        self.items[name_product] = new_price


flowers_shop = Store('flowers shop','LA')
flowers_shop.add_product('роза', 100)
flowers_shop.add_product('тюльпан', 222)
flowers_shop.add_product('фиалка', 333)

beer_shop = Store('beer shop','Berlin')
beer_shop.add_product('светлое', 444)
beer_shop.add_product('темное', 555)
beer_shop.add_product('фирменное', 666)

sport_shop = Store('beer shop','Madrid')
sport_shop.add_product('футболка', 777)
sport_shop.add_product('шорты', 888)
sport_shop.add_product('бутсы', 999)

print(1, sport_shop.items)

print(2, sport_shop.get_price('футболка'))
print(3, sport_shop.get_price('шорты'))
print(4, sport_shop.get_price('бутсы'))
print(5, sport_shop.get_price('гетры'))

print(6, sport_shop.update_price('бутсы', 1111))
print(7, sport_shop.get_price('бутсы'))

print(8, sport_shop.del_product('шорты'))
print(9, sport_shop.items)




