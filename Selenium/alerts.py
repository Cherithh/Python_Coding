from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class alerts:
    def alert(self):
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
        alertsss = driver.switch_to.alert.text
        print(alertsss)
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.close()


alerts1 = alerts()
alerts1.alert()
