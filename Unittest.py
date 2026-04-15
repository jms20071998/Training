import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Run all tests in a file
#python -m unittest test_file_name.py

#2. Run a specific test class
#python -m unittest test_file_name.TestClassName

#3. Run a specific test method
#python -m unittest test_file_name.TestClassName.test_method_name

#4. Discover and run all tests in a folder
#python -m unittest discover

#or
#with a specific folder:
#python -m unittest discover -s tests


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)

        # username and password fields and login button
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        time.sleep(3)

        # Enter login credentials
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        time.sleep(7)

        # Verify successful login by checking for the presence of inventory items
        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.assertGreater(len(inventory_items), 0, "Login failed or no inventory items found.")

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Login first
        # username_field = driver.find_element(By.ID, "user-name")
        # password_field = driver.find_element(By.ID, "password")
        # login_button = driver.find_element(By.ID, "login-button")
        # time.sleep(5)
        # username_field.send_keys("standard_user")
        # password_field.send_keys("secret_sauce")
        # login_button.click()
        # time.sleep(5)

        # Add first inventory item to the cart
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        add_to_cart_button.click()
        time.sleep(5)

        # Verify the cart shows 1 item
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "1", "Item was not added to the cart.")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

    #------------------------------------------------------------------------------



