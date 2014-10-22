from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class IncomeCheckboxGroup(Component):
    HIGH_LEVEL = "#income_group-9288"
    MID_LEVEL = "#income_group-9287"
    LOW_LEVEL = "#income_group-9286"
    INCOME_BLOCK = ".campaign-setting__value"
    INCOME_BLOCK_WRAPPER = ".campaign-setting__wrapper_income_group"

    def set_income(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_BLOCK_WRAPPER + ">" + self.INCOME_BLOCK)
        )).click()

    def set_high_income(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.HIGH_LEVEL)
        )).click()

    def set_mid_income(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.MID_LEVEL)
        )).click()

    def set_low_income(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.LOW_LEVEL)
        )).click()


    def assert_high_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                 WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.HIGH_LEVEL)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False

    def assert_mid_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                 WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.MID_LEVEL)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False


    def assert_low_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                 WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.LOW_LEVEL)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False