from behave import *
from pageElement.carepostcardElements import *
import utilities.config as sconfig
from selenium.webdriver import *
from allure_behave.hooks import allure_report
import time
import os
import glob
from utilities.driverUtil import *
from random import randint
use_step_matcher("re")

@step("I click on the sign in button")
def step_impl(context):

    driver.waitOnElement(signInButton)
    driver.elementClick(signInButton)

    driver.waitFor(2)

@step("I sign in as an admin using my email")
def step_impl(context):

    driver.waitOnElement(emailInput)
    driver.elementClick(emailInput)
    driver.enterValues(emailInput, 'vlad.sharkov@wambi.org')
    driver.elementClick(sendLinkButton)

    driver.waitFor(5)

@step("I enter the post creation screen")
def step_impl(context):
    driver.waitOnElement(postButton)
    driver.elementClick(postButton)

@when("I validate that the address to section loads properly")
def step_impl(context):
    driver.waitOnElement(addressedTo)

@step("I validate that the Carepostcard body loads properly")
def step_impl(context):
    driver.waitOnElement(cardBody)

@step("I validate that the location section loads properly")
def step_impl(context):
    driver.waitOnElement(cardLocation)

@step("I validate that the Carepostcard creation button starts off disabled")
def step_impl(context):
    driver.waitOnElement(disabledCreateCard)

@when("I fill out the addressee section with a random number")
def step_impl(context):
    global random_addressee_num
    random_addressee_num = randint(1000, 9999)
    driver.elementClick(addressedTo)
    driver.enterValues(addressedTo, "Test {}".format(random_addressee_num))

@step("I fill out the Carepostcard body with a random number")
def step_impl(context):
    driver.elementClick(cardBody)
    global random_body_num
    random_body_num = randint(1000, 9999)
    driver.enterValues(cardBody, "{}".format(random_body_num))

@step("I select a location")
def step_impl(context):
    driver.elementClick(cardLocation)
    driver.waitOnElement(cardLocationSearch)
    driver.enterValues(cardLocationSearch, 'Columbus ALZ')
    driver.elementClick(locationSelection)

@when("I post the CarePostCard")
def step_impl(context):
    driver.waitOnElement(createCard)
    driver.elementClick(createCard)

@step("I validate that the CarePostCard loads properly")
def step_impl(context):
    driver.waitOnElement(cardReviewAddressedTo)
    driver.waitOnElement(cardReviewBody)

@then("I validate that the expected addressee text is present")
def step_impl(context):
    addressed_to_text = driver.getTextForElement(cardReviewAddressedTo)
    if str(addressed_to_text) != "To: Test {}".format(random_addressee_num):
        raise ValueError('Addressed to line does not contain expected text')

@step("I validate that the expected body text is present")
def step_impl(context):
    body_text = driver.getTextForElement(cardReviewBody)
    if str(body_text) != str(random_body_num):
        raise ValueError('Body does not contain expected text')
    driver.waitFor(5)

