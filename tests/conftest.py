import json
import pytest
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

from pages.landing import HomePage


@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        b = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = ChromeOptions()
        opts.add_argument('headless')
        b = webdriver.Chrome(chrome_options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()


@pytest.fixture
def landing_page(browser):
    return HomePage(browser)
