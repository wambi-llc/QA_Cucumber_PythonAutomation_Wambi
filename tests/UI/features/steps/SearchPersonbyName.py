from behave import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.confirmPersonBeginReviewPageElements import *
from pageElement.searchPersonbyNamePageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
import utilities.config as sconfig
import time
import os
import requests
import json
use_step_matcher("re")


@step("I have selected a location Or been sent directly to this page from the chatbot")
def step_impl(context):
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)
    driver.pressTab()
    time.sleep(2)
    driver.pressTab()
    driver.pressEnter()
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == sconfig.patientPortalLoginpage, "Team Member Login page is not displaying correctly"
    time.sleep(2)
    driver.enterValues(emailInput, 'cpcstaging@gmail.com')
    time.sleep(2)
    driver.waitOnElement(Submit)
    driver.elementClick(Submit)
    #Get OTP Verfication
    res = requests.get(sconfig.getOTP)
    dirname = os.path.dirname(__file__)
    jsonfile = os.path.join(dirname, 'responsedata.json')
    responsedata = {}
    # json resonse data in encoding form
    responsedata = json.dumps(res.json())
    # create json file and write the jsonresponse data
    with open(jsonfile, 'w') as json_files:
        json_files.write(responsedata)
    # read the json encoded file and decode the json data
    with open(jsonfile, 'r') as jsonfiles:
        # data = jsonfiles.read()
        dataDict = json.load(jsonfiles)
        getOTP = dataDict['token']
        patientId = dataDict['patientId']
    time.sleep(5)
    driver.enterValues(enterOTP, getOTP)
    time.sleep(2)
    driver.waitOnElement(chkTerms)
    driver.elementClick(chkTerms)
    time.sleep(2)
    driver.waitOnElement(submitbtn)
    driver.elementClick(submitbtn)
    time.sleep(2)

@when("the page loads")
def step_impl(context):
    time.sleep(10)

@then("I can see a list of the first 10 people")
def step_impl(context):
    global searchList
    time.sleep(5)
    driver.waitOnElement(resultList)
    searchList = driver.getTextForElement(resultList)
    print(len(searchList))
    assert len(searchList) is not None, "list of peoples are not loaded more then 10 people"


@step("the list is scrollable to load more")
def step_impl(context):
    time.sleep(10)


@step("the list is sorted alphabetically by last name")
def step_impl(context):
    global searchList1
    time.sleep(30)
    driver.waitOnElement(resultList)
    searchList1 = driver.getTextForElement(resultList)
    print(len(searchList1))


@step("I am on the search for person screen")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "Team Member search page is not displaying correctly"

@when("I enter text in the search box")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchPerson, 'Wambi')


@then("the list of people is filtered to match my search text")
def step_impl(context):
    global searchList
    time.sleep(5)
    driver.waitOnElement(resultList)
    searchList = driver.getTextForElement(resultList)
    print(len(searchList))

