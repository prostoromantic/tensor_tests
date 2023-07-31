from YandexImages import YandexImages
from YandexSearch import YandexSearch
from loguru import logger


def test_yandex_search(browser):
    ''' Поиск в яндексе '''

    yandex_main_page = YandexSearch(browser)
    # Зайти на https://ya.ru/
    yandex_main_page.browser_get()

    # Проверить наличия поля поиска | Ввести в поиск Тензор
    yandex_main_page.enter_word('Тензор')

    # Проверить, что появилась таблица с подсказками (suggest)
    yandex_main_page.check_table_menu()

    # Нажать enter
    yandex_main_page.send_keys_enter()

    # Проверить, что появилась страница результатов поиска
    yandex_main_page.get_search_result()

    # Проверить 1 ссылка ведет на сайт tensor.ru
    link = yandex_main_page.get_link()
    assert link.get_attribute('href') == 'https://tensor.ru/'


def test_yandex_images(browser):
    ''' Картинки на яндексе '''

    yandex_main_page = YandexImages(browser)
    # Зайти на ya.ru
    yandex_main_page.browser_get()

    # Проверить, что кнопка меню присутствует на странице | Открыть меню, выбрать “Картинки”
    current_url = yandex_main_page.find_menu()

    # Проверить, что перешли на url https://yandex.ru/images/
    logger.debug(f'Current Url - {current_url}')
    assert current_url == 'https://yandex.ru/images/'

    # Открыть первую категорию
    search_input, category_name = yandex_main_page.check_category()

    # Проверить, что название категории отображается в поле поиска
    logger.debug(f"Category name - {category_name}, Act category - {search_input.get_attribute('value')}")
    assert search_input.get_attribute('value') == category_name

    # Открыть 1 картинку | Проверить, что картинка открылась
    image = yandex_main_page.open_image().get_attribute('src')
    logger.debug(f'First image - {image}')

    # Нажать кнопку вперед
    image_next = yandex_main_page.forward().get_attribute('src')

    # Проверить, что картинка сменилась
    logger.debug(f'Second image - {image_next}')
    assert image != image_next

    # Нажать назад
    image_prev = yandex_main_page.back().get_attribute('src')

    # Проверить, что картинка осталась из шага 8
    logger.debug(f'Third image - {image_prev}')
    assert image == image_prev
