from selenium import webdriver
driver = webdriver.Chrome()
import time

class browser:
    def open_browser(self):

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")     
        driver.maximize_window()
        time.sleep(5)
        driver.close  


Webbrowser = browser()
Webbrowser.open_browser()