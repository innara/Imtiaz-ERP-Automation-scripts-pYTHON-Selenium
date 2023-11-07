from telnetlib import EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("Url example")
driver.set_page_load_timeout(20)
email = driver.find_element(By.NAME, "email")
email.send_keys("email example")
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
# delete Floor
delete = driver.find_element(By.XPATH, '//*[@id="34"]/td[6]/div/a[2]/i')
delete.click()
button = driver.find_element(By.XPATH, ' /html/body/div[3]/div/div[6]/button[1]')
button.click()
time.sleep(5)
driver.quit()