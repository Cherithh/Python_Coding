from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class sliders:
    def slide(self):
        driver.get("https://www.snapdeal.com/search?clickSrc=top_searches&keyword=shoes%20for%20men&categoryId=0&vertical=p&noOfResults=20&SRPID=topsearch&sort=rlvncy&q=Price%3A128%2C2995%7C")
        driver.maximize_window()
        left_handle = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        right_handle = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        actions = ActionChains(driver)
        actions.click_and_hold(left_handle).pause(1).move_by_offset(100,0).release().perform()
        time.sleep(3)
        actions.click_and_hold(right_handle).move_by_offset(-60,0).release().perform()
        time.sleep(3)


sliding = sliders()
sliding.slide()