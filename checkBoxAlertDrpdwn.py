#1.checkbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
driver = webdriver.Chrome()
import time
driver.get("https://testautomationpractice.blogspot.com/?m=1")
driver.maximize_window()
time.sleep(2)
sunday = driver.find_element(By.XPATH,"//input[@id='sunday']")
sunday.click()
monday = driver.find_element(By.XPATH,"//input[@id='monday']")
monday.click()
time.sleep(4)
driver.quit()

#2. checkbox
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import select
# driver = webdriver.Chrome()
# import time
# driver.get("https://testautomationpractice.blogspot.com/?m=1")
# driver.maximize_window()
# time.sleep(2)
# check_box = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for box in check_box:
#     box.click()
# for a in check_box:
#     weekname = a.get_attribute("id")
#     if weekname == "sunday" and weekname == "monday":
#         a.click()
#         for b in check_box:
#             if b.is_selected():
#                 b.click()
# time.sleep(5)
# print("sun and mon are selected")
# driver.quit()

#alerts -1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# import time
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("hello world")
# time.sleep(4)
# alert.accept()
# driver.quit()

#alerts -2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# import time
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(3)
# print("alert accepted")

#alerts -3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# import time
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(3)
# print("alert accepted")

#dropdown
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# import time
# time.sleep(3)
# dropdown = driver.find_element(By.XPATH,"//select[@id='country']")
# drop = Select(dropdown)
# time.sleep(3)
# drop.select_by_visible_text("Canada")
# time.sleep(3)
# drop.select_by_value("germany")
# time.sleep(3)
# drop.select_by_index(5)
# time.sleep(3)
# print("dropdown selected successfully")
# driver.quit()

#headless -1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# option = Options()
# option.add_argument("--headless")
# option.add_argument("--disable-gpu")
# option.add_argument("window-size=1920,1080")
# driver = webdriver.Chrome(options=option)
# driver.get("http://www.amazon.com")
# time.sleep(3)
# print("Page title : ",driver.title)
# driver.quit()

#implicit wait
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import element_located_to_be_selected
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# time.sleep(3)
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# time.sleep(3)
# driver.find_element(By.ID, "login-button").click()
# time.sleep(3)
# # Error: Timeout exception, No such element exception
# print("Login is successful")
# driver.quit()

# explicit wait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10)
#
# username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
# username.send_keys("standard_user")
#
# password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
# password.send_keys("secret_sauce")
#
# login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
# login_button.click()
#
# print("login success:" "login successful")
# driver.quit()




