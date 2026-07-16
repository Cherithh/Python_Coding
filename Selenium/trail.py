from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class BuyingItem:
    def fromflipkart(self):
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        close_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='✕']")))
        close_btn.click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,"//*[text()='flipkart']").is_displayed()
        mouse = driver.find_element(By.XPATH,"//input[@class='nw1UBF v1zwn25']")
        mouse.send_keys("Foxsky 109 cm (43 inch) QLED Full HD Smart Android TV 2026 Edition with 2.1 CH Audio System Tuned by 3")
        mouse.send_keys(Keys.ENTER)
        parent_handle = driver.current_window_handle
        mouse_search = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Foxsky 109 cm (43 inch) QLED Full HD Smart Android TV 2026 Edition with 2.1 CH Audio System Tuned by 3']")))
        mouse_search.click()
        windows  = driver.window_handles
        for window in windows:
            if window != parent_handle:
                driver.switch_to.window(window)
                driver.find_element(By.XPATH,"//div[normalize-space()='Buy now']").click()

        time.sleep(3)
        driver.close()

buymouse = BuyingItem()
buymouse.fromflipkart()