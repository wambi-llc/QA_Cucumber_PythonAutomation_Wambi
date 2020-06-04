from behave import *
from utilities.driverUtil import driver

use_step_matcher("re")





class loginscreen_locators():

    #def __init__(self, driver):
       # self.driver = driver
        # self.clockid.textbox_name = 'clockid'
        # self.password.textbox_name = 'password'
        # self.submitButton_id = 'submit'

    def enterUsername(self):
        #driver.wait_until(self.usernameField);
        #//*[@id="clockid"]
        driverUtil.driver.find_element_by_xpath("//input[@name='clockid']").clear()
        #driver.find_element_by_xpath.send_keys("dummytext")

            # driver.find_element_by_xpath("//input[@name='self.clockid.textbox_name']").clear
            # driver.find_element_by_xpath("//input[@name='self.clockid.textbox_name']").send_keys(clockid)

    def enterPassword(self, password):
            driverUtil.driver.find_element_by_xpath("//input[@name='self.password.textbox_name']").clear
            driverUtil.driver.find_element_by_xpath("//input[@name='self.password.textbox_name']").send_keys(password)

    def click_login(self):
            driver.find_element_by_xpath("//button[@type='submitButton_id']").click()
