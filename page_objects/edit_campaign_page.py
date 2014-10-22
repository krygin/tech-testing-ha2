from components.campaign_properties import CampaignProperties
from components.income_checkbox_group import IncomeCheckboxGroup
from components.save_changes_button import SaveChangesButton
from components.where_tree import WhereTree
from page_objects.page import Page

__author__ = 'Ivan'


class EditCampaignPage(Page):

    @property
    def campaign_properties(self):
        return CampaignProperties(self.driver)

    @property
    def save_changes_button(self):
        return SaveChangesButton(self.driver)

    @property
    def income_checkbox_group(self):
        return IncomeCheckboxGroup(self.driver)

    @property
    def where_tree(self):
        return WhereTree(self.driver)