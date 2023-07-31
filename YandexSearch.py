from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexSearchSelectors:
    search_input = (By.ID, 'text')
    suggest = (By.CLASS_NAME, 'mini-suggest__popup-content')
    search_result = (By.ID, 'search-result')
    link = (By.CLASS_NAME, 'OrganicTitle-Link')


class YandexSearch(BasePage):

    def enter_word(self, phrase):
        search_field = self.find_element(YandexSearchSelectors.search_input, 'Не удалось найти поиск')
        search_field.send_keys(phrase)
        return search_field

    def send_keys_enter(self):
        return self.find_element(YandexSearchSelectors.search_input, 'Не удалось найти поиск').send_keys(Keys.ENTER)

    def check_table_menu(self):
        return self.find_element(YandexSearchSelectors.suggest, 'Не удалось найти таблицу с подсказками')

    def get_search_result(self):
        return self.find_element(YandexSearchSelectors.search_result, 'Не обнаружены результаты поиска')

    def get_link(self):
        return self.find_element(YandexSearchSelectors.link, 'Не обнаружен результат поиска')