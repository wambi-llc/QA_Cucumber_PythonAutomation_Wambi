from behave import *
from pageElement.troubleSigninPageElements import *
from pageElement.loginPageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random

use_step_matcher("re")


@given("I am Tina")
def step_impl(context):
    time.sleep(2)



@step("I have navigated to the Wambi URL")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.wambiNewURL)

@step("I do not remember my username/password Or I do not have a username/password")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(usrName)
    #driver.elementClick(userNameLoginPage)
    driver.enterValues(usrName, sconfig.usrname)
    #driver.elementClick(passwordLoginPage)
    time.sleep(1)
    driver.enterValues(password, sconfig.pword)



@when("I click the “Trouble signing in\?” link")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(troubleSignin)
    driver.elementClick(troubleSignin)


@then("the Sign In Help window appears")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(signinHelp)
    print(driver.getTextForElement(signinHelp))
    assert driver.getTextForElement(signinHelp) == 'Sign In Help', "The Sign In Help window is not appearing"