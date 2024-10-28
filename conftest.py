import pytest
from selenium import webdriver
import os
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a screenshots directory if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Browser initialization fixture
@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        driver_path = "../HealthCare_Website_Testing/Browsers/chromedriver.exe"
        driver = webdriver.Chrome(service=ChromeService(driver_path))
    elif request.param == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        driver_path = "../HealthCare_Website_Testing/Browsers/geckodriver.exe"
        driver = webdriver.Firefox(service=FirefoxService(driver_path))
    elif request.param == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        driver_path = "../HealthCare_Website_Testing/Browsers/msedgedriver.exe"
        driver = webdriver.Edge(service=EdgeService(driver_path))

    driver.maximize_window()
    request.cls.driver = driver  # Makes driver available in the test class
    yield driver  # Pass driver instance to tests
    driver.quit()  # Quit browser after test completion

# Pytest hook to capture screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot if the test fails
    if report.when == "call" and report.failed:
        driver = item.instance.driver
        if driver:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved to {screenshot_name}")