from behave import *
from pageElement.loginPageElements import *
from pageElement.employeesElements import *
import utilities.config as sconfig
import string
import random
import time
import os
import glob
from utilities.driverUtil import driver
use_step_matcher("re")
empId = 0

@given("I navigate to Wambi Application")

def test_step_impl(context):
    driver.clear_cookies()
    driver.navigate(sconfig.testurl)
    driver.waitFor(2)


@step("I click on Team Member Login")

def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(teamMemberLoginButton)
    driver.elementClick(teamMemberLoginButton)


@step("I enter username and password and click Login to login as SE User")
def test_step_impl(context):
    time.sleep(10)
    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.usrname)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)
    driver.elementClick(submitButtonLoginPage)



@when("I click on Employees Tab Solution")
def test_step_impl(context):

    time.sleep(10)
    driver.waitOnElement(employeesTab)
    driver.elementClick(employeesTab)

@step("I click on Excel button")
def test_step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(10)
    driver.waitOnElement(excelButton)
    driver.elementClick(excelButton)



@then("I validate the Excel sheet downloads")
def test_step_impl(context):
    time.sleep(10)
    home = os.path.expanduser('~')
    downloadspath = os.path.join(home,"downloads")
    list_of_files = glob.glob(downloadspath + "/*.xls")
    try:
     latest_file = max(list_of_files, key=os.path.getctime)
     print ('Download Excelsheet is in Downloads directory' + latest_file)
    except OSError:
     print ('Excel file is not downloaded' + 'FAIL' )

    #driver.closeBrowser()


@when("I hover on Employees Tab Solution")
def step_impl(context):
    time.sleep(10)
    driver.moveToElement(employeesTab)
    time.sleep(10)

@step('I click on "Add a New Employee" option')
def step_impl(context):
    driver.elementClick(addEmployeesTab)
    time.sleep(10)


@then("I choose random option from the User Type dropdown")
def step_impl(context):
    usertype = driver.getSelectedElements(selectUserType)
    selectOption = len(usertype.options) - 1
    usertype.select_by_index(random.randint(1,selectOption))


@step("I select a random facility, random clinic/department, and a random discipline")
def step_impl(context):
    time.sleep(20)
    facilities = driver.getSelectedElements(selectFacilities)
    facilitiesoption = len(facilities.options)-1
    print(facilitiesoption)
    #facilities.select_by_index(1)
    facilities.select_by_index(random.randint(1,facilitiesoption))
    time.sleep(20)
    #***************** Select Clinic Options **************************
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(10)
    #**************** Select Discipline *********
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(10)
@step("I generate a random number between 3 and 50 digits for the Employee ID")
def step_impl(context):
    driver.pressTab()
    #driver.waitOnElement(employeeId)
    global empId
    empId = random.randint(100,100000000)
    driver.enterValues(employeeId,empId)
    # ********* select job title ******
    driver.pressTab()
    driver.pressEnter()
    driver.pressKeyDown()
    driver.pressEnter()
    time.sleep(10)
    driver.pressTab()


@step("I generate a random string of letters for First Name, Last Name and Display Name")
def step_impl(context):
    driver.waitOnElement(fName)
    driver.enterValues(fName,random.choices(string.ascii_letters,k=10))
    driver.pressTab()                                                            
    #time.sleep(5)
    driver.waitOnElement(lName)
    driver.enterValues(lName,random.choices(string.ascii_letters,k=5))
    driver.pressTab()
    #time.sleep(5)
    driver.waitOnElement(displayname)
    driver.enterValues(displayname,random.choices(string.ascii_letters,k=8))


@then("I press Submit at the bottom of the Employee Registration Page")
def step_impl(context):
    time.sleep(20)
    driver.moveToElement(submitButtonemployeePage)
    driver.elementClick(submitButtonemployeePage)


@step("Search for the newly created employees First Name in the Search bar")
def step_impl(context):
    driver.waitOnElement(searchNewEmployee)
    driver.enterValues(searchNewEmployee, empId)
    time.sleep(5)
    driver.elementClick(searchSubmit)

@then("I validate that the new employee does show up in search results")
def step_impl(context):
     time.sleep(10)
     driver.pressEnter()
     validateEmpid = driver.getTextForElement(checkEmployee)
     assert int(validateEmpid) == empId, "New record is not created"

     #driver.closeBrowser()
