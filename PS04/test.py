from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
import random



#Если работаем в Firefox
browser = webdriver.Firefox()


#Если работаем в Chrome
browser = webdriver.Chrome()


#Далее одинаково для всех браузеров

#Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

hatnotes = {}
elements = browser.find_elements(By.TAG_NAME, "div")
number = 1
for element in elements:
    # Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        print(f"{number}: {element.find_element(By.TAG_NAME, "a").get_attribute("title")}")
        hatnotes[number] = element.find_element(By.TAG_NAME, "a").get_attribute("href")
        number += 1
choice_number = int(input("Введите номер ссылки: "))

link = hatnotes[choice_number]
browser.get(link)

input()
time.sleep(10)