import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # IMPORTANT: allow SPA to load completely
    time.sleep(10)

    yield driver

    driver.quit()


def test_quick_launch_my_leave(driver):

    # Login (FIXED locators)
    driver.find_element(
        By.XPATH, "//input[@name='username']"
    ).send_keys("Admin")

    driver.find_element(
        By.XPATH, "//input[@name='password']"
    ).send_keys("admin123")

    driver.find_element(
        By.XPATH, "//button[@type='submit']"
    ).click()

    time.sleep(10)

    # Quick Launch → My Leave
    driver.find_element(
        By.XPATH,
        "//div[contains(@class,'orangehrm-quick-launch')]//button[@title='My Leave']"
    ).click()

    time.sleep(5)

