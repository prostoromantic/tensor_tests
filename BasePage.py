from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from loguru import logger


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://ya.ru/'

    def find_element(self, selector, message):
        logger.info(f'Find element - {selector}')
        return WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                selector
            ),
            message=message
        )

    def browser_get(self):
        return self.browser.get(self.url)

    def click_to_element(self, selector, message):
        element = self.find_element(selector, message)
        element.click()
        logger.info(f'Click to - {selector}')
        return element

    def switch_handles(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])
