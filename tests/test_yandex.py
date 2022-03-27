import time
from typing import List

from selenium import webdriver

from ..yandex_pages import YandexSearch, ImagesPage

URL = "tensor.ru"
REQUIRED_LINKS_NUMBER = 5
IMAGES_URL = 'https://yandex.ru/images/'


def is_required_url_in_links(links: List[str]) -> bool:
    return all([URL in link for link in links[:REQUIRED_LINKS_NUMBER]])


def test_yandex_search(browser):
    yandex_search = YandexSearch(browser)
    try:
        yandex_search.go_to_site()

        yandex_search.find_search_field()
        assert yandex_search.search_field, 'Не удалось найти поисковое поле на странице '

        yandex_search.enter_word("Тензор")
        suggestions = yandex_search.find_suggestions()
        assert suggestions, 'Окно подсказок не появилось после ввода текста в поисковое поле'

        yandex_search.click_on_the_search_button()
        links = yandex_search.get_results_links()

        assert is_required_url_in_links(links), f'Первые {REQUIRED_LINKS_NUMBER} результатов не содержат ссылку "{URL}"'
    except AssertionError as err:
        yandex_search.logger.exception(err, exc_info=False)
        raise err


def test_images(browser: webdriver):
    yandex_images = ImagesPage(browser)
    try:
        yandex_images.go_to_site()

        images_link = yandex_images.get_images_navigation_bar()
        images_link.click()

        yandex_images.driver.switch_to.window(yandex_images.driver.window_handles[-1])
        cur_url = yandex_images.driver.current_url
        assert cur_url.startswith(IMAGES_URL + '?'), 'Некорректный адрес страницы.'

        first_images_category = yandex_images.get_first_category()
        first_images_category_text = yandex_images.get_first_category_text().text
        first_images_category.click()

        search_field_text = yandex_images.find_search_field().get_attribute("value")
        assert search_field_text == first_images_category_text, f'В поисковом поле неправильный текст.'

        first_image = yandex_images.get_first_image()
        first_image.click()
        time.sleep(1)

        image_src = yandex_images.get_current_image().get_attribute('src')

        yandex_images.press_button_next()
        time.sleep(1)

        yandex_images.press_button_back()
        cur_image_src = yandex_images.get_current_image().get_attribute('src')
        assert image_src == cur_image_src, f'После возвращения на предыдущую страницу, получили другое изображение.'
        time.sleep(1)

    except AssertionError as err:
        yandex_images.logger.exception(err, exc_info=False)
        raise err
