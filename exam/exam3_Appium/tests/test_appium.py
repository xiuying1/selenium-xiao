import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Adjust according to your device or emulator version
        "deviceName": "Android Emulator",
        "app": "src/test/resources/apk/app-debug-1.0.0.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

def test_click_button(driver):
    # Wait for the button to appear and click it
    button = driver.find_element(AppiumBy.ID, "com.example:id/button")
    button.click()
    time.sleep(2)  # Wait for the page to load

def test_extract_text(driver):
    # Extract resource text
    text_view = driver.find_element(AppiumBy.ID, "com.example:id/textView")
    extracted_text = text_view.text
    print(f"Extracted Text: {extracted_text}")
    assert extracted_text == "Expected Text"

def test_assert_different_page(driver):
    # Click the button to navigate to a different page
    button = driver.find_element(AppiumBy.ID, "com.example:id/button")
    button.click()
    time.sleep(2)  # Wait for the page to load

    # Assert resources on the different page
    new_page_text_view = driver.find_element(AppiumBy.ID, "com.example:id/newPageTextView")
    new_page_text = new_page_text_view.text
    assert new_page_text == "Expected New Page Text"

