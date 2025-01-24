from abc import abstractmethod
from selenium.webdriver.chrome.webdriver import WebDriver


class MainStage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @abstractmethod
    def open_site(self):
        ...


class Stage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
