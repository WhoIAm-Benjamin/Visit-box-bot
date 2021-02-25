# coding: utf8

# тестовый скрипт - заходим на сайт visit-box.net
import urllib
import urllib.request
from selenium import webdriver
import time
import pyautogui

login='maksim.trya@mail.ru'
password='mWkskeksqwerterW3'

try:
    browser = webdriver.Chrome()
    browser.get("https://visit-box.net/visits/")
    browser.maximize_window()							# раскрываем окно браузера на весь экран
    browser.implicitly_wait(5)							# говорим WebDriver искать каждый элемент в течение 5 секунд
    input1 = browser.find_element_by_css_selector('[name="login"]') # нашли поле Login
    input1.send_keys(login)
    input2 = browser.find_element_by_css_selector('[name="password"]') # нашли поле Password
    input2.send_keys(password)
    time.sleep(70)
    url1 = browser.find_element_by_css_selector('[class="title"]') # нашли первую доступную для просмотра ссылку
    url1.click()
## решить проблемы
## 1 - обновлять (F5) - стнаницу - чтобы больше 10-ти
## 2 - переключатьфокус на 2ю страницу
    time.sleep(20)
###################################################################
# тут я буду пытаться сохранить страницу сайта локально
# ATTENSION!!!! - Работает ТОЛЬКО если Язык ввода по умолчанию стоит Английский. Просто выбрать Английский язык не поможет
# ATTENSION!!!! - файл html(вместе с аналогичной подпапкой со js-скриптами картинками и просчим мусором)
# сохраняется в папку загрузки выбранную по умолчанию, у меня например это папка Загрузки (Downloads)
# ATTENSION!!!! - при повторном запуске данного скрипта выскочит окно сообщения чтотакой файл уже  существует
#(по идее или после обработки удаляем данный файл или каждый раз переименовываем его
# ATTENSION!!!! - при ручном запуске данного сохраненного файла из локальной папки если не хотим получить сообщение:
# Сбой при загрузке капчи. Повторите попытку - запускаем html-файл без его подпапки со js-скриптами
# open 'Save as...' to save html and assets
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite('SEQUENCE.html')
    pyautogui.hotkey('enter')
###################################################################

    
finally:
    # успеваем скопировать код за 30 секунд
    
    time.sleep(10)
    # закрываем браузер после всех манипуляций
#    browser.quit()

# не забываем оставить пустую строку в конце файла
