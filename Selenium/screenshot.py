from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class screenshots:
    def screen(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)
        driver.save_screenshot("C://Users/cheri/projects/cherith/.pytest_cache/basic_python_problems/Selenium/screenshot.png")
        time.sleep(3)

screenshot = screenshots()
screenshot.screen()