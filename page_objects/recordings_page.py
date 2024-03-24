
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.locators.recordings_page import Locators
from utils.custom_wait import custom_wait

logger = logging.getLogger(__file__)


class RecordingsPage(BasePage):
   # items_titles = 'inventory_item_name '
   ## c = '.inventory_item_price '
  #  buttons_add_to_card = "//button[contains(@data-tests, 'add-to-cart')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def find_upload_btn(self, timeout=3):
        self._element_is_visible(locator=(By.CSS_SELECTOR, self.locators.upload_media_btn_css_locator), timeout=timeout)
        return self

    def get_items_titles(self) -> list[str]:
        return self.get_texts(locator=(By.CLASS_NAME, self.items_titles))

    def get_items_prices(self) -> list[str]:
        return self.get_texts(locator=(By.CSS_SELECTOR, self.items_prices))

    def scroll_to_by_js_last_item(self, number):
        el = self.get_element_by_number(locator=(By.XPATH, self.buttons_add_to_card), number=number)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def scroll_by_selenium_to_last_item(self, number):
        el = self.get_element_by_number(locator=(By.XPATH, self.buttons_add_to_card), number=number)

        logger.info(f'Found {self.buttons_add_to_card} number {number}')

        ActionChains(driver=self.driver).scroll_to_element(el).perform()

    def scroll_by_selenium_to_last_item_with_custom_wait(self, number):
        el = custom_wait(driver=self.driver, el_numbers=number, locator=(By.XPATH, self.buttons_add_to_card))[number - 1]
        ActionChains(driver=self.driver).scroll_to_element(el).perform()