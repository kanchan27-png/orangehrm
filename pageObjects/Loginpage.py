import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM_Login:
    Text_Username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME, "password")
    Click_login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Menu_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # task poll frequency # default frequency
        # total 10... if the element visible in 3 sec then it will not take complete 10 sec for next operation

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Name))
        self.driver.find_element(*OrangeHRM_Login.Text_Username_Name).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*OrangeHRM_Login.Text_Password_Name).send_keys(password)

    def Click_Login(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_login_XPATH))
        self.driver.find_element(*OrangeHRM_Login.Click_login_XPATH).click()

    def Click_Menu(self):
        self.driver.find_element(*OrangeHRM_Login.Click_Menu_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*OrangeHRM_Login.Click_Logout_XPATH).click()

    def Login_Status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_XPATH))
            self.driver.find_element(*OrangeHRM_Login.Click_Menu_XPATH)
            return True
        except:
            return False