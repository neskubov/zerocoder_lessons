#Сохранение и загрузка данных
import os
import json

filename = "data_base_file.json"

#Загружаем список задач или создаем фаил для задач
if not os.path.exists(filename):
    # Открываем файл в режиме записи и создаем его, если он не существует
    with open(filename, 'w', encoding='utf-8') as file:
        # Записываем данные в формате JSON
        json.dump({"list_employees": [], "list_animals": []}, file, ensure_ascii=False, indent=4)
    print(f"Файл '{filename}' был создан и данные записаны.")

#Загрузка данных из базы
def load_list_zoo():
    #Читаем данные из базы
    with open(filename, 'r', encoding='utf-8') as file:
        data_base = json.load(file)
    return data_base

def save_list_zoo(data):
    with open(filename, 'w', encoding='utf-8') as file:
        # Записываем данные в формате JSON
        json.dump(data, file, ensure_ascii=False, indent=4)
