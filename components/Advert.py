from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from constants import WebDriverSettings

__author__ = 'Ivan'


class Advert(Component):
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    URL = 'input[data-name="url"]'
    SUBMIT = '.banner-form__save-button'
    IMAGE_PATH = 'input[data-name="image"]'
    BIG_IMAGE_PATH = 'input[data-name="promo_image"]'
    IMAGE = '.banner-preview__wrapper[data-name="image"]'
    BIG_IMAGE = '.banner-preview__wrapper[data-name="promo_image"]'

    def set_title(self, title):
        edit_box = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                 WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.TITLE)
        )
        edit_box.send_keys(title)

    def set_text(self, text):
        text_area = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                  WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        text_area.send_keys(text)

    def set_url(self, url):
        edit_box = WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT,
                                 WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )[1]
        edit_box.send_keys(url)

    def set_image(self, path_to_image):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE_PATH)
        )
        element.send_keys(path_to_image)

    def set_big_image(self, path_to_big_image):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BIG_IMAGE_PATH)
        )
        element.send_keys(path_to_big_image)


    def loading_image(self, driver):
        image = driver.find_element_by_css_selector(self.IMAGE)
        return WebDriverWait(image, WebDriverSettings.WEBDRIVER_TIMEOUT,
                             WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.value_of_css_property("background-image") is not None
        )

    def loading_big_image(self, driver):
        big_image = driver.find_element_by_css_selector(self.BIG_IMAGE)
        return WebDriverWait(big_image, WebDriverSettings.WEBDRIVER_TIMEOUT,
                             WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: d.value_of_css_property("background-image") is not None
        )

    def wait_for_image_loading(self):
        WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: self.loading_image(d)
        )

    def wait_for_big_image_loading(self):
        WebDriverWait(self.driver, WebDriverSettings.WEBDRIVER_TIMEOUT, WebDriverSettings.WEBDRIVER_POLL_FREQUENCY).until(
            lambda d: self.loading_big_image(d)
        )

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()