from selenium.webdriver.common.by import By


class RegistrationPage:
    REGISTRATION_FORM = (By.CLASS_NAME, 'registration')

    NTF_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, '[id="modal-ready-popup"] [class="close"]')

    TITLE = (By.CSS_SELECTOR, '[class="slogan"] h1')

    REGISTRATION_PROGRESS_BAR = (By.CSS_SELECTOR, '[class="reg-steps-2 first-step"]')

    REGISTRATION_PROGRESS_BAR_TITLE = (By.CSS_SELECTOR, '[class="registration"] h2')

    AMOUNT_CALCULATOR_TOOLBAR_TITLE = (By.CSS_SELECTOR, '[class="change-amount"] label')

    AMOUNT_CALCULATOR_TOOLBAR_BUTTON = (By.CSS_SELECTOR, '[class="change-amount"] [class="button secondarry-btn"]')

    NAME_INPUT_FIELD = (By.CSS_SELECTOR, '[name="name"]')

    SURNAME_INPUT_FIELD = (By.CSS_SELECTOR, '[name="surname"]')

    NIN_INPUT_FIELD = (By.CSS_SELECTOR, '[name="pesel"]')

    NIN_INPUT_FIELD_TOOLTIP = (By.XPATH, '//input[contains(@name,"pesel")]//..//div[@class ="tip-example"]')

    IDN_INPUT_FIELD = (By.CSS_SELECTOR, '[name="document-number"]')

    IDN_INPUT_FIELD_TOOLTIP = (By.XPATH, '//input[contains(@name,"document-number")]//..//div[@class ="tip-example"]')

    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, '[name="email"]')

    PHONE_INPUT_FIELD = (By.CSS_SELECTOR, '[name="phone"]')

    DOCUMENT_TYPE_DROPDOWN = (By.CSS_SELECTOR, '[name="document_type"]')

    DOCUMENT_TYPE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, '[name="document_type"] option')

    COUNTRY_INPUT_FIELD = (By.XPATH, '//input[contains(@name,"country")]/preceding-sibling::input[@class="input"]')

    PHONE_PREFIX_INPUT_FIELD = (By.CSS_SELECTOR, '[name="phone_prefix"]')

    COUNTRY_INPUT_FIELD = (By.XPATH, '//input[contains(@name,"country")]/preceding-sibling::input[@class="input"]')

    PHONE_PREFIX_INPUT_FIELD = (By.CSS_SELECTOR, '[name="phone_prefix"]')

    INPUT_FIELD_TIP = (By.CSS_SELECTOR, '.registration [class="tip"]')

    RESEND_SMS_BUTTON = (By.ID, 'resend-loader')

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.find_element(*self.TITLE)

    def get_resend_sms_button(self):
        return self.browser.find_element(*self.RESEND_SMS_BUTTON)

    def get_country_input_field(self):
        return self.browser.find_element(*self.COUNTRY_INPUT_FIELD)

    def get_phone_prefix_input_field(self):
        return self.browser.find_element(*self.PHONE_PREFIX_INPUT_FIELD)

    def get_name_input_field(self):
        return self.browser.find_element(*self.NAME_INPUT_FIELD)

    def get_surname_input_field(self):
        return self.browser.find_element(*self.SURNAME_INPUT_FIELD)

    def get_nin_input_field(self):
        return self.browser.find_element(*self.NIN_INPUT_FIELD)

    def get_idn_input_field(self):
        return self.browser.find_element(*self.IDN_INPUT_FIELD)

    def get_email_input_field(self):
        return self.browser.find_element(*self.EMAIL_INPUT_FIELD)

    def get_phone_input_field(self):
        return self.browser.find_element(*self.PHONE_INPUT_FIELD)

    def get_registration_progress_bar(self):
        return self.browser.find_element(*self.REGISTRATION_PROGRESS_BAR)

    def get_document_type_dropdown(self):
        return self.browser.find_element(*self.DOCUMENT_TYPE_DROPDOWN)

    def get_registration_progress_bar_title(self):
        return self.browser.find_element(*self.REGISTRATION_PROGRESS_BAR_TITLE)

    def get_amount_calculator_title(self):
        return self.browser.find_element(*self.AMOUNT_CALCULATOR_TOOLBAR_TITLE)

    def get_amount_calculator_button(self):
        return self.browser.find_element(*self.AMOUNT_CALCULATOR_TOOLBAR_BUTTON)

    def close_notification_popup(self):
        self.browser.find_element(*self.NTF_POPUP_CLOSE_BUTTON).click()
        self.browser.find_element(*self.REGISTRATION_FORM)

    def is_title_visible(self):
        return self.get_title().is_displayed()

    def is_resend_sms_button_visible(self):
        return self.get_resend_sms_button().is_displayed()

    def get_title_text(self):
        return self.get_title().text

    def is_registration_progress_bar_visible(self):
        return self.get_registration_progress_bar().is_displayed()

    def is_registration_progress_bar_title_visible(self):
        return self.get_registration_progress_bar_title().is_displayed()

    def get_registration_progress_bar_title_text(self):
        return self.get_registration_progress_bar_title().text

    def is_amount_calculator_button_visible(self):
        return self.get_amount_calculator_button().is_displayed()

    def is_amount_calculator_title_visible(self):
        return self.get_amount_calculator_title().is_displayed()

    def get_amount_calculator_title__text(self):
        return self.get_amount_calculator_title().text

    def validate_input_field(locator, placeholder):
        assert locator.is_displayed() == True
        assert locator.is_enabled() == True
        assert locator.get_attribute('placeholder') == placeholder

    def validate_readonly_input_field(locator, placeholder):
        assert locator.is_displayed() == True
        assert locator.is_enabled() == True
        assert locator.get_attribute('readonly') is not None
        assert locator.get_attribute('value') == placeholder

    def validate_readonly_input_field(locator, placeholder):
        assert locator.is_displayed() == True
        assert locator.is_enabled() == True
        assert locator.get_attribute('readonly') is not None
        assert locator.get_attribute('value') == placeholder

    def validate_document_type_drop_down(self, selected_value, value_list):
        assert self.get_document_type_dropdown().is_displayed() == True
        assert self.get_document_type_dropdown().is_enabled() == True

        for option in self.browser.find_elements(*self.DOCUMENT_TYPE_DROPDOWN_OPTIONS):
            if option.text in value_list:
                if option.is_selected():
                    assert option.text == selected_value
            else:
                raise Exception("Unexpected option value")

    def validate_registration_page_tooltips(self):
        assert self.browser.find_element(*self.NIN_INPUT_FIELD_TOOLTIP).is_displayed()
        assert self.browser.find_element(*self.NIN_INPUT_FIELD_TOOLTIP).is_enabled()

        assert self.browser.find_element(*self.IDN_INPUT_FIELD_TOOLTIP).is_displayed()
        assert self.browser.find_element(*self.IDN_INPUT_FIELD_TOOLTIP).is_enabled()

    def validate_input_field_tip(self, value):
        if value not in [o.text for o in self.browser.find_elements(*self.INPUT_FIELD_TIP)]:
            raise Exception("Unexpected input field tip value")
