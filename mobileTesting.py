from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "15",  # Adjust according to your device/emulator version
    "appium:deviceName": "MyPhonePixel8",  # Ensure this matches your device/emulator name
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Perform touch actions
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(454, 1182)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(588, 716)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(912, 1516)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    # Interact with elements
    el5 = driver.find_element(by=AppiumBy.ID, value="com.momosa:id/mat_edit_outline")
    el5.send_keys("12345")
    
    el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(15)")
    el6.click()

   

# Wait for 5 seconds
    #time.sleep(5)

    #el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Skip")')
    #el7.click()

    wait = WebDriverWait(driver, 10)
    skip_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip")')))
    skip_button.click()

    #el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.ImageView").instance(0)')
    #.click()

    wait = WebDriverWait(driver,10)
    Humberger_widget = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(2)')))
    Humberger_widget.click()



    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(342, 2026)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(342, 1271)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value = 'new UiSelector().className("android.view.ViewGroup").instance(83)')
    el9.click()

    #el10 =  driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value = 'new UiSelector().className("android.view.ViewGroup").instance(49)')
    #el10.click()

    wait = WebDriverWait(driver,10)
    SignOut_popup = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, ' ')))
    SignOut_yes = SignOut_popup.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.ViewGroup").instance(48)')
    SignOut_yes.click()



finally:
    driver.quit()
