from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration1.html'
with webdriver.Chrome() as browser:
    browser.get(link)

    first_name = browser.find_element_by_css_selector('.first_block .first')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('.first_block .second')
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_css_selector('.first_block > .form-group.third_class > input')
    email.send_keys('Ivan@ivanov.iv')
    phone = browser.find_element_by_css_selector('.second_block > .first_class > input')
    phone.send_keys('147852369')
    address = browser.find_element_by_css_selector('.second_block > .second_class > input')
    address.send_keys('Ivanovka')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
