from BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class YandexImagesSelectors:
    search_input = (By.ID, 'text')
    all_service = (By.CLASS_NAME, 'services-suggest__icons-more')
    images = (By.CSS_SELECTOR, '[aria-label=Картинки]')
    images_div = (By.CLASS_NAME, 'PopularRequestList')
    category_block = (By.CLASS_NAME, 'PopularRequestList-Preview')
    search_input_images = (By.NAME, 'text')
    image = (By.CLASS_NAME, 'serp-item__link')
    media_viewer = (By.CLASS_NAME, 'MMImage-Origin')
    button_next = (By.CLASS_NAME, 'CircleButton_type_next')
    button_prev = (By.CLASS_NAME, 'CircleButton_type_prev')


class YandexImages(BasePage):

    def find_menu(self):
        self.click_to_element(YandexImagesSelectors.search_input, 'Не удалось найти поиск')
        self.click_to_element(YandexImagesSelectors.all_service, 'Не удалось найти "Все сервисы"')
        self.click_to_element(YandexImagesSelectors.images, 'Не удалось найти "Картинки" в меню')
        self.switch_handles()
        return self.browser.current_url

    def check_category(self):
        category_name = self.click_to_element(YandexImagesSelectors.category_block, 'Не удалось найти категорию картинки')
        return self.find_element(YandexImagesSelectors.search_input_images, 'Не удалось найти поиск для картинок'), category_name.text

    def enter_word(self, phrase):
        search_field = self.find_element(YandexImagesSelectors.search_input, 'Не удалось найти поиск')
        search_field.send_keys(phrase)
        return search_field

    def open_image(self):
        self.click_to_element(YandexImagesSelectors.image, 'Не удалось найти картинку')
        time.sleep(1)
        return self.find_element(YandexImagesSelectors.media_viewer, 'Не удалось найти картинку')

    def forward(self):
        self.click_to_element(YandexImagesSelectors.button_next, 'Не удалось найти кнопку вперед')
        time.sleep(1)
        return self.find_element(YandexImagesSelectors.media_viewer, 'Не удалось найти картинку')

    def back(self):
        self.click_to_element(YandexImagesSelectors.button_prev, 'Не удалось найти кнопку назад')
        time.sleep(1)
        return self.find_element(YandexImagesSelectors.media_viewer, 'Не удалось найти картинку')