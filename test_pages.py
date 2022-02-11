from lib2to3.pgen2 import driver
from pages.search_yandex import SearchPage, SearchResults, SearchImage
import time


# Тест-кейс проверки наличия поля поиска
def test_search_field_yandex_is(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_search()

# Тест-кейс проверки наличия таблицы suggest
def test_suggest_table_yandex_is(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.input()                     # вводим "Тензор"
    page.should_be_suggest()        # проверяем наличие поля suggest

# Тест-кейс проверки наличия результатов поиска по слову "Тензор"
def test_results_search_tenzor_is(browser):
    link = "https://yandex.ru/"
    page = SearchResults(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.input()                     # вводим "Тензор"
    page.go_to_search()             # Поиск
    page.should_be_results()        # проверяем что есть результаты

# Тест-кейс проверки того, что в первых пяти результатах есть ссылка на Тензор
def test_results_url_tenzor_is(browser):
    link = "https://yandex.ru/"
    page = SearchResults(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.input()                     # вводим "Тензор"
    page.go_to_search()             # Поиск
    page.should_be_url_tenzor()        # проверяем что есть ссылка


# Тест-кейс проверяет наличие ссылки на картинки
def test_image_is(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_image()        # проверяем что есть ссылка на картинки


# Тест-кейс проверяет что перешли по ссылке Картинки
def test_image_go(browser):
    link = "https://yandex.ru/"
    page = SearchPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу       
    image_page = page.go_to_image()  # кликаем по ссылке Картинки
    image_page.should_url_is_correct()


# Тест-кейс проверяет что правильно зашли в первую категорию картинок
def test_first_category_right(browser):
    link = "https://yandex.ru/images/?utm_source=main_stripe_big"
    page = SearchImage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  # открываем страницу                      
    page.go_to_category() # Кликаем по первой категории
    page.should_right_text() # Проверяем что открылась верная


# Тест-кейс открывает первую картинку и проверяет что открылась
def test_first_image(browser):
    link = "https://yandex.ru/images/?utm_source=main_stripe_big"
    page = SearchImage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  # открываем страницу                      
    page.go_to_category() # Кликаем по первой категории
    url1 = page.go_first_image()
    page_image = SearchImage(browser=browser, url=browser.current_url)   
    assert url1 == page_image.url, "Открылась не та картинка"
 
# Тест-кейс открывает следующую картинку и проверяет что другая
def test_next_image(browser):
    link = "https://yandex.ru/images/?utm_source=main_stripe_big"
    page = SearchImage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  # открываем страницу                      
    page.go_to_category() # Кликаем по первой категории
    page.go_first_image() # Кликаем по первой картинке
    url1 = browser.current_url #Запоминаем текущий адрес первой картинки
    page.go_next_image()  # Переходим на вторую
    page.url = browser.current_url
    assert url1 != page.url, "Картинка не изменилась"


# Тест-кейс открывает первую картинку, затем вторую, первую и проверяет что это та же
def test_check_image_first(browser):
    link = "https://yandex.ru/images/?utm_source=main_stripe_big"
    page = SearchImage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  # открываем страницу                      
    page.go_to_category() # Кликаем по первой категории
    page.go_first_image() # Кликаем по первой картинке
    title1 = page.member_image() # Запоминаем название картинки
    page.go_next_image()  # вперед
    page.go_prev_image() # назад
    assert title1 == page.member_image(), "Другая картинка"


  



    
