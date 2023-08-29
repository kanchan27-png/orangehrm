import time

import allure
from allure_commons.types import AttachmentType

from pageObjects.Loginpage import OrangeHRM_Login
from utilities.Logger import LogGenerator
from utilities.ReadConfig import Readconfig

# folder#file#class

class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()
    log = LogGenerator.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/")
    @allure.title(" Page Title Test Case")
    @allure.issue("ABC123")
    @allure.story(" This is story#1")
    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup  # open browser # url orangehrm
        self.log.info("Page Title is " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            time.sleep(4)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_page_title_001_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("G:\\OrangeHRM\\Screenshots\\test_page_title_001_pass.png")
            #self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot("G:\\OrangeHRM\\Screenshots\\test_page_title_001_fail.png")
            #self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False
        self.log.info("Testcase test_page_title_001 is completed\n")

    def test_login_002(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering password :" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Clicking in login button :" + self.Password)
        self.lp.Click_Login()
        # print(self.lp.Login_Status())
        self.log.info("Checking login status")
        if self.lp.Login_Status() == True:
            self.log.info("taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_002_fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("G:\\OrangeHRM\\Screenshots\\test_login_002_pass.png")

            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout()
            #self.driver.close()
            self.log.info("Testcase test_login_002 is passed")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_002_pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("G:\\OrangeHRM\\Screenshots\\test_page_title_001_fail.png")
            #self.driver.close()
            self.log.info("Testcase test_login_002 is failed")
            assert False
        self.log.info("Testcase test_login_002 is completed\n")

# pytest -v -n=2 --html=Reports/OrangeHRMreport.html --alluredir="Allure-results" --browser firefox