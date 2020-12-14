from behave import *
from utilities.driverUtil import driver
from pageElement.confirmPersonBeginReviewPageElements import *
from pageElement.ReviewBackExitPageElements import *
from pageElement.reviewBackQuestionsPageElements import *
import utilities.config as sconfig
import time
use_step_matcher("re")


@step("want to change my answer or see how I responded")
def step_impl(context):
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "Team Member search page is not displaying correctly"
    time.sleep(5)
    driver.elementClick(selectPerson)
    #time.sleep(2)
    #driver.enterValues(selectDepartment, 'Neurology')
    time.sleep(2)
    driver.elementClick(beginReview)


@when("I tap on “Back” Then I am returned to the previous review question")
def step_impl(context):
    time.sleep(2)
    driver.elementClick(question1)
    time.sleep(3)
    driver.elementClick(question1)
    time.sleep(3)
    driver.elementClick(back)
    time.sleep(2)

@step("can change my response")
def step_impl(context):
    driver.elementClick(question1)
    print(driver.getTextForElement(question1))
    assert driver.getTextForElement(question1) == 'Poor', "Not able to change the response"
