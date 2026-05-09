from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class dragdrops:
    def dd(self):
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        driver.switch_to.frame(frame)
        drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
        drop = driver.find_element(By.XPATH,"//div[@id='droppable']")
        actions = ActionChains(driver)
        # actions.drag_and_drop(drag,drop).perform()
        actions.drag_and_drop_by_offset(drag,160,30).perform()
        time.sleep(3)


dragdrop = dragdrops()
dragdrop.dd()