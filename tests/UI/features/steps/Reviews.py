from behave import *
from pageElement.HomePageElements import *
from pageElement.ReviewElements import *
from pageElement.myPageElements import *
from utilities.driverUtil import driver
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
    driver.waitOnElement(submitLocation)
    driver.elementClick(submitLocation)
    time.sleep(2)
    driver.waitOnElement(personProfile)
    driver.elementClick(personProfile)
    time.sleep(2)
    driver.waitOnElement(beginReview)
    driver.elementClick(beginReview)
    time.sleep(2)
    driver.waitOnElement(surveyAnswers)
    driver.elementClick(surveyAnswers)
    time.sleep(2)
    driver.waitOnElement(surveyAnswers2)
    driver.elementClick(surveyAnswers2)
    time.sleep(2)
    driver.waitOnElement(surveyAnswers3)
    driver.elementClick(surveyAnswers3)
    time.sleep(2)
    driver.waitOnElement(surveyAnswers4)
    driver.elementClick(surveyAnswers4)
    time.sleep(2)
    driver.waitOnElement(surveyAnswers5)
    driver.elementClick(surveyAnswers5)
    time.sleep(2)

@then("in the comment bubble I add a random text and validate the spellcheck error line show after pressing space")
def step_impl(context):

    Text = ''.join(random.choice(string.ascii_letters) for i in range(10))
    driver.waitOnElement(commentBubbleSection)
    driver.enterValues(commentBubbleSection, Text)
    assert driver.tagAttributes(textAreaElem, 'spellcheck') == "true", "spell check is not highlighted as  "

