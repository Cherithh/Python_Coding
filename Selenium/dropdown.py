from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class dropdowns:
    def drop(self):
        driver.get("https://www.salesforce.com/form/signup/elf-v2-login")
        driver.maximize_window()
        drpdown = driver.find_element(By.NAME,"CompanyEmployees")
        forselect = Select(drpdown)
        forselect.select_by_index(2)
        time.sleep(3)
        driver.close()

dropdown = dropdowns()
dropdown.drop()