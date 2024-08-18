import pytest
from appium import webdriver
import csv
from appium.options.common.base import AppiumOptions
from datetime import datetime
from loginPage import LoginPage
from HomePage import HomePageScreen
from SendMoney_to_MoMoNo import sendMoney


@pytest.fixture(scope="class")
def setup_class(request): #pass request to a fixture, it allows the fixture to access details about the test, such as the test class, test module, or the name of the test function being executed
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:platformVersion": "15",
        "appium:deviceName": "MyMediumPhone35",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    #request.cls: Attaches the driver and page objects to the test class (TestLogin), making them accessible within the test methods.
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.home_page = HomePageScreen(driver)
    request.cls.send_money = sendMoney(driver)
    request.cls.results_file = 'test_results.csv'

    yield
    
    driver.quit()

@pytest.mark.usefixtures("setup_class")
class TestLogin:

    @pytest.fixture(autouse=True)
    def always_run_beforeTest(self):
        print('**********************************************************')

    @pytest.fixture
    def read_test_data(self):
        test_data = []
        with open('test_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                test_data.append(row)
        return test_data

    @pytest.fixture
    def write_test_result(self):
        def _write_result(Testcase_Description, result):
            with open(self.results_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([Testcase_Description, result, timestamp])
        return _write_result

    def test_login(self, read_test_data, write_test_result):
        for data in read_test_data:
            self.username = data['PIN']

        self.login_page.click_momo_app()
        self.login_page.enter_momo_pin(self.username)
        self.login_page.click_sign_in_button()
        login_results = self.login_page.click_skip_button()

        if login_results:
            write_test_result('Login successful', 'PASS')
        else:
            write_test_result('Login Failed', 'FAIL')
            pytest.fail("Login failed, cannot proceed to homepage test.")
        
    def test_homePage(self, write_test_result):
        homepage_results = self.home_page.get_balance()
        if homepage_results:
            write_test_result(f'Balance is displayed, Balance: {homepage_results}', 'PASS')
        else:
            write_test_result('Balance not displayed', 'FAIL')
        
    
    def test_sendMoney(self, write_test_result):
        self.send_money.ClickSend()
        self.send_money.clickSend_money_to_cell()
        self.send_money.Enter_MoMoNumber()
        self.send_money.ClickContinue_button()
        self.send_money.Select_amount()
        self.send_money.Click_continue_toSend()
        #recipient_details = self.send_money.get_recipient_details
        self.send_money.click_confirm_button()
        self.send_money.getTransaction_id()
        print(self.send_money.sucessScreen())

        trans_results = self.send_money.sucessScreen()
        if trans_results:
            write_test_result(f'Send Money to MoMo number is successful{self.send_money.trans_id}','PASS')
        else:
            write_test_result('Send Money to MoMo number failed', 'Failed')



if __name__ == "__main__":
    pytest.main()
