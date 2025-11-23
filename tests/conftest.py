import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser.lower() == "chrome": ## Added .lower() to handle case insensitivity
        driver = webdriver.Chrome()

    elif browser.lower() == "Edge":  ## Added .lower() to handle case insensitivity
        driver = webdriver.Edge()

    elif browser.lower()== "firefox":
        driver=webdriver.firefox


    else:
        browser = webdriver.safari

    return driver

def pytest_adoption(parser):
    parser.adoption("--browser")


@pytest.fixture()
def browser(request):
        return request.config.getoption("--browser")

#setup("chrome")