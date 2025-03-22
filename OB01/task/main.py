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


class Task():
    def __init__(self):
        self.dict_task = {}

    def get_new_task(self):
        return [{task_id: self.dict_task[task_id]} for task_id in self.dict_task if self.dict_task[task_id][3] == 'new']

    def add_task(self, id_task, name, description, deadline, status='new'): #deadline в секундах
        self.dict_task[id_task] = [name, description, deadline, status]

    def change_status(self, id_task):
        if self.dict_task:
            self.dict_task[id_task][3] = 'completed'

new_task = Task()

new_task_id1 = generate_random_hash()
new_task.add_task(new_task_id1,'call', 'позвонить', 1000)

new_task_id2 = generate_random_hash()
new_task.add_task(new_task_id2,'add_task', 'добавить задачу', 2222)

new_task_id3 = generate_random_hash()
new_task.add_task(new_task_id3,'football', 'поиграть в футбол', 6666)

print(1, new_task.get_new_task())
new_task.change_status(new_task_id2)
print(2, new_task.get_new_task())



