from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class HomePageScreen:

    def __init__(self, driver):
        self.driver = driver

        # Locator for the balance element(you can use partial text matching with the UiSelector to locate the balance element if balance start with consistent currency)
        self.get_customer_balance = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("R")')

    def get_balance(self):
        try:
            print("Attempting to locate the balance element")
            wait = WebDriverWait(self.driver, 30)
            self.post_login_balance = wait.until(EC.visibility_of_element_located(self.get_customer_balance))

            if self.post_login_balance.is_displayed():
                balance_text = self.post_login_balance.text  # Capture the text from the balance element
                print(f"Balance element is displayed. Balance: {balance_text}")
                return balance_text  # Return the balance text

        except TimeoutException as e:
            print(f"Failed to locate balance element: {str(e)}")
            return None
