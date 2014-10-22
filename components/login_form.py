from components.component import Component
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.ui import Select, WebDriverWait

__author__ = 'Ivan'


class LoginForm(Component):
    LOGIN = "#id_Login"
    PASSWORD = "#id_Password"
    DOMAIN = "#id_Domain"
    SUBMIT = "#gogogo>input"

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(password)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()