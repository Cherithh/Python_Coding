from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver  import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver.get("https://www.flipkart.com/")
driver.maximize_window()
actions = ActionChains(driver)
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
my_cases = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Login']")))
actions.move_to_element(my_cases).perform()
time.sleep(5)
