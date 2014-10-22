# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class WhereTree(Component):
    RUSSIA_NODE = '#regions188>.tree__node__input'
    COLLAPSE_RUSSIA_TREE = "#regions188>.tree__node__collapse-icon"
    MOSCOW_GROUP = '[data-name="moscow"]'
    MOSCOW_NODE = '#regions70>.tree__node__input'
    SBP_NODE = '#regions107>.tree__node__input'
    PENZA_NODE = '#regions96>.tree__node__input'


    def set_region(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.COLLAPSE_RUSSIA_TREE)
        )).click()

    def set_moscow_group(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.MOSCOW_GROUP)
        )).click()

    def set_spb_node(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.SBP_NODE)
        )).click()

    def set_moscow_node(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.MOSCOW_NODE)
        )).click()

    def set_penza_node(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.PENZA_NODE)
        )).click()

    def uncheck_all_nodes(self):
        (WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.RUSSIA_NODE)
        )).click()

    def assert_moscow_node_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.MOSCOW_NODE)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False

    def assert_spb_node_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.SBP_NODE)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False

    def assert_penza_node_checked(self):
        checkbox = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                       WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.PENZA_NODE)
        )
        if checkbox.get_attribute("checked") == "true":
            return True
        else:
            return False