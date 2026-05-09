#1.USing Application Commands
# from selenium import webdriver
# driver = webdriver.Chrome()
# import time
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# print(driver.page_source)
# print("title: ",driver.title)
# print("current url:",driver.current_url)
# driver.maximize_window()
# time.sleep(3)
# driver.close()

#2.Conditional commands
# from selenium import webdriver
# driver = webdriver.Chrome()
# from selenium.webdriver.common.by import By
# import time
# driver.get("https://demo.nopcommerce.com/register")
# driver.maximize_window()
# time.sleep(4)
# searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print(searchbox.is_displayed())
# print(searchbox.is_enabled())
# time.sleep(3)
# driver.close()

#3.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# import time
# driver.get("https://demo.nopcommerce.com/register")
# driver.maximize_window()
# a = driver.find_element(By.XPATH,"//input[@id='gender-male']")
# b = driver.find_element(By.XPATH,"//input[@id='gender-female']")
# print(a.is_displayed())
# print(a.is_enabled())
# a.click()
# print("Enter male radio button")
# print(a.is_selected())
# print(b.is_selected())
# time.sleep(5)
# driver.close()

#4.Navigational Commands
# from selenium import webdriver
# driver = webdriver.Chrome()
# import time
# driver.get("https://snapdeal.com/")
# driver.maximize_window()
# driver.back()
# time.sleep(4)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(5)
# driver.close()