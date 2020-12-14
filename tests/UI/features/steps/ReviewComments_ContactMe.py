from behave import *
from utilities.driverUtil import driver
from pageElement.ReviewBackExitPageElements import *
from pageElement.reviewBackQuestionsPageElements import *
from pageElement.ReviewCommentsContactMePageElements import *
import utilities.config as sconfig
import time
import random
import string
use_step_matcher("re")

@step("am reviewing someone")
def step_impl(context):
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "Team Member search page is not displaying correctly"
    ##driver.enterValues(searchbyPerson, 'test')
    time.sleep(5)
    driver.elementClick(selectPerson)
    time.sleep(2)
    driver.elementClick(beginReview)


@when("I rate a question at or below the configured setting to prompt for a comment \(  \)")
def step_impl(context):
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
    time.sleep(2)



@then("I am prompted to enter a comment")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(enterComments)



@step("I can tap to enter a comment")
def step_impl(context):
    time.sleep(2)
    Text = ''.join(random.choice(string.ascii_letters) for i in range(10))
    driver.enterValues(enterComments, Text)


@step("my comment text is checked for spelling errors by my browser")
def step_impl(context):
    time.sleep(2)
    assert driver.tagAttributes(textAreaElem, 'spellcheck') == "true", "spell check is not highlighted for comment text area"
    time.sleep(2)
    driver.elementClick(back)
    time.sleep(2)
    driver.elementClick(wambiBirdLog)
    time.sleep(2)


@when("I toggle On the setting to “Contact Me”")
def step_impl(context):
    time.sleep(2)
    #driver.waitOnElement(toggleContactMe)
    driver.elementClick(toggleContactMe)


@then("a form appears asking me for my contact information\.")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(firstName)
    driver.enterValues(firstName,'test')
    time.sleep(2)
    driver.waitOnElement(lastName)
    driver.enterValues(lastName,'test')
    time.sleep(2)


@step("my phone # or email address is already entered \(from authentication WP-525\)")
def step_impl(context):
    time.sleep(2)
    print(driver.tagAttributes(email,'value'))
    assert driver.tagAttributes(email,'value') == 'on', "email address is not entering correct id"
    time.sleep(2)
    driver.elementClick(back)
    time.sleep(2)


