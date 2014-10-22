import os
from components.login_form import LoginForm
from constants import Credentials
from page_objects.page import Page

__author__ = 'Ivan'


class LoginPage(Page):
    PATH = "/login"

    @property
    def form(self):
        return LoginForm(self.driver)

    def login(self):
        self.open()
        TTHA2LOGIN = Credentials.TTHA2LOGIN
        TTHA2PASSWORD = Credentials.TTHA2PASSWORD
        TTHA2DOMAIN = Credentials.DOMAIN
        login_form = self.form
        login_form.set_login(TTHA2LOGIN)
        login_form.set_password(TTHA2PASSWORD)
        login_form.set_domain(TTHA2DOMAIN)
        login_form.submit()