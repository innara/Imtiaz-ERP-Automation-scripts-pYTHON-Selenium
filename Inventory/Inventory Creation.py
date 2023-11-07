from telnetlib import EC

import driver as driver
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("Enter URL ")
driver.set_page_load_timeout(20)
email = driver.find_element(By.NAME, "email")
email.send_keys("Example email")
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
# List of inventory items with different data
inventory_items = [
    {
        "project_name": "Something ",
        "floor": "Floor 1",
        "type": "Shop",
        "property_type": "Commercial property",
        "status": "Open",
        "balcony_area": "160",
        "suite_size": "400",
        "rate": "45.6",
        "parking_no": "1",
    },
]
# Loop for creating inventory
for _ in range(50):
    time.sleep(4)
    for item_data in inventory_items:
        # Access inventory from the sidebar
        driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[8]/a').click()
        time.sleep(3)

        # Create New inventory
        new = driver.find_element(By.XPATH, '//*[@id="dataTableBuilder_wrapper"]/div[1]/div[2]/div/div[2]/button[1]')
        new.click()

        # Filling Inventory fields
        driver.find_element(By.XPATH, '//*[@id="select2-project-container"]').click()
        search_input = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        search_input.send_keys(item_data["project_name"])
        wait = WebDriverWait(driver, 10)
        first_result = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="select2-project-results"]//li[1]')))
        first_result.click()
        time.sleep(5)

        # Selecting floor
        dropdown_el = driver.find_element(By.XPATH, '//*[@id="floor"]')
        dropdown = Select(dropdown_el)
        dropdown.select_by_visible_text(item_data["floor"])
        time.sleep(3)

        # Selecting Type
        dropdown_el = driver.find_element(By.XPATH, '//*[@id="type"]')
        dropdown = Select(dropdown_el)
        dropdown.select_by_visible_text(item_data["type"])
        time.sleep(3)

        # Generate a unique "Unit No" based on the current timestamp
        unit_no = f"{int(time.time())}"
        unit = driver.find_element(By.XPATH, '//*[@id="name"]')
        unit.send_keys(unit_no)
        time.sleep(2)

        # Property type
        dropdown_el = driver.find_element(By.XPATH, '//*[@id="property_id"]')
        dropdown = Select(dropdown_el)
        dropdown.select_by_visible_text(item_data["property_type"])
        time.sleep(3)

        # Status
        dropdown_el = driver.find_element(By.XPATH, '//*[@id="status"]')
        dropdown = Select(dropdown_el)
        dropdown.select_by_visible_text(item_data["status"])
        time.sleep(3)

        # Balcony size
        balcony = driver.find_element(By.XPATH, '//*[@id="balcony_area"]')
        balcony.send_keys(item_data["balcony_area"])

        # Suite Size
        Suite = driver.find_element(By.XPATH, '//*[@id="area"]')
        Suite.send_keys(item_data["suite_size"])

        # Rate
        Rate = driver.find_element(By.XPATH, '//*[@id="rate"]')
        Rate.send_keys(item_data["rate"])

        # Parking
        Park = driver.find_element(By.XPATH, '//*[@id="parking_no"]')
        Park.send_keys(item_data["parking_no"])

        time.sleep(2)
        button = driver.find_element(By.XPATH, '//*[@id="inventory_form"]/div/div[2]/div[2]/div/div/button')
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(10)
        button.click()
        time.sleep(5)

# Quit the webdriver
driver.quit()