from components.advert import Advert
from components.campaign_settings import CampaignSettings
from components.create_campaign_button import CreateCampaignButton
from components.income_checkbox_group import IncomeCheckboxGroup
from components.top_menu import TopMenu
from components.where_tree import WhereTree
from page_objects.page import Page

__author__ = 'Ivan'


class CreatePage(Page):
    PATH = "/ads/create/"

    @property
    def top_menu(self):
        return TopMenu(self.driver)


    @property
    def income_checkbox_group(self):
        return IncomeCheckboxGroup(self.driver)

    @property
    def campaign_settings(self):
        return CampaignSettings(self.driver)

    @property
    def advert(self):
        return Advert(self.driver)

    @property
    def create_campaign_button(self):
        return CreateCampaignButton(self.driver)

    @property
    def where_tree(self):
        return WhereTree(self.driver)