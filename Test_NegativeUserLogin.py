import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)  # wait for page to load
    yield driver
    driver.quit()

def test_negative_login(driver):

    # FIRST NEGATIVE TEST
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    error_text = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
    assert "Invalid credentials" in error_text

    # Clear fields
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "password").clear()

    time.sleep(1)

    # SECOND NEGATIVE TEST
    driver.find_element(By.NAME, "username").send_keys("wronguser")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    error_text = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
    assert "Invalid credentials" in error_text
