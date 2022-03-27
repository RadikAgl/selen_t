from .base import BasePage
from selenium.webdriver.common.by import By

from .logger import setup_logger


class ImagesPage(BasePage):

    XPATH_YANDEX_NAVIGATION_IMAGES = (By.XPATH, "//a[@data-id='images']")
    XPATH_SEARCH_FIELD = (By.XPATH, '//input[@class="input__control mini-suggest__input"]')
    XPATH_FIRST_CATEGORY_TEXT = (By.XPATH, '//div[contains(@class, "PopularRequestList-Item_pos_0")]//div['
                                           '@class="PopularRequestList-SearchText"]')
    XPATH_FIRST_IMAGE = (By.XPATH, '//div[contains(@class, "serp-item_pos_0")]//img')

    LOCATOR_IMAGES_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_CURRENT_IMAGE = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_IMAGE_BUTTON_NEXT = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_IMAGE_BUTTON_BACK = (By.CLASS_NAME, "CircleButton_type_prev")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = setup_logger(type(self).__name__, f'logs/logs-{type(self).__name__}.log')
        self.logger.info('Начало автотестирования')

    def get_images_navigation_bar(self):
        return self.find_element(self.XPATH_YANDEX_NAVIGATION_IMAGES)

    def get_first_category(self):
        return self.find_element(self.LOCATOR_IMAGES_FIRST_CATEGORY)

    def find_search_field(self):
        return self.find_element(self.XPATH_SEARCH_FIELD)

    def get_first_category_text(self):
        return self.find_element(self.XPATH_FIRST_CATEGORY_TEXT)

    def get_first_image(self):
        return self.find_element(self.XPATH_FIRST_IMAGE)

    def press_button_next(self):
        self.find_element(self.LOCATOR_IMAGE_BUTTON_NEXT).click()

    def press_button_back(self):
        self.find_element(self.LOCATOR_IMAGE_BUTTON_BACK).click()

    def get_current_image(self):
        return self.find_element(self.LOCATOR_CURRENT_IMAGE)


class YandexSearch(BasePage):

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGESTIONS = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

    XPATH_YANDEX_SEARCH_RESULTS = (By.XPATH, '//li[@class="serp-item desktop-card"]//div[(contains(@class, '
                                             '"Organic-Subtitle"))]//a[not(contains(@class, '
                                             '"Sitelinks-Title"))]')

    def __init__(self, driver):
        super().__init__(driver)
        self.search_field = None
        self.logger = setup_logger(type(self).__name__, f'logs/logs-{type(self).__name__}.log')
        self.logger.info('Начало автотестирования')

    def find_search_field(self):
        self.search_field = self.find_element(self.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):
        self.search_field.click()
        self.search_field.send_keys(word)

    def find_suggestions(self):
        return self.find_element(self.LOCATOR_YANDEX_SEARCH_SUGGESTIONS)

    def get_results_links(self):
        result = self.find_elements(self.XPATH_YANDEX_SEARCH_RESULTS)
        return [link.get_attribute("href") for link in result]

    def click_on_the_search_button(self):
        return self.find_element(self.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()


