from telnetlib import EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("Some URL")
driver.set_page_load_timeout(20)
email = driver.find_element(By.NAME, "email")
email.send_keys("Some email")
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="formAuthentication"]/button')
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")
time.sleep(5)

# Accessing Project from sidebar
driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[3]').click()
time.sleep(3)
# Adding new project

driver.find_element(By.XPATH,'//*[@id="dataTableBuilder_wrapper"]/div[1]/div[2]/div/div[2]/button').click()
time.sleep(5)
projectname = driver.find_element(By.NAME, 'name')
projectname.send_keys("Isloo project")
status = driver.find_element(By.XPATH, ' //*[@id="project_status"]')
status.send_keys('In Progress')
address = driver.find_element(By.XPATH, ' //*[@id="project_location"]')
address.send_keys('Dhok Paracha, Islamabad')
area = driver.find_element(By.XPATH, ' //*[@id="area"]')
area.send_keys(' 30999')  #area
dld = driver.find_element(By.XPATH, ' //*[@id="dld_fee"]')
dld.send_keys(' 10')
adminfee= driver.find_element(By.XPATH,'//*[@id="admin_fee"]')
adminfee.send_keys('1000')
time.sleep(10)
element = driver.find_element(By.XPATH,'//*[@id="projectbtn"]')
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)
element.click()
time.sleep(4)
# Floor creation within Project
floor = driver.find_element(By.XPATH, '//*[@id="tabs"]/ul/li[3]')
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
time.sleep(3)
floor.click()
add = driver.find_element(By.XPATH, ' //*[@id="floor"]/div[1]/div[2]/div/button')
time.sleep(3)
add.click()
floor_name = driver.find_element(By.XPATH, ' //*[@id="floor_name"]')
floor_name.send_keys('Floor 1')
time.sleep(2)
button = driver.find_element(By.XPATH ,'//*[@id="floorbtn"]')
button.click()
print('Successfully created Floor ')
time.sleep(10)

# Create Type:
type = driver.find_element(By.XPATH, ' //*[@id="tabs-type"]')
type.click()
time.sleep(2)
addtype = driver.find_element(By.XPATH, "(//button[@id='add-new-attachment'])[2]")
addtype.click()
type_name = driver.find_element(By.XPATH, ' //*[@id="type_name"]')
type_name.send_keys('Shop')

EOI = driver.find_element(By.ID, 'eoi')
EOI.send_keys('300')
time.sleep(10)
submit = driver.find_element(By.XPATH, ' //*[@id="typebtn"]')
submit.click()
print('successfully created Unit Type')
time.sleep(5)


# Property Type
property_type = driver.find_element(By.XPATH, ' //*[@id="tabs-property"]')
property_type.click()
new = driver.find_element(By.XPATH, "//div[@class='property-list']//button[@id='add-new-attachment']")
new.click()
time.sleep(2)
name = driver.find_element(By.XPATH, '//*[@id="property_type"]')
name.send_keys('Commercial property')
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="propertybtn"]')
button.click()
print("Successfully created Property Type ")
time.sleep(5)

# Sales Offer setting
sales_offer = driver.find_element(By.XPATH,'//*[@id="tabs-saleSetting"]')
sales_offer.click()
element = driver.find_element(By.XPATH,'//*[@id="salesOfferbtn"]')
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)
element.click()
time.sleep(5)
driver.quit()

