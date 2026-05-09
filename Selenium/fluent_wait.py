from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class fluentwait:
    def fluent(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        waits = WebDriverWait(driver,10,5,ignored_exceptions=NoSuchElementException)
        username = waits.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
        username.send_keys("Admin")

obj = fluentwait()
obj.fluent()   