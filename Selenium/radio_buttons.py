from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

class radiobutton:
    def radiobuttons(self):
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH,"//input[@id='html']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@id='javascript']").click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH,"//input[@id='html']").is_selected()
        print(elem)
        elem2 = driver.find_element(By.XPATH,"//input[@id='javascript']").is_selected()
        print(elem2)
        driver.close()

radio = radiobutton()
radio.radiobuttons()
