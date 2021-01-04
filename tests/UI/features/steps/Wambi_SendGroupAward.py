from behave import *
from pageElement.awardsElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random

use_step_matcher("re")


@when("I hover on Awards Tab Solution")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(awardsTab)
    driver.moveToElement(awardsTab)
    time.sleep(2)

@step('I click on "Post Award" option')
def step_impl(context):
    driver.waitOnElement(addAwards)
    driver.elementClick(addAwards)
    time.sleep(5)


@step("I select a random facility, random clinic/department,AwardType, TimePeriod and Badge")
def step_impl(context):
    driver.waitOnElement(clickFacilities)
    driver.elementClick(clickFacilities)
    time.sleep(2)
    driver.waitOnElement(selectFacilities)
    driver.elementClick(selectFacilities)
    # ***************** Select Clinic Options **************************
    time.sleep(5)
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(10)
    # **************** Select Discipline *********
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    ## **************** Select AwardType *********
    time.sleep(2)
    driver.waitOnElement(clickAwardType)
    driver.elementClick(clickAwardType)
    time.sleep(4)
    driver.waitOnElement(selectAward)
    global text1
    text1 = driver.getTextForElement(selectAward)
    driver.elementClick(selectAward)
    #driver.pressEnter()
    #******** specifyDetails*************

    note = random.randint(100, 100000000)
    time.sleep(2)
    driver.pressTab()
    driver.enterValues(specifyDetails, note)
   # driver.pressTab()
    # ******** select TimePeriod*************
    time.sleep(2)
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    # ******** select Badge*************
    time.sleep(2)
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(2)


@then("I press Submit at the bottom of the Page")
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(submit)
    driver.elementClick(submit)

@when("I click on Awards Tab Solution")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(awardsTab)
    driver.elementClick(awardsTab)


@step("Search for the newly created Group Award in the Search bar")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchText, 'Innovation Award')
    time.sleep(2)
    driver.elementClick(submit)


@then("I validate that the new Group Award does show up in search results")
def step_impl(context):
    time.sleep(15)
    print(driver.getTextForElement(searchResult))
    assert driver.getTextForElement(searchResult) == 'Innovation Award', 'Group award is not displaying in search results'
