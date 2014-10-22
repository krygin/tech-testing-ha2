from components.component import Component

__author__ = 'Ivan'


class CreateCampaignButton(Component):
    SUBMIT = ".main-button-new"

    def click(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()