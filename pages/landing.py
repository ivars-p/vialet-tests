from selenium.webdriver.common.by import By
from pages.registration import RegistrationPage


class HomePage:
    URL = 'https://vialet.pl/'

    REGISTRATION_BUTTON = (By.CLASS_NAME, '_register-route')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def click_register(self):
        self.browser.find_element(*self.REGISTRATION_BUTTON).click()
        return RegistrationPage(self.browser)

