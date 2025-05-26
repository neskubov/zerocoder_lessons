from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
#Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(5)

def search():
    #Находим окно поиска
    search_box = browser.find_element(By.ID, "searchInput")
    #Запрашиваем текст для поиска у пользователя
    searchInput = input("Введите запрос для поиска: ")
    #Правим текст поиска под шаблон
    text = searchInput[0].upper() + searchInput[1:].lower()
    #Отправляем текст для поиска
    search_box.send_keys(text)
    #Добавляем не только введение текста, но и его отправку
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    #Проверка наличия статьи
    try:
        browser.find_element(By.CLASS_NAME, "mw-search-nonefound")
        print("Статья отсутствует. Повторите поиск")
        search()
    except:
        # Получаем ссылку
        a = browser.find_element(By.LINK_TEXT, text)
        # Добавляем клик на элемент
        a.click()

#Функция для реализации выбора пользователя
def get_information():
    print("Выберите действие:",
          "1 - листать параграфы статьи",
          "2 - перейти на одну из внутренних статей",
          "3 - выйти из программы",
          sep="\n")

    choice = int(input())

    match choice:
        case 1:
            #Поиск всех параграфов
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            #Чтение параграфов
            for paragraph in paragraphs:
                print(paragraph.text)
                input("Нажмите ENTER для перехода к следующему параграфу:")
                print("-------------------------------------------------")
            print("INFORMATION: Статья прочитана. Выход из программы")
            #Закрыть все окна браузера
            browser.quit()

        case 2:
            hatnotes = {}
            elements = browser.find_elements(By.TAG_NAME, "div")
            #Счетчик ссылок
            number = 0
            for element in elements:
                # Чтобы искать атрибут класса
                cl = element.get_attribute("class")
                if cl == "hatnote navigation-not-searchable ts-main":
                    number += 1
                    #Выводим список статей и добавляем в словарь
                    print(f"{number}: {element.find_element(By.TAG_NAME, "a").get_attribute("title")}")
                    hatnotes[number] = element.find_element(By.TAG_NAME, "a").get_attribute("href")

            if number == 0:
                print("Связанных статей нет, программа завершена")
                browser.quit()
                return

            choice_number = int(input("Введите номер ссылки: "))
            link = hatnotes[choice_number]
            browser.get(link)
            time.sleep(5)
            get_information()

        case 3:
            print("Программа завершена")
            browser.quit()
            return

search()
get_information()


