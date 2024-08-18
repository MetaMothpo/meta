from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options






def testloginPage():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager(version="124.0.5221.0").install())

    driver.get('https://www.saucedemo.com/')



    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')

    screenshot_path = "screenshot1.png"
    driver.save_screenshot(screenshot_path)
    login_screen =(f"Login Screen {screenshot_path}")

    driver.find_element(By.ID, 'login-button').click()

   


    time.sleep(5)

    #title = 'Swag Labs'
    #gettext = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div').text

    if driver.title == 'Swag Labs':
        screenshot_path = "screenshot2.png"
        driver.save_screenshot(screenshot_path)
        login_screen =(f"Home screen {screenshot_path}")
        return 'logged in successfully'
        
    else:
        return 'Not logged in'

if __name__ == "__main__":
    testloginPage()


# test_script.py
#def run_tests():
    # Simulate some test logic
    # For example, this could be running Selenium tests or some other scripts
    #test_results = []

    # Example test cases
    #test_results.append("Test 1: Passed")
    #test_results.append("Test 2: Passed")
    #test_results.append("Test 3: Failed")

    # Combine results into a single string or list
    #result_summary = "\n".join(test_results)

    #return result_summary







