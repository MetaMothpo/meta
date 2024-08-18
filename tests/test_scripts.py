from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_page():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Navigate to the SauceDemo login page
    driver.get('https://www.saucedemo.com/')

    # Perform login
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    
    # Take a screenshot of the login page
    screenshot_path = "screenshot1.png"
    driver.save_screenshot(screenshot_path)
    print(f"Login Screen: {screenshot_path}")

    driver.find_element(By.ID, 'login-button').click()

    # Wait for the page to load
    time.sleep(5)

    # Check if login was successful
    if driver.title == 'Swag Labs':
        # Take a screenshot of the home page
        screenshot_path = "screenshot2.png"
        driver.save_screenshot(screenshot_path)
        print(f"Home Screen: {screenshot_path}")
        result = 'Logged in successfully'
    else:
        result = 'Not logged in'
    
    # Close the browser
    driver.quit()

    return result

if __name__ == "__main__":
    test_result = test_login_page()
    print(test_result)
