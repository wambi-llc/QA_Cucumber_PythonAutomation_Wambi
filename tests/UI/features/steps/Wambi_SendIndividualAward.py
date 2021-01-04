from behave import *
from pageElement.awardsElements import *
from utilities.driverUtil import driver
import time
import os
import string
import random

use_step_matcher("re")


@step("I click on Individual Award")
def step_impl(context):
    time.sleep(2)
    driver.moveToElement(IndividualAward)
    driver.elementClick(IndividualAward)



@step("I select a Select Individuals, Employee Award,AwardType, Spedify details,TimePeriod and Badge")
def step_impl(context):
    time.sleep(2)
    driver.pressTab()
    time.sleep(5)
    driver.enterValues(selIndividual,'wambi')
    time.sleep(5)
    driver.pressEnter()
    time.sleep(2)
    driver.pressEnter()
    time.sleep(5)
    driver.enterValues(selIndividual, 'dursley')
    time.sleep(5)
    driver.pressEnter()
    time.sleep(2)
    driver.pressEnter()
    time.sleep(5)
    #********************** select Employee Award ***************
    driver.pressTab()
    time.sleep(2)
    driver.waitOnElement(selEmployee)
    driver.elementClick(selEmployee)
    driver.pressEnter()
    time.sleep(3)
    # ******** select TimePeriod*************
    driver.moveToElement(selTimePeriod)
    driver.elementClick(selTimePeriod)
    driver.pressEnter()
    time.sleep(2)
    # ******** select Badge*************
    #time.sleep(5)
    driver.moveToElement(selBadge)
    driver.elementClick(selBadge)
    driver.pressEnter()
    time.sleep(2)


@then("I press Submit individual award at the bottom of the Page")
def step_impl(context):
    driver.pressTab()
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressEnter()


@step("Search for the newly created Individual Award in the Search bar")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchText, 'Innovation Award')
    time.sleep(2)
    driver.elementClick(submit)


@then("I validate that the new created Award does show up in search results")
def step_impl(context):
    time.sleep(15)
    print(driver.getTextForElement(searchResult))
    assert driver.getTextForElement(searchResult) == 'Innovation Award', 'Newly Created Individual award is not displaying in search results'
