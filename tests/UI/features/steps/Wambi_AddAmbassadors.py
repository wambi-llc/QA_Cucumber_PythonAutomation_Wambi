from behave import *
from pageElement.ambassadorsPageElements import *
from pageElement.myPageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random
use_step_matcher("re")





@when("I hover on Ambassadors Tab Solution")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Ambassadors)
    driver.moveToElement(Ambassadors)


@step('I click on "Add a Ambassador" option')
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(addAmbassador)
    driver.elementClick(addAmbassador)
    time.sleep(2)


@step("I select a random facility, random clinic/department")
def step_impl(context):
    time.sleep(5)
    driver.waitOnElement(clickFacilityOption)
    driver.elementClick(clickFacilityOption)
    time.sleep(4)
    driver.elementClick(selectFacilities)
    time.sleep(10)
    # ***************** Select Clinic Options **************************
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(10)


@step("I generate a random number between 3 and 50 digits for the Abassador ID")
def step_impl(context):
    global ambId
    ambId = random.randint(100, 100000000)
    driver.enterValues(name, ambId)
    driver.pressTab()


@then("I press Submit at the bottom of the Ambassador Registration Page")
def step_impl(context):
    time.sleep(2)
    driver.elementClick(submit)

@when("I click on Ambassadors Tab Solution")
def step_impl(context):
    time.sleep(2)
    print(ambId)
    driver.elementClick(Ambassadors)

@step("Search for the newly created Ambassador  Name in the Search bar")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchambId,ambId)
    time.sleep(2)
    driver.elementClick(search)


@then("I validate that the new Ambassador does show up in search results")
def step_impl(context):
      assert int(driver.getTextForElement(searchResult)) == ambId, "new Ambassador is not displaying in search results"