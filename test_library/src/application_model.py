from selenium.webdriver.chrome.webdriver import WebDriver

from test_library.src.actions import Actions


class ApplicationModel:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def actions(self) -> Actions:
        return Actions(self.__driver)
