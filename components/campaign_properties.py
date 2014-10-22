from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class CampaignProperties(Component):
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    PAD = '.base-setting__pads-item__label'

    def get_campaign_name(self):
        return WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                             WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME).get_attribute("value")
        )

    def get_pad(self):
        return WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                             WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.PAD).get_attribute("value")
        )