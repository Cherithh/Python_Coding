from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

class hidden_elements:
    def elements(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        elem = driver.find_element(By.XPATH,"//div[@id='myDIV'] ").is_displayed()
        print(elem)
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@class='ws-btn w3-hover-black w3-dark-grey'] ").click()
        elem2 = driver.find_element(By.XPATH,"//div[@id='myDIV'] ").is_displayed()
        time.sleep(3)
        print(elem2)
        driver.close()

elements1 = hidden_elements()
elements1.elements()