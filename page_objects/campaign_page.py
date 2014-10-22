from components.campaign_properties import CampaignProperties
from components.delete_campaign_button import DeleteCampaignButton
from components.edit_campaign_button import EditCampaignButton
from page_objects.page import Page

__author__ = 'Ivan'



class CampaignPage(Page):
    PATH = '/ads/campaigns/'


    @property
    def delete_campaign_button(self):
        return DeleteCampaignButton(self.driver)

    @property
    def edit_campaign_button(self):
        return EditCampaignButton(self.driver)