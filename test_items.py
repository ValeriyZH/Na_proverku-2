import pytest 
from selenium import webdriver 
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

  
class TestMainPage1():
        
    def test_language(self, browser): 
        link_product = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link_product)
        time.sleep(10)
        yes_submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        yes_submit.click()
        assert True, "Кнопка недоступна"      
                 
if __name__ == "__main__":
    test_language()  
