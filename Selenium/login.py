from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

def login():

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")     
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    print(driver.title)
    

login()