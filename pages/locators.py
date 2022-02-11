from selenium.webdriver.common.by import By

# Задаем локаторы для страницы поиска
class SearchPageLocators():
    SEARCH = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup_visible") 
    ENTER = (By.CSS_SELECTOR, "[type='submit']")
    IMAGE = (By.CSS_SELECTOR, "[data-id='images']")
    
# Локаторы для страницы результатов поиска
class SearchResultsLocators():
    RESULTS = (By.CSS_SELECTOR, "[data-cid='3']") 

# Локаторы для страницы с картинками
class SearchImages():
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 a")
    TITLE_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 img")
    FIRST_IMAGE = (By.CSS_SELECTOR, "[data-type='o'] a")
    NEXT_IMAGE = (By.CSS_SELECTOR, ".CircleButton_type_next")
    TITLE_IMAGE = (By.CSS_SELECTOR, ".MMOrganicSnippet-TitleWrap a")
    PREV_IMAGE = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    

