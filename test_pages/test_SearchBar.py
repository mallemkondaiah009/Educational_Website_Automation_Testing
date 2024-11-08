import pytest
from pages.SearchBar import SearchBar
import time

@pytest.mark.usefixtures("init_driver")
class TestUserLogin:

    def test_user_login(self):
        # URL of the login page
        url = "http://selenium1py.pythonanywhere.com/en-gb/"
        search_page = SearchBar(self.driver)
        search_page.open_login_page(url)
        time.sleep(10)
        search_page.search_bar()
        search_page.search_click

