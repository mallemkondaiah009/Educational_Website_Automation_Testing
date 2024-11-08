from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SearchBar:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search = (By.ID, "id_q")
        self.search_click=(By.XPATH,"//input[@value='Search']")


    def open_login_page(self, url: str):
        self.driver.get(url)

    def search_bar(self):
        self.driver.find_element(*self.search).send_keys("The Robot Novels")

    def enter_search(self):
        self.driver.find_element(*self.search_click).click()



