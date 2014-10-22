from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class CampaignSettings(Component):
    CAMPAIGN_NAME = ".base-setting__campaign-name__input"
    GROUP_EVENT_VIDEOCHANNEL = "#product-type-5212"
    ODNOKLASSNIKI_MOBILE = "#pad-mobile_odkl_feed_abstract"

    def set_campaign_name(self, name):
        edit_box = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        edit_box.clear()
        edit_box.send_keys(name)

    def set_group_event_videochannel(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.GROUP_EVENT_VIDEOCHANNEL)
        )).click()

    def set_odnoklassniki_mobile(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.ODNOKLASSNIKI_MOBILE)
        )).click()