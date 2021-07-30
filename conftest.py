import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope='function')
# def browser():
#     print('\nstart browser for test..')
#     browser = webdriver.Chrome()
#     yield browser
#     print('\nquit browser..')
#     browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose lang')
    parser.addoption('--full_screen', default=False, help='Open browser in fullscrin')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    window_size = request.config.getoption('full_screen')
    browser = None
    
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        # options.add_argument('--start-maximized')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    if window_size:
        browser.maximize_window()

    yield browser
    print('\nquit browser..')
    browser.quit()