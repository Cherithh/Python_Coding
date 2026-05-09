from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

class checkbox:
    def checkboxes(self):
        driver.get("https://getcssscan.com/css-checkboxes-examples")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//label[@for='example-1']").click()
        elem = driver.find_element(By.XPATH,"//label[@for='example-1']").is_displayed()
        print(elem)
        time.sleep(5)
        elem2 = driver.find_element(By.XPATH,"//input[@class='sc-gJwTLC ikxBAC']").is_selected()
        print(elem2)
        driver.close()

check = checkbox()
check.checkboxes()

