from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class auto:
    def suggestions(self):
        driver.get("https://www.yatra.com/%3Fredirect%3Dno")
        driver.maximize_window()
        new = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        new.click()
        new.send_keys("Delhi")
        time.sleep(2)
        new.send_keys(Keys.ENTER)
        time.sleep(5)
        new2 = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        new2.click()
        new2.send_keys("Mum")
        search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/div/li")
        print(len(search_results))
        for search in search_results:
            # print(search.text)
            if "Mumbai (BOM)" in search.text:
                search.click()
                time.sleep(5)
                break
        
        driver.close()

autosuggestions = auto()
autosuggestions.suggestions()