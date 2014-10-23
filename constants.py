import os

__author__ = 'Ivan'


class Credentials(object):
    TTHA2LOGIN = 'tech-testing-ha2-15'
    TTHA2PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'


class WebDriverSettings(object):
    WEBDRIVER_TIMEOUT = 30
    WEBDRIVER_POLL_FREQUENCY = 0.1


class IncomeCheckboxGroupElementSelectors(object):
    HIGH_LEVEL = "#income_group-9288"
    MID_LEVEL = "#income_group-9287"
    LOW_LEVEL = "#income_group-9286"