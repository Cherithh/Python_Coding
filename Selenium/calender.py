from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

class calenders:
    def date(self):
        driver.get("https://www.yatra.com/%3Fredirect%3Dno")
        time.sleep(5)
        all_dates = driver.find_elements(By.XPATH,"https://www.yatra.com/%3Fredirect%3Dno")
        for dates in all_dates:
            if dates.get_attribute("date==date") == ("05/09/2025"):
                dates.click()
                break

time.sleep(5)
calen = calenders()
calen.date()