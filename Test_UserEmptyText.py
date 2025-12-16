import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Fixture to set up and tear down the browser
@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    yield driver

    driver.quit()


# Parametrize test with multiple negative login scenarios
@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("Admin", "wrongpass", "Invalid credentials"),
        ("", "admin123", "Required"),
        ("Admin", "", "Required"),
        ("", "", "Required")
    ]
)
def test_negative_login(driver, username, password, expected):
    # Enter username only if it is not empty
    if username != "":
        driver.find_element(By.NAME, "username").send_keys(username)
    # Enter password only if it is not empty
    if password != "":
        driver.find_element(By.NAME, "password").send_keys(password)
    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    # Validate error message for invalid credentials
    if expected == "Invalid credentials":
        error_text = driver.find_element(
            By.CLASS_NAME, "oxd-alert-content-text"
        ).text
        assert expected in error_text

    # Validate required field validation message
    else:
        error_text = driver.find_element(
            By.XPATH, "//span[text()='Required']"
        ).text
        assert expected in error_text
