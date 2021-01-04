from behave import *
from pageElement.wambiplatformElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")
from selenium import webdriver
import re


@given("I have navigated to the Wambi application")
def step_impl(context):
    driver.navigate('https://dev-w4.wambiapp.com/')
    driver.waitOnElement(wambiUsername)
    driver.waitOnElement(wambiPassword)

@step("I have logged in")
def step_impl(context):
    driver.enterValues(wambiUsername, 'W00046')
    driver.enterValues(wambiPassword, 'W00046')
    driver.elementClick(wambiLogIn)

@then("I am able to click on all the navigation buttons")
def step_impl(context):
    driver.waitOnElement(wambiSendEmail)
    driver.waitOnElement(wambiDashboard)
    driver.waitOnElement(wambiCarePostCard)
    driver.waitOnElement(wambiChallenges)
    driver.waitOnElement(wambiNotifications)

@then("I am able to view my profile")
def step_impl(context):
    driver.waitOnElement(wambiProfile)
    driver.elementClick(wambiProfile)

@step("I am able to view the available tabs")
def step_impl(context):
    driver.waitOnElement(wambiUsername)
    if driver.driver.wambiUsername.is_displayed():
        raise Exception('uh oh')

@then("I am able to sign out")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am able to sign out')


@when("I attempt to log in without entering a username or password")
def step_impl(context):
    driver.waitOnElement(wambiUsername)

@then("I will not be able to click the log in button")
def step_impl(context):
    if driver.driver.find_element_by_xpath("/html/body/div/main/section/div[1]/form/div[3]/button").is_enabled() == True:
        raise Exception('Log in button unexpectedly enabled')

@when("I attempt to log in without entering a password")
def step_impl(context):
    driver.waitOnElement(wambiUsername)
    driver.enterValues(wambiUsername,'W00046')

@when("I input a username with an incorrect password")
def step_impl(context):
    driver.enterValues(wambiPassword, 'VanDammeKick')

@then("I will be able to click the log in button")
def step_impl(context):
    driver.waitOnElement(wambiLogIn)
    driver.elementClick(wambiLogIn)

@step("I will not be able to log in and an error message will display")
def step_impl(context):
    driver.waitOnElement(wambiErrorMessage)
    if  re.match('Username / Password not found', str(driver.getTextForElement(wambiErrorMessage))) == None:
        raise ValueError('Expected error text not found')