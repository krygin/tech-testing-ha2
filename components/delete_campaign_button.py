from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component

__author__ = 'Ivan'



class DeleteCampaignButton(Component):
    BUTTON = '.control__preset_delete'
    BLOCK = '.control_campaign .control__preset_delete'

    def click(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        element.click()