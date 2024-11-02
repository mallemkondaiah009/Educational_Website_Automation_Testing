import pytest
from pages.Login_Page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestUserLogin:

    def test_user_login(self):
        # URL of the login page
        url = "http://selenium1py.pythonanywhere.com/en-gb/"

        # Initialize the LoginPage object
        login_page = LoginPage(self.driver)

        # Open the login page and perform login steps
        login_page.open_login_page(url)
        login_page.click_login_link()
        login_page.enter_username("kixov36981@nestvia.com")
        login_page.enter_password("zoro@Roronoa9")
        login_page.submit_login()

