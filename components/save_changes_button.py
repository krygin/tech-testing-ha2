from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class SaveChangesButton(Component):
    SAVE_CHANGES_BUTTON = ".main-button-new"

    def click(self):
        element = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.SAVE_CHANGES_BUTTON)
        )
        element.click()