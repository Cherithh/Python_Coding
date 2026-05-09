from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class iframes:
    def iframe(self):
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[@id='runbtn']").click()
        driver.switch_to.frame("iframeResult")
        driver.switch_to.parent_frame()
        time.sleep(2)


iframess = iframes()
iframess.iframe()