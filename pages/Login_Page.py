from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_link = (By.ID, "login_link")
        self.username_input = (By.ID, "id_login-username")
        self.password_input = (By.ID, "id_login-password")
        self.login_button = (By.NAME, "login_submit")

    def open_login_page(self, url: str):
        self.driver.get(url)

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_username(self, username: str):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.login_button).click()
