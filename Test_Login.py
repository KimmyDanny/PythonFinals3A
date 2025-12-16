import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Maximize the browser window for better visibility
    driver.maximize_window()
    # Navigate to the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver

    # teardown
    driver.quit()



def test_positive_login(driver):
    time.sleep(10)

    #locators
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


    assert "auth/login" not in driver.current_url


