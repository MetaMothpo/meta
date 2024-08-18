from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
class sendMoney:

    def __init__(self, driver):
        self.driver = driver

        self.Send = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)')
        self.Send_money_to_cell = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(8)')
        self.Enter_cellNumber = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter cellphone number")')
        self.ContinueButton = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")')
        self.Enter_amount = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+R20")')
        self.Continue_to_send = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")')
        self.account_name = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("TUWANI")')
        self.cell_number = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("083 857 8919")')
        self.total_amount =(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("R20.00").instance(1)')
        self.confirm_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Confirm")')
        self.success_trans = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Success!")')
        self.transaction_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(10)')
        self.done_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(13)')


    def ClickSend(self):
        self.driver.find_element(*self.Send).click()
    
    def clickSend_money_to_cell(self):
      
            #wait = WebDriverWait(self.driver, 30)
            #self.clickSendMoney= wait.until(EC.element_to_be_clickable())
        self.driver.find_element(*self.Send_money_to_cell).click()
    
    def Enter_MoMoNumber(self):
        wait = WebDriverWait(self.driver, 30)
        self.enter_msisdn = wait.until(EC.visibility_of_element_located(self.Enter_cellNumber))
        
        if self.enter_msisdn.is_displayed():
            msisdn = self.enter_msisdn.send_keys('0713329729')

        

    def ClickContinue_button(self):
        self.driver.find_element(*self.ContinueButton).click()

    def Select_amount(self):
        
        wait = WebDriverWait(self.driver, 30)
        self.amount = wait.until(EC.visibility_of_element_located(self.Enter_amount))

        if self.amount.is_displayed():
            self.amount.click()

        #self.driver.find_element(*self.Enter_amount).click()
    
    def Click_continue_toSend(self):
        wait= WebDriverWait(self.driver, 30)
        continueButton = wait.until(EC.visibility_of_element_located(self.Continue_to_send))
        continueButton.click()



    def get_recipient_details(self):
        recipient_name = self.driver.find_element(*self.account_name).text
        recipient_number = self.driver.find_element(*self.cell_number).text
        totalAmount = self.driver.find_element(*self.total_amount).text

        return recipient_name, recipient_number, totalAmount
    
    def click_confirm_button(self):
        wait = WebDriverWait(self.driver, 30)
        self.confirmButton = wait.until(EC.visibility_of_element_located(self.confirm_button))
        self.confirmButton.click()
        time.sleep(3)
        #self.driver.find_element(*self.confirm_button).click()
        self.success_screen=self.driver.find_element(*self.success_trans).text
        print('Sucess message is',self.success_screen)

        return self.success_screen
    
    def getTransaction_id(self):
        self.trans_id =self.driver.find_element(*self.transaction_id)

    def sucessScreen(self):
        try:

            if self.success_screen == 'Success!':
                self.trans_id.text
                return self.trans_id
            
        except TimeoutException as e:
            print(f"Transaction Failed: {str(e)}")
            return None

        
