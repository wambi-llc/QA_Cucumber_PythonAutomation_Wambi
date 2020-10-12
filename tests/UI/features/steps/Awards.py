from behave import *
from pageElement.awardsElements import *
from pageElement.myPageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import datetime
from selenium.webdriver import *
from allure_behave import *
from allure_pytest import *
import time
import os
use_step_matcher("re")

@when("I click on Awards Tab")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(awardsTab)
    driver.elementClick(awardsTab)



@step("I Zoom In to Screen to max Zoom In allowed")
def step_impl(context):
    driver.zoomWindow()


@then("I validate the Date sub tab is showing all the text")
def step_impl(context):
    #time.sleep(20)
    validatedatetime = driver.getTextForElement(dateValue)
    assert datetime.datetime.strptime(validatedatetime, '%m/%d/%Y  %H:%M:%S'),'Datetime is not displayed properly'

@then("I validate the Action sub tab is showing all the text")
def step_impl(context):
    assert driver.getTextForElement(ActionTab) == 'Actions', "Action tab is not displaying"

    #driver.closeBrowser()