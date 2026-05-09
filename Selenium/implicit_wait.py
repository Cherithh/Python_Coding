from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class impwait:
    def implicit(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
obj = impwait()
obj.implicit()
