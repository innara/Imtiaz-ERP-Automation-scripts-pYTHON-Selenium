from telnetlib import EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("Url exmple")
driver.set_page_load_timeout(20)
email = driver.find_element(By.NAME, "email")
email.send_keys("some email")
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

# Accessing floor  from sidebar
driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[4]/a').click()
time.sleep(2)

# New Floor
New = driver.find_element(By.XPATH, ' //*[@id="floor-table_wrapper"]/div[1]/div[2]/div/div[2]/button')
New.click()

# Select project and floor name
dropdown_el = driver.find_element(By.XPATH, '//*[@id="project_id"]')
dropdown = Select(dropdown_el)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)
floor_name = driver.find_element(By.XPATH, ' //*[@id="floor_project_name"]')
floor_name.send_keys('Floor 1')
button = driver.find_element(By.XPATH,'//*[@id="submit_floor"]')
button.click()
time.sleep(3)

driver.quit()