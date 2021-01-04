from behave import *
from pageElement.userProfilepageElements import *
from utilities.driverUtil import driver
import time
import os
import string
import random

use_step_matcher("re")


@step("click on UsersProfile image")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userImage)
    driver.elementClick(userImage)


@step("click on users name")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userName)
    driver.elementClick(userName)


@step('Scroll down to the Bio Info section and hover over the "\?" bubble')
def step_impl(context):
    time.sleep(2)
    driver.pressEnter()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)


@step("enter text in Bio Info tab")
def step_impl(context):
    driver.clearElement(bioInfoText)
    global randomText
    randomText = random.randint(100,1000000000000)
    driver.enterValues(bioInfoText, randomText)
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)




@then("submit the Bio Request")
def step_impl(context):
    #time.sleep(2)
    driver.pressEnter()

@then("it should route to Mypage tab")
def step_impl(context):
    time.sleep(2)
    assert driver.getCurrentURL() == "https://dev.wambiapp.com/admin", "Not routing to MyPage tab"


@then("I validate that the Bio Info has been changed")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(userImage)
    driver.elementClick(userImage)
    time.sleep(2)
    time.sleep(2)
    driver.waitOnElement(userName)
    driver.elementClick(userName)
    time.sleep(2)
    driver.pressEnter()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    driver.pressKeyDown()
    time.sleep(2)
    print(randomText)
    print(driver.getElementbyvalue(bioInfoText))
    assert int(driver.getElementbyvalue(bioInfoText)) == randomText, "UserProfile has not updated correctly"