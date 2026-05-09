#Keys
# import time
# from selenium import webdriver
# from selenium.webdriver.common import keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains, Keys # Key  is a class
# driver = webdriver.Chrome()
# driver.get("https://text-compare.com/")
# driver.maximize_window()
# input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
# input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
# input1.send_keys("Hello welcome to Selenium to perform automation testing using Pytest framework and with Hybrid structure")
# time.sleep(3)
# act = ActionChains(driver)
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# act.key_down(Keys.TAB).perform()
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# time.sleep(3)
# print("Keyboard successfully")
# driver.quit()

#scrollup/scroll down using JS
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.fita.in/")
# driver.maximize_window()
# time.sleep(5)
# # Use WebDriverWait to wait for the element to be present
# element_to_scroll_to = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'FITA Academy')]")))
#
# # Scroll to the element using scrollIntoView()
# driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", element_to_scroll_to)
# time.sleep(3)
#
# # Scroll down by 1000 pixels
# scroll_down_script = "window.scrollBy(0,1000);"
# driver.execute_script(scroll_down_script)
# print("Scrolled the page till 1000 pixel")
# time.sleep(3)
# # Scroll down by 1800 pixels
# scroll_down_script = "window.scrollBy(0,2500);"
# driver.execute_script(scroll_down_script)
# time.sleep(3)
# print("scrolled the page till 2500")
#
# # Scroll up by 1000 pixels
# scroll_up_script = "window.scrollBy(0, -1000);"
# driver.execute_script(scroll_up_script)
# print("scrolled the page till -1000")
# time.sleep(3)
#
# # Scroll to the bottom of the page
# scroll_to_bottom_script = "window.scrollTo(0, document.body.scrollHeight);"
# driver.execute_script(scroll_to_bottom_script)
# time.sleep(3)
# print("scrolled the page to the bottom")
#
# # Scroll back to the top of the page
# scroll_to_top_script = "window.scrollTo(0, 0);"
# driver.execute_script(scroll_to_top_script)
# print("scrolled the page to the top")
# time.sleep(3)
# driver.quit()
#-----------------------------------------------------------------------------------
#link
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

links = driver.find_elements(By.XPATH,"//a")
print("Total no.of links:",len(links))

for link in links:
    print(link.text)
driver.quit()