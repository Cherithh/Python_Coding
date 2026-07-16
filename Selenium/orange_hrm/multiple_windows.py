from selenium import webdriver
driver = webdriver.Chrome()
from selenium .webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

driver.get("https://www.yatra.com/%3Fredirect%3Dno")
driver.maximize_window()
wait = WebDriverWait(driver,10)
actions = ActionChains(driver)
parent_window = driver.current_window_handle
wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='Cabs']"))).click()
windows = driver.window_handles
print(windows)
for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Book a Cab']"))).click()
        time.sleep(3)

driver.switch_to.window(parent_window)
# more = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='+ More']")))
# actions.move_to_element(more).perform()
# time.sleep(2)
# wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='Gift Voucher']"))).click()
# time.sleep(3)
facebook = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@title='Facebook']")))
driver.execute_script("arguments[0].scrollIntoView({block : 'Center'});",facebook)
# facebook.click()
time.sleep(3)