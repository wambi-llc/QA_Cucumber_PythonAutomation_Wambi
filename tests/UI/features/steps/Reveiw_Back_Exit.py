from behave import *
from utilities.driverUtil import driver
from pageElement.confirmPersonBeginReviewPageElements import *
from pageElement.ReviewBackExitPageElements import *
import utilities.config as sconfig
import time

use_step_matcher("re")


@step("I have started the survey questions for my selected person")
def step_impl(context):
    time.sleep(2)
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "Team Member search page is not displaying correctly"
    #time.sleep(2)
    #driver.enterValues(searchPerson, 'test')
    #time.sleep(5)
    driver.elementClick(selectPerson)
    time.sleep(2)
    #driver.enterValues(selectDepartment,'Neurology')
    #time.sleep(2)
    driver.pressTab()
    driver.pressEnter()

@when("I tap on the Wambi bird \(the design may change\) in the top left,")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(wambiBirdLog)
    driver.elementClick(wambiBirdLog)



@then("I am redirected back to the Search Location screen")
def step_impl(context):
    time.sleep(2)
    assert driver.getCurrentURL() == sconfig.patientPortalLocation, "Search Location screen is not redirected properly"


