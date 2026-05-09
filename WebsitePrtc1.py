from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(10)
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys("Jyoti")
driver.find_element(By.ID, "email").send_keys("matti123@gmail.com")
driver.find_element(By.ID, "phone").send_keys("9838343883")
driver.find_element(By.ID, "textarea").send_keys("Kumaraswamy layout, Bengaluru")
driver.find_element(By.ID, "female").click()
time.sleep(3)
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'sun') or contains(@id,'sat')]")
for box in checkbox:
    box.click()
#select country
time.sleep(3)
dropdown = driver.find_element(By.ID, "country")
drop = Select(dropdown)
drop.select_by_visible_text("India")
time.sleep(3)
dropdown = driver.find_element(By.ID, "colors")
drop = Select(dropdown)
drop.select_by_visible_text("Yellow")
time.sleep(3)
driver.find_element(By.ID, "datepicker").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[5]/a').click()
time.sleep(3)
file_path = r"C:\Users\user\Downloads\WhatsApp Image 2025-12-05 at 07.17.50.jpeg"
# driver.find_element(By.ID, "singleFileInput").click()
file_input = driver.find_element(By.ID, "singleFileInput")
file_input.send_keys(file_path)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="singleFileForm"]/button').click()
time.sleep(3)
driver.quit()