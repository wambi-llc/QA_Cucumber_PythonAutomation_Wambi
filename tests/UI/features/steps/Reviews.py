from behave import *
from pageElement.HomePageElements import *
from pageElement.ReviewElements import *
from pageElement.myPageElements import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.changLocationPageElements import *
from pageElement.confirmPersonBeginReviewPageElements import *
from pageElement.reviewBackQuestionsPageElements import *
from pageElement.ReviewCommentsContactMePageElements import *
from pageElement.Prompt_NomintateNurseDaisyAwardPageElements import *
import time
import string
import random
import re

use_step_matcher("re")


@then("I click on Reviews Tab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Reviews)
    driver.elementClick(Reviews)
    time.sleep(2)


@step(
    "click submit, click on a person, press start review, and navigate through the review until I reach the comment page")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)
    driver.waitOnElement(NEXT)
    driver.elementClick(NEXT)
    time.sleep(2)
    driver.enterValues(searchPerson, 'Wambi Super Admin Edna')
    time.sleep(2)

    time.sleep(2)
    driver.waitOnElement(selectNurse)
    driver.elementClick(selectNurse)
    time.sleep(2)
    driver.waitOnElement(clickClinic)
    driver.elementClick(clickClinic)

    time.sleep(2)
    driver.waitOnElement(selectClinic)
    driver.elementClick(selectClinic)
    time.sleep(2)
    driver.waitOnElement(chkTerms)
    driver.elementClick(chkTerms)
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressEnter()
    time.sleep(2)
    driver.elementClick(question1)
    time.sleep(2)
    driver.elementClick(question1)
    time.sleep(2)
    driver.elementClick(question1)
    time.sleep(2)
    driver.elementClick(question1)
    time.sleep(2)
    driver.elementClick(question1)


@then("in the comment bubble I add a random text and validate the spellcheck error line show after pressing space")
def step_impl(context):

    Text = ''.join(random.choice(string.ascii_letters) for i in range(10))
    driver.waitOnElement(enterComments)
    driver.enterValues(enterComments, Text)
    assert driver.tagAttributes(textAreaElem, 'spellcheck') == "true", "spell check is not highlighted as  "

