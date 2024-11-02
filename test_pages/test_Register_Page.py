import pytest
from pages.Register_Page import RegistrationPage

@pytest.mark.usefixtures("init_driver")
class TestUserRegistration:

    def test_user_registration(self):
        # URL of the registration page
        url = "http://selenium1py.pythonanywhere.com/en-gb/"

        # Initialize the RegistrationPage object
        registration_page = RegistrationPage(self.driver)

        # Open the registration page and perform registration steps
        registration_page.open_login_page(url)
        registration_page.click_login_link()
        registration_page.enter_email("kixov36981@nestvia.com")
        registration_page.enter_password("zoro@Roronoa9")
        registration_page.confirm_password("zoro@Roronoa9")
        registration_page.submit_registration()


