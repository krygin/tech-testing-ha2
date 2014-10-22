from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class EditCampaignButton(Component):
    EDIT_BUTTON = ".control__link_edit"

    def click(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.EDIT_BUTTON)
        )).click()