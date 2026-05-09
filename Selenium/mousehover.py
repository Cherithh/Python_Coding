from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class mousehovers:
    def mouse(self):
        driver.get("https://www.yatra.com/%3Fredirect%3Dno")
        driver.maximize_window()
        more = driver.find_element(By.XPATH,"//span[@class='more-arr']")
        action = ActionChains(driver)
        action.move_to_element(more).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_cruise']").click()
        time.sleep(3)



mousehover = mousehovers()
mousehover.mouse()
