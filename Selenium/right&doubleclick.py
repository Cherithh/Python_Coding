from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class right_double:
    def click(self):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        double_click = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
        actions = ActionChains(driver)
        actions.double_click(double_click).perform()
        time.sleep(3)
        alerttext = driver.switch_to.alert.text
        print(alerttext)
        driver.switch_to.alert.accept()
        time.sleep(3)
        right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        actions.context_click(right_click).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-quit']").click()
        alerttext2 = driver.switch_to.alert.text
        print(alerttext2)
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.close()

clicking = right_double()
clicking.click()
