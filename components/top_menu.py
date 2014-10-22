from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class TopMenu(Component):
    ELEMENT_SELECTOR = "#PH_user-email"

    def get_email(self):
        return (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.ELEMENT_SELECTOR)).text
        )