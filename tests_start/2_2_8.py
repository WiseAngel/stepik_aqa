import time
import os
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

class UploadFile:

    def __init__(self, link: str) -> None:
        self.link = link

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self

    def upload_file(self):
        browser = webdriver.Chrome()
        browser.get(self.link)


        print(os.path.abspath(__file__))
        print(os.path.abspath(os.path.dirname(__file__)))

        first_name = browser.find_element_by_name('firstname')
        first_name.send_keys('Ivan')
        
        last_name = browser.find_element_by_name('lastname')
        last_name.send_keys('Ivanov')
        
        email = browser.find_element_by_name('email')
        email.send_keys('Ivan@ivanov.iv')

        file = browser.find_element_by_name('file')

        current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
        file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
        file.send_keys(file_path)

        btn = browser.find_element_by_css_selector('.btn.btn-primary')
        btn.click()

        time.sleep(10)


with UploadFile(link) as uf:
    try:
        uf.upload_file()
    except Exception as err:
        print(err)

