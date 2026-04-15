from selenium.webdriver.common.by import By
from utilities.waits import wait_for_visibility, wait_for_clickable

class LoginPage:
    def _init_(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, pwd):
        # Wait for username field
        wait_for_visibility(self.driver, self.username).send_keys(user)

        # Wait for password field
        wait_for_visibility(self.driver, self.password).send_keys(pwd)

        # Wait for login button and click
        wait_for_clickable(self.driver, self.login_button).click()