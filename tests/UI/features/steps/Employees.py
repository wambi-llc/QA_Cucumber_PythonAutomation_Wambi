from behave import *
from pageElement.loginPageElements import *
from pageElement.employeesElements import *
import utilities.config as sconfig
from selenium.webdriver import *
from allure_behave.hooks import allure_report
import time
import os
import glob
from utilities.driverUtil import driver
use_step_matcher("re")

driver.clear_cookies()

@given("I navigate to Wambi Application")
def step_impl(context):

    driver.navigate(sconfig.testurl)

    driver.waitFor(2)

@step("I click on Team Member Login")
def step_impl(context):

    driver.waitOnElement(teamMemberLoginButton)
    driver.elementClick(teamMemberLoginButton)

@step("I enter username and password and click Login")
def step_impl(context):

    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.usrname)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)
    driver.elementClick(submitButtonLoginPage)



@when("I click on Employees Tab Solution")
def step_impl(context):

    time.sleep(10)
    driver.waitOnElement(employeesTab)
    driver.elementClick(employeesTab)

@step("I click on Excel button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(10)
    driver.waitOnElement(excelButton)
    driver.elementClick(excelButton)



@then("I validate the Excel sheet downloads")
def step_impl(context):

    home = os.path.expanduser('~')
    downloadspath = os.path.join(home,"downloads")
    list_of_files = glob.glob(downloadspath + "/*.xls")
    try:
     latest_file = max(list_of_files, key=os.path.getctime)
     print ('Download Excelsheet is in Downloads directory' + latest_file)
    except OSError:
     print ('Excel file is not downloaded' + 'FAIL' )

    driver.closeBrowser()
