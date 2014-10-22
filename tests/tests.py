import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from constants import Credentials
from page_objects.campaign_page import CampaignPage
from page_objects.create_page import CreatePage
from page_objects.edit_campaign_page import EditCampaignPage
from page_objects.login_page import LoginPage

__author__ = 'Ivan'


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        LoginPage(self.driver).login()
        self.create_page = CreatePage(self.driver)
        # self.edit_page = EditPage(self.driver)
        self.create_page.open()


    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        email = self.create_page.top_menu.get_email()
        self.assertEquals(Credentials.TTHA2LOGIN + Credentials.DOMAIN, email)

    def test_campaign_create(self):
        self.create_page.campaign_settings.set_campaign_name("NAME")
        self.create_page.campaign_settings.set_group_event_videochannel()
        self.create_page.campaign_settings.set_odnoklassniki_mobile()

        self.create_page.advert.set_image(os.path.abspath("test.jpg"))
        self.create_page.advert.set_big_image(os.path.abspath("test2.jpg"))
        self.create_page.advert.set_title("TITLE")
        self.create_page.advert.set_text("text")
        self.create_page.advert.set_url("http://www.odnoklassniki.ru/event/15")
        self.create_page.advert.wait_for_image_loading()
        self.create_page.advert.wait_for_big_image_loading()
        self.create_page.advert.submit()
        self.create_page.create_campaign_button.click()

        campaigns_page = CampaignPage(self.driver)
        campaigns_page.edit_campaign_button.click()

        edit_page = EditCampaignPage(self.driver)
        campaign_name = edit_page.campaign_properties.get_campaign_name()
        edit_page.save_changes_button.click()
        campaigns_page.delete_campaign_button.click()
        self.assertEqual(campaign_name, "NAME")

    def test_high_and_mid_incomes(self):
        self.create_page.campaign_settings.set_campaign_name("NAME")
        self.create_page.campaign_settings.set_group_event_videochannel()
        self.create_page.campaign_settings.set_odnoklassniki_mobile()

        self.create_page.advert.set_image(os.path.abspath("test.jpg"))
        self.create_page.advert.set_big_image(os.path.abspath("test2.jpg"))
        self.create_page.advert.set_title("TITLE")
        self.create_page.advert.set_text("text")
        self.create_page.advert.set_url("http://www.odnoklassniki.ru/event/15")
        self.create_page.advert.wait_for_image_loading()
        self.create_page.advert.wait_for_big_image_loading()
        self.create_page.advert.submit()
        self.create_page.income_checkbox_group.set_income()
        self.create_page.income_checkbox_group.set_high_income()
        self.create_page.income_checkbox_group.set_mid_income()
        self.create_page.create_campaign_button.click()

        campaigns_page = CampaignPage(self.driver)
        campaigns_page.edit_campaign_button.click()

        edit_page = EditCampaignPage(self.driver)
        high_income_checked = edit_page.income_checkbox_group.assert_high_checked()
        mid_income_checked = edit_page.income_checkbox_group.assert_mid_checked()
        low_income_checked = edit_page.income_checkbox_group.assert_low_checked()
        edit_page.save_changes_button.click()
        campaigns_page.delete_campaign_button.click()
        self.assertTrue(high_income_checked)
        self.assertTrue(mid_income_checked)
        self.assertFalse(low_income_checked)

    def test_low_incomes(self):
        self.create_page.campaign_settings.set_campaign_name("NAME")
        self.create_page.campaign_settings.set_group_event_videochannel()
        self.create_page.campaign_settings.set_odnoklassniki_mobile()

        self.create_page.advert.set_image(os.path.abspath("test.jpg"))
        self.create_page.advert.set_big_image(os.path.abspath("test2.jpg"))
        self.create_page.advert.set_title("TITLE")
        self.create_page.advert.set_text("text")
        self.create_page.advert.set_url("http://www.odnoklassniki.ru/event/15")
        self.create_page.advert.wait_for_image_loading()
        self.create_page.advert.wait_for_big_image_loading()
        self.create_page.advert.submit()
        self.create_page.income_checkbox_group.set_income()
        self.create_page.income_checkbox_group.set_low_income()
        self.create_page.create_campaign_button.click()

        campaigns_page = CampaignPage(self.driver)
        campaigns_page.edit_campaign_button.click()

        edit_page = EditCampaignPage(self.driver)
        high_income_checked = edit_page.income_checkbox_group.assert_high_checked()
        mid_income_checked = edit_page.income_checkbox_group.assert_mid_checked()
        low_income_checked = edit_page.income_checkbox_group.assert_low_checked()
        edit_page.save_changes_button.click()
        campaigns_page.delete_campaign_button.click()
        self.assertFalse(high_income_checked)
        self.assertFalse(mid_income_checked)
        self.assertTrue(low_income_checked)


    def test_moscow_group(self):
        self.create_page.campaign_settings.set_campaign_name("NAME")
        self.create_page.campaign_settings.set_group_event_videochannel()
        self.create_page.campaign_settings.set_odnoklassniki_mobile()

        self.create_page.advert.set_image(os.path.abspath("test.jpg"))
        self.create_page.advert.set_big_image(os.path.abspath("test2.jpg"))
        self.create_page.advert.set_title("TITLE")
        self.create_page.advert.set_text("text")
        self.create_page.advert.set_url("http://www.odnoklassniki.ru/event/15")
        self.create_page.advert.wait_for_image_loading()
        self.create_page.advert.wait_for_big_image_loading()
        self.create_page.advert.submit()
        self.create_page.where_tree.set_moscow_group()
        self.create_page.create_campaign_button.click()

        campaigns_page = CampaignPage(self.driver)
        campaigns_page.edit_campaign_button.click()

        edit_page = EditCampaignPage(self.driver)
        edit_page.where_tree.set_region()
        moscow_node = edit_page.where_tree.assert_moscow_node_checked()
        spb_node = edit_page.where_tree.assert_spb_node_checked()
        penza_node = edit_page.where_tree.assert_penza_node_checked()
        edit_page.save_changes_button.click()
        campaigns_page.delete_campaign_button.click()
        self.assertTrue(moscow_node)
        self.assertFalse(spb_node)
        self.assertFalse(penza_node)

    def test_penza_and_spb(self):
        self.create_page.campaign_settings.set_campaign_name("NAME")
        self.create_page.campaign_settings.set_group_event_videochannel()
        self.create_page.campaign_settings.set_odnoklassniki_mobile()

        self.create_page.advert.set_image(os.path.abspath("test.jpg"))
        self.create_page.advert.set_big_image(os.path.abspath("test2.jpg"))
        self.create_page.advert.set_title("TITLE")
        self.create_page.advert.set_text("text")
        self.create_page.advert.set_url("http://www.odnoklassniki.ru/event/15")
        self.create_page.advert.wait_for_image_loading()
        self.create_page.advert.wait_for_big_image_loading()
        self.create_page.advert.submit()
        self.create_page.where_tree.uncheck_all_nodes()
        self.create_page.where_tree.set_region()
        self.create_page.where_tree.set_spb_node()
        self.create_page.where_tree.set_penza_node()
        self.create_page.create_campaign_button.click()

        campaigns_page = CampaignPage(self.driver)
        campaigns_page.edit_campaign_button.click()

        edit_page = EditCampaignPage(self.driver)
        edit_page.where_tree.set_region()
        moscow_node = edit_page.where_tree.assert_moscow_node_checked()
        spb_node = edit_page.where_tree.assert_spb_node_checked()
        penza_node = edit_page.where_tree.assert_penza_node_checked()
        edit_page.save_changes_button.click()
        campaigns_page.delete_campaign_button.click()
        self.assertFalse(moscow_node)
        self.assertTrue(spb_node)
        self.assertTrue(penza_node)

