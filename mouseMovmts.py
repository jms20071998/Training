#hoverover
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
# Point = driver.find_element(By.XPATH,"//button[text()='Point Me']")
# Mobile = driver.find_element(By.XPATH,"//button[text()='Mobiles']")
# Laptop = driver.find_element(By.XPATH,"//button[text()='Laptops']")
# act = ActionChains(driver)
# time.sleep(3)
# act.move_to_element(Point).move_to_element(Mobile).move_to_element(Laptop).click().perform()
# time.sleep(3)
# print("Mouse hoverover completed successfully")
# driver.quit()

#right click
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()
# time.sleep(2)
# right = driver.find_element(By.XPATH, "//span[text()='right click me']")
# act = ActionChains(driver)
# act.context_click(right).perform()
# time.sleep(3)
# driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
# time.sleep(4)
# driver.quit()

#double click
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/#")
# driver.maximize_window()
# time.sleep(2)
# field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
# field1.clear()
# field1.send_keys("Selenium")
# time.sleep(3)
#
# button = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
# act = ActionChains(driver)
# act.double_click(button).perform()
# time.sleep(4)
# driver.quit()

# drag drop
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
# source = driver.find_element(By.XPATH,"//div[@id='draggable']")
# target = driver.find_element(By.XPATH,"//div[@id='droppable']")
# act = ActionChains(driver)
# act.drag_and_drop(source,target).perform()
# time.sleep(4)
# print("drag drop has been done successfully")
# driver.quit()

# slider
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
min_slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
max_slider = driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")
act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, 300, 0).perform()
print("location of sliders")
print(min_slider.location)
print(max_slider.location)
time.sleep(5)
driver.quit()
