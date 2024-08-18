from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver



        # Locator tuples
        self.momo_app = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MoMo SA ComDevops SIT")')
        self.momo_pin = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.momosasit:id/mat_edit_outline")')
        self.login_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign in")')
        self.post_login_banner = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip")')

    def click_momo_app(self):
        # Initialize Action Chains for touch interactions
        self.actions = ActionChains(self.driver)
        self.actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        self.actions.w3c_actions.pointer_action.move_to_location(461, 1175)
        self.actions.w3c_actions.pointer_action.pointer_down()
        self.actions.w3c_actions.pointer_action.move_to_location(491, 476)
        self.actions.w3c_actions.pointer_action.release()
        self.actions.perform()

        wait = WebDriverWait(self.driver, 20)
        momo_app_logo = wait.until(EC.visibility_of_element_located(self.momo_app))
        momo_app_logo.click()   

    def enter_momo_pin(self, pin):
        wait = WebDriverWait(self.driver, 20)
        sign_in_text_field = wait.until(EC.visibility_of_element_located(self.momo_pin))
        sign_in_text_field.send_keys(pin)

    def click_sign_in_button(self):
        #time.sleep(2)
        self.driver.find_element(*self.login_button).click()

    def click_skip_button(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            self.skip_button = wait.until(EC.visibility_of_element_located(self.post_login_banner))
            if self.skip_button.is_displayed():
                self.skip_button.click()
                return True
        except:
            pass
        return False

