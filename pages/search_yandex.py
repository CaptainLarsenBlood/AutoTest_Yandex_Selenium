from conftest import browser
from pages.base_page import BasePage
#from selenium.webdriver.common.by import By
from pages.locators import SearchPageLocators, SearchResultsLocators, SearchImages
from selenium.webdriver.common.by import By

# Методы для страницы поиска
class SearchPage(BasePage): 

    def go_to_search(self):
        go_search = self.browser.find_element(*SearchPageLocators.ENTER)
        go_search.click()
    
    def go_to_image(self):
        go_image = self.browser.find_element(*SearchPageLocators.IMAGE)
        go_image.click()         
        return SearchImage(browser=self.browser, url=self.browser.current_url) 
    
    def input(self):
        self.browser.find_element(*SearchPageLocators.SEARCH).send_keys("Тензор") 

    def should_be_search(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH), "Поле поиска отсутствует"
    
    def should_be_suggest(self):
        assert self.is_element_present(*SearchPageLocators.SUGGEST), "Таблица с подсказками отсутствует"
    
    def should_be_image(self):
        assert self.is_element_present(*SearchPageLocators.IMAGE), "Нет ссылки на картинки"

    
    
    
# Методы для страницы результатов поиска
class SearchResults(SearchPage):

    def should_be_results(self):
        assert self.is_element_present(*SearchResultsLocators.RESULTS), "Нет результатов поиска"

    # Проверяем что ссылка на тензор есть в первых пяти результатах (при отсутсвии такой ссылки долго проверяет - сек 15, надо будет улучшить...)
    def should_be_url_tenzor(self):

        flag = False # флаг наличия ссылки на тензор
        for url in range(5):
            tenzor_url = "[data-cid='{}'] a[href = 'https://tensor.ru/']".format(url)	#формируем селектор
            if self.is_element_present(By.CSS_SELECTOR, tenzor_url): 
                flag = True
                break
        assert flag, "В первых пяти результатах нет ссылки на тензор"



# Методы для страницы с картинками
class SearchImage(BasePage):
    
    def should_url_is_correct(self):

        print(self.browser.current_url)
        assert "login" in self.url, "URL не соответствует https://yandex.ru/images/"
        
    
    def go_to_category(self):

        self.element = self.browser.find_element(*SearchImages.TITLE_CATEGORY) 
        self.title = self.element.get_attribute("alt") # Попутно запоминаем как называлась категория изображений

        go_category = self.browser.find_element(*SearchImages.FIRST_CATEGORY)
        go_category.click() 

    def should_right_text(self):

        assert self.browser.find_element(By.XPATH,"//title[contains(text(), '{}')]".format(self.title)), "Открылась неправильная категория"
    
    def go_first_image(self):

        self.element2 = self.browser.find_element(*SearchImages.FIRST_IMAGE) 
        self.title2 = self.element2.get_attribute("href") # Попутно запоминаем url картинки

        go_first = self.browser.find_element(*SearchImages.FIRST_IMAGE)
        go_first.click() 

        return self.title2
        
    def go_next_image(self):

        go_next = self.browser.find_element(*SearchImages.NEXT_IMAGE)
        go_next.click() 
    
    def member_image(self):
        title = self.browser.find_element(*SearchImages.TITLE_IMAGE)
        return title
        #print(title.text)
    
    def go_prev_image(self):
        go_prev = self.browser.find_element(*SearchImages.PREV_IMAGE)
        go_prev.click() 


    
             
      	


