from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_link = (By.ID, "login_link")
        self.email_input = (By.ID, "id_registration-email")
        self.password1_input = (By.ID, "id_registration-password1")
        self.password2_input = (By.ID, "id_registration-password2")
        self.register_button = (By.NAME, "registration_submit")

    def open_login_page(self, url: str):
        self.driver.get(url)

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_email(self, email: str):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password1_input).send_keys(password)

    def confirm_password(self, password: str):
        self.driver.find_element(*self.password2_input).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*self.register_button).click()
