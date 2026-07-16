from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(@href,'viewMyDetails')]").click()
# driver.find_element(By.XPATH,"//a[contains(@href,'viewPimModule')]").click()
wait = WebDriverWait(driver,20)
# pim_add = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add']")))
# pim_add.click()

# wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[normalize-space()='Add Employee']")))
# upload = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
# upload.send_keys(r"C:\Users\cheri\OneDrive\Pictures\uwp4442502.jpeg")

# driver.find_element(By.NAME,"firstName").send_keys("He")
# driver.find_element(By.NAME,"lastName").send_keys("Man")
# driver.find_element(By.XPATH,"//label[normalize-space()='Employee Id']/following::input[1]").send_keys("8976")
# driver.find_element(By.XPATH,"//span[contains(@class,'--label-right')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//label[normalize-space()='Username']/following::input[1]").send_keys("Cheri564")
# driver.find_element(By.XPATH,"//label[normalize-space()='Password']/following::input[1]").send_keys("Cherith@123")
# driver.find_element(By.XPATH,"//label[normalize-space()='Confirm Password']/following::input[1]").send_keys("Cherith@123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(5)
wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[normalize-space()='Personal Details']")))
firstname = driver.find_element(By.NAME,"firstName")
firstname.send_keys(Keys.CONTROL, "a")
firstname.send_keys(Keys.DELETE)
firstname.send_keys("Batman")
lastname = driver.find_element(By.NAME,"lastName")
lastname.send_keys(Keys.CONTROL, "a")
lastname.send_keys(Keys.DELETE)
lastname.send_keys("WD")
emp_id = driver.find_element(By.XPATH,"//label[normalize-space()='Employee Id']/following::input[1]")
emp_id.send_keys(Keys.CONTROL, "a")
emp_id.send_keys(Keys.DELETE)
emp_id.send_keys("3434")
drn_license = wait.until(EC.visibility_of_element_located((By.XPATH,'//label[normalize-space()="Driver\'s License Number"]/following::input[1]')))
drn_license.send_keys(Keys.CONTROL, "a")
drn_license.send_keys(Keys.DELETE)
drn_license.send_keys("DRN5463")

license = wait.until(EC.visibility_of_element_located((By.XPATH,"//label[normalize-space()='License Expiry Date']/following::input[1]")))
license.send_keys(Keys.CONTROL,"a")
license.send_keys(Keys.DELETE)
license.send_keys("2026/05/05")


nationality = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Nationality']/following::div[contains(@class,'oxd-select-text-input')][1]")))
while True:
    selected_value = nationality.text

    if selected_value == "Indian":
        nationality.click()
        break

    nationality.send_keys(Keys.ARROW_DOWN)


wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Marital Status']/following::div[contains(@class,'oxd-select-text-input')][1]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Single']"))).click()
time.sleep(5)

attachments = wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[text()='Attachments']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attachments)
attachments.click()

# body = driver.find_element(By.TAG_NAME, "body")
# body.send_keys(Keys.END)
# blood_type = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Blood Type']/following::div[@class='oxd-select-text oxd-select-text--active']")))
# while True:
#     blood_data = blood_type.text
#     if blood_data == "O-":
#         blood_type.click()
#         break

#     blood_type.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[normalize-space()='Select File']")))
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\cheri\Downloads\Bruno JD.pdf")
time.sleep(5)
driver.find_element(By.XPATH,"//textarea[@placeholder='Type comment here']").send_keys("YEAHHH!!!")
save_button = driver.find_element(By.XPATH,"//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
save_button.click()
time.sleep(5)


scroll_dependents = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Dependents']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", scroll_dependents)
scroll_dependents.click()

wait.until(EC.visibility_of_element_located((By.XPATH,".//button[normalize-space()='Add']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//label[normalize-space()='Name']/following::input[1]"))).send_keys("Batwoman")

relationship = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='oxd-select-text-input']")))
relationship.click()
while True:
    relationshipdata = relationship.text
    if relationshipdata == "Child":
        relationship.click()
        break
    
    relationship.send_keys(Keys.ARROW_DOWN)
    
time.sleep(3)

attachments_add = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='orangehrm-attachment']//i[@class='oxd-icon bi-plus oxd-button-icon']")))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",attachments_add)
attachments_add.click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//label[normalize-space()='Select File']")))
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\cheri\Downloads\PAN.pdf")
time.sleep(5)
driver.find_element(By.XPATH,"//img[@alt='profile picture']").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Logout']"))).click()
company = wait.until(EC.visibility_of_element_located((By.XPATH,"//img[@alt='company-branding']")))
if company.is_displayed():
    print("Logout successful")
else:
    print("Could not Logout Properly")