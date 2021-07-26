import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW

links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 
    'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 
    'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('link', links)
def test_fin(browser, link):

    browser.get(link)

    answer = math.log(int(time.time()))

    WW(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'string-quiz__textarea'))).send_keys(f'{answer}')

    browser.find_element_by_class_name('submit-submission').click()

    res = WW(browser, 5).until(lambda x: x.find_element_by_class_name('smart-hints__hint')).text

    assert res == 'Correct!', f'Текст ответа: {res}'
