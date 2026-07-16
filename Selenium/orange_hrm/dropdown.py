from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
categories = wait.until(EC.presence_of_element_located((By.ID,"searchDropdownBox")))
dropdown = Select(categories)
dropdown.select_by_visible_text("Car & Motorbike")

search = driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("Ferrari Lego")
search.send_keys(Keys.ENTER)

# last = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Last 30 days')]")))
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",last)
body = driver.find_element(By.TAG_NAME,"body")
body.send_keys(Keys.END)
time.sleep(2)
body.send_keys(Keys.HOME)
time.sleep(2)