from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time


class multiple_windows:
    def windows(self):
        driver.get("https://www.yatra.com/%3Fredirect%3Dno")
        driver.maximize_window()
        parent_window = driver.current_window_handle
        print(parent_window)
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-cabs']").click()
        all_windows = driver.window_handles
        print(all_windows)
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                driver.find_element(By.XPATH,"//button[@id='submit-btn']").click()
                time.sleep(3)
                driver.switch_to.alert.accept()
                time.sleep(3)
        driver.switch_to.window(parent_window)
        time.sleep(3)
        driver.close()




multiple_window = multiple_windows()
multiple_window.windows()