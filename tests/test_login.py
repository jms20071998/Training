from selenium import webdriver
from pages.login_page import pages

def test_login_valid_user():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = pages(driver)
    login_page.login("standard_user", "secret_sauce")

    # Assertion: check successful login
    assert "inventory" in driver.current_url

    driver.quit()