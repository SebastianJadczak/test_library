from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from test_library.utils.cookie import CookieData
from test_library.utils.locator import Locator


class Actions:

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def find_element(self, locator: Locator) -> WebElement:
        return self.__driver.find_element(locator.by, locator.value)

    def find_elements(self, locator: Locator) -> list[WebElement]:
        return self.__driver.find_elements(locator.by, locator.value)

    def send_keys(self, locator: Locator, data: str | float | int):
        self.__driver.find_element(locator.by, locator.value).send_keys(data)

    def get(self, url: str):
        self.__driver.get(url)

    def click(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).click()

    def clear(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).clear()

    def clear_and_send_keys(self, locator: Locator, data: str):
        el = self.__driver.find_element(locator.by, locator.value)
        el.clear()
        el.send_keys(data)

    def is_selected(self, locator: Locator) -> bool:
        return self.__driver.find_element(locator.by, locator.value).is_selected()

    def select(self, locator: Locator, value: str):
        select = Select(self.__driver.find_element(locator.by, locator.value))
        select.select_by_value(value)

    def implicitly_wait(self, time: int | float):
        self.__driver.implicitly_wait(time)

    def get_text(self, locator: Locator) -> str:
        return self.__driver.find_element(locator.by, locator.value).text

    def get_value(self, locator: Locator) -> str | None:
        return self.__driver.find_element(locator.by, locator.value).get_attribute('value')

    def get_placeholder(self, locator: Locator) -> str | None:
        return self.__driver.find_element(locator.by, locator.value).get_attribute('placeholder')

    def get_rect(self, locator: Locator) -> dict:
        return self.__driver.find_element(locator.by, locator.value).rect

    def get_value_of_css_property(self, locator: Locator, css_property: str) -> str:  # add property Enum
        return self.__driver.find_element(locator.by, locator.value).value_of_css_property(css_property)

    def add_cookie(self, cookie: CookieData):
        self.__driver.add_cookie(cookie_dict={'name': cookie.name, 'value': cookie.value})

    def wait_until_presence_of_element_located(self, locator: Locator, *, time: int):
        wait = WebDriverWait(self.__driver, time)
        return wait.until(method=expected_conditions.presence_of_element_located((locator.by, locator.value)),
                          message='Nie znaleziono elementu w wyznaczonym czasie')

    def get_session_id(self) -> str | None:
        return self.__driver.session_id()
