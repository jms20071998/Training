from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
driver.maximize_window()
# Wait for the page to load completely
time.sleep(5)

# Scroll down by 1000 pixels
scroll_down_script = "window.scrollBy(0, 1000);"
driver.execute_script(scroll_down_script)
time.sleep(2)

# Scroll to the element using scrollIntoView()
element_to_scroll_to = driver.find_element(By.XPATH, "//table[contains(@class, 'wikitable')]")
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", element_to_scroll_to)
time.sleep(2)

# Scroll down by another 1000 pixels
driver.execute_script(scroll_down_script)
time.sleep(2)

# Scroll up by 1000 pixels
scroll_up_script = "window.scrollBy(0, -1000);"
driver.execute_script(scroll_up_script)
time.sleep(2)

# Scroll back to the top of the page
scroll_to_top_script = "window.scrollTo(0, 0);"
driver.execute_script(scroll_to_top_script)
time.sleep(2)

# Find the table element and print its content
table = driver.find_element(By.XPATH, "//table[contains(@class, 'wikitable')]")
rows = table.find_elements(By.TAG_NAME, "tr")

# Loop through the rows and print the cell data
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)

driver.quit()