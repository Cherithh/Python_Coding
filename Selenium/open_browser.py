from selenium import webdriver
driver = webdriver.Chrome()
import time

def open_browser():

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")     
    driver.maximize_window()
    time.sleep(5)
    driver.close  

open_browser()