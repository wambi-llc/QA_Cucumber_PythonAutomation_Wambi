from behave import *
from pageElement.loginPageElements import *
from pageElement.HomePageElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
import time
import datetime
import re

use_step_matcher("re")


@given("I am a Wambi Admin \(SE, SA\)")
def step_impl(context):
    driver.clear_cookies()
    driver.navigate(sconfig.testurl)
    driver.waitFor(2)
    driver.elementClick(teamMemberLoginButton)


@step("I am logged in")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.usrname)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)
    driver.elementClick(submitButtonLoginPage)


@when("I click on Reviews Tab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Reviews)
    driver.elementClick(Reviews)


@then("I logged out from Wambi Site and navigate to Patient Portal")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    print(driver.getTextForElement(portaldevHomepage))
    assert 'Recognize the people that' in driver.getTextForElement(portaldevHomepage) , "It s not logged out from Wambi site"
