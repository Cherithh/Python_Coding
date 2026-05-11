from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class expwait:
    def explicit(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        wait = WebDriverWait(driver,10)
        user = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
        user.send_keys("admin")

obj = expwait()
obj.explicit()   