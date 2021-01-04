from behave import *
from pageElement.trendingPageElements import *
from pageElement.HomePageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random

use_step_matcher("re")


@when("I hover on Trending Tab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Trending)
    driver.moveToElement(Trending)


@step('I click on "Add Post" option')
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(addPost)
    driver.elementClick(addPost)


@step("I select Title, Facility,Clinic and Tag People to Post values")
def step_impl(context):
    time.sleep(2)
    global titleText
    titleText = random.randint(100, 100000000)
    #driver.enterValues(employeeId, empId)
    driver.enterValues(title,titleText)
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressEnter()
    #time.sleep(2)
    driver.waitOnElement(selFacility)
    driver.elementClick(selFacility)
    time.sleep(2)
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(2)
    driver.waitOnElement(content)
    driver.enterValues(content,random.randint(100, 100000000))


@when("I click on Trending Tab Solution")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Trending)
    driver.elementClick(Trending)


@step("Search for the newly created post in the Search bar")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(inputSearch,titleText)
    time.sleep(2)
    driver.elementClick(srchButton)


@then("I validate that the new created Trending feed post does show up in search results")
def step_impl(context):
    time.sleep(2)
    assert int(driver.getTextForElement(resultText)) == titleText, "Newly created Trending feed post is not displaying in search results"
