from behave import *
from pageElement.loginPageElements import *
from pageElement.employeesElements import *
import utilities.config as sconfig
import time
from utilities.driverUtil import driver
use_step_matcher("re")


@given("I am a User that has logged into the Wambi platform")
def step_impl(context):
    driver.clear_cookies()
    driver.navigate(sconfig.testurl)
    driver.waitFor(2)


@step("completed verification steps")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(teamMemberLoginButton)
    driver.elementClick(teamMemberLoginButton)


@step("I enter my User ID and Password on the login page as Employee or SA users")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.empUser)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)
    #driver.elementClick(submitButtonLoginPage)


@step("I click Submit")
def step_impl(context):
    time.sleep(2)
    driver.elementClick(submitButtonLoginPage)

@then("I am routed to My Page")
def step_impl(context):
    assert driver.getTextForElement(myPageTab) == 'PERKS', "It is not routed  to myPage Tab"


@step("I enter my  User ID and Password on the login page as SE user")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.usrname)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)


@then("I am routed to the Ratings tab")
def step_impl(context):
    time.sleep(2)
    assert driver.getTextForElement(ratingsTab) == 'Ratings', "It is not routed to Ratings tab"



