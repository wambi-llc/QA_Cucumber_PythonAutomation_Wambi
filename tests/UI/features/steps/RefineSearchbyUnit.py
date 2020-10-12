from behave import *
from utilities.driverUtil import driver
from pageElement.refineSearchbyUnitPageElements import *
import time
use_step_matcher("re")



@when("I click the \+ Unit button")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Unit)
    driver.elementClick(Unit)


@then("I can see a list of Units")
def step_impl(context):
    time.sleep(2)
    getListUnits = driver.getElements(unitList)
    for counter in range(len(getListUnits)):
        print(getListUnits[counter].text)


@step("can search the list of Units by entering text\.")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchUnits,'ALC Maternity')
    time.sleep(2)



@step("can select one from the list of Units")
def step_impl(context):
    time.sleep(2)
    driver.moveToElement(filterbySearchUnits)
    driver.elementClick(filterbySearchUnits)





@then("the unit I selected is indicated above the result list")
def step_impl(context):
    time.sleep(2)
    print(driver.getTextForElement(selectedUnit))
    assert driver.getTextForElement(selectedUnit) == 'ALC Maternity', "Selected Unit is not displaying in result list"


@step("any previously selected unit is replaced")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(closeUnitList)
    driver.elementClick(closeUnitList)
    time.sleep(2)
    driver.waitOnElement(Unit)
    driver.elementClick(Unit)
    time.sleep(3)
    driver.enterValues(searchUnits,'Critical')
    time.sleep(5)
    driver.waitOnElement(filterbySearchUnits)
    driver.elementClick(filterbySearchUnits)
    time.sleep(2)
    print(driver.getTextForElement(replacedUnit))
    assert driver.getTextForElement(replacedUnit) == 'ALC Critical Care', "Selected Unit is not replaced"


@step("the results list is updated to show only people with my selected unit\.")
def step_impl(context):
    time.sleep(2)
    searchResults = driver.getElements(resultList)
    for counter in range(len(searchResults)):
        print(searchResults[counter].text)
    time.sleep(2)


