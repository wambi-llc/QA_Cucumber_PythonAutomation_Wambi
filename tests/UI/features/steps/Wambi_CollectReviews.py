from behave import *
from pageElement.troubleSigninPageElements import *
from pageElement.collectReviewPageElements import *
from pageElement.loginPageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random

use_step_matcher("re")


@given("Navigate to https://dev-w4\.wambiapp\.com/auth/login")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.wambiNewURL)


@step("I enter username and password and click Login to login as Admin User")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(usrName)
    # driver.elementClick(userNameLoginPage)
    driver.enterValues(usrName, sconfig.myPortalUserid)
    # driver.elementClick(passwordLoginPage)
    time.sleep(1)
    driver.enterValues(password, sconfig.myPortalPwd)
    time.sleep(2)
    driver.waitOnElement(loginbtn)
    driver.elementClick(loginbtn)


@then("You are taken to https://dev-w4\.wambiapp\.com/admin")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev-w4.wambiapp.com/admin', "It is not navigating to admin URL"


@step("Click on your profile icon")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(profileIcon)
    driver.elementClick(profileIcon)

@step("Click on Collect Patient Gratitude")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(collectPatientGratitude)
    driver.elementClick(collectPatientGratitude)


@then("User is routed to the /portal/location page and can select their location")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev-w4.wambiapp.com/portal/location?id=a26b5598b2b', "It is not routed to portal location page"

@then("There should be more than one location")
def step_impl(context):
    time.sleep(2)
    print(len(driver.getElements(locCount)))
    assert len(driver.getElements(locCount)) > 1, "No more then  one location is present"

@step("Select your location and click Continue")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(selLocation)
    driver.elementClick(selLocation)
    time.sleep(2)
    driver.waitOnElement(NEXT)
    driver.elementClick(NEXT)

@then("User is routed to the /portal/employee \(Who would you like to recognize\)")
def step_impl(context):
    time.sleep(2)
    assert driver.getTextForElement(whoWouldyouText) == 'Who would you',"Who would you Text is not dispaying"
    assert driver.getTextForElement(liketoRecognizeText) == 'like to recognize?',"like to rcognize? text is not displaying correctly"

@when("Attempt to access wambi app")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.wambiNewURL)


@then("User should not be able to   access the Wambi app without reauthetcating")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev-w4.wambiapp.com/auth/login', "User is able to access Wambi Appp without reauthenticating"


@given("I am a leader")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.wambiNewURL)
    time.sleep(2)
    driver.waitOnElement(usrName)
    # driver.elementClick(userNameLoginPage)
    driver.enterValues(usrName, sconfig.multiplePortalUserid)
    # driver.elementClick(passwordLoginPage)
    time.sleep(1)
    driver.enterValues(password, sconfig.multiplePortalPwd)
    time.sleep(2)
    driver.waitOnElement(loginbtn)
    driver.elementClick(loginbtn)


@step("I have permissions to collect reviews for team members")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(profileIcon)
    driver.elementClick(profileIcon)


@when("I click on the Collect Patient Gratitude menu item")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(collectPatientGratitude)
    driver.elementClick(collectPatientGratitude)


@then("I am prompted to select one of my available portals")
def step_impl(context):
    time.sleep(2)
    assert driver.getTextForElement(selectPortal) == 'Select a portal:',"Available portals are not displaying correctly"
    time.sleep(2)
    driver.waitOnElement(clickPortal)
    driver.elementClick(clickPortal)
    time.sleep(2)
    driver.waitOnElement(continuebtn)
    driver.elementClick(continuebtn)


@step("am taken directly to the portal")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev-w4.wambiapp.com/portal/location?id=2c9214f1cd15', "It is not routed to portal location page"


@step("am already authenticated as a portal user")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(selLocation1)
    driver.elementClick(selLocation1)
    time.sleep(2)
    driver.waitOnElement(NEXT)
    driver.elementClick(NEXT)


@step("am logged out of the team member interface")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.wambiNewURL)
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev-w4.wambiapp.com/auth/login', "User is able to access Wambi Appp without reauthenticating"



