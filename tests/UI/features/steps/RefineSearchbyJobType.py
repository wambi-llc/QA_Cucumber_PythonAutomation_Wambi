from behave import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
from pageElement.confirmPersonBeginReviewPageElements import *
import utilities.config as sconfig
import requests
import json
import time
import os
use_step_matcher("re")


@given("I login to patient portal user")
def step_impl(context):
    time.sleep(2)
    driver.navigate(sconfig.patientPortalLoginpage)
    time.sleep(2)
    driver.enterValues(emailInput,'cpcstaging@gmail.com')
    time.sleep(2)
    driver.waitOnElement(Submit)
    driver.elementClick(Submit)
    #Get OTP
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



@step("have searched for the person I want to recognize")
def step_impl(context):
    time.sleep(5)
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
    # Get OTP Verfication
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
    #driver.pressTab()
    #driver.pressTab()
    #driver.pressEnter()
    time.sleep(2)

    driver.enterValues(searchPerson, 'john')
    time.sleep(2)
    driver.pressEnter()
    time.sleep(5)



@when("I click the Job Type button")
def step_impl(context):
    time.sleep(2)
    print(driver.getTextForElement(jobType))
    driver.waitOnElement(jobType)
    driver.elementClick(jobType)
    time.sleep(5)

@then("I can see a list of Job Types")
def step_impl(context):
    getJobTypesList = driver.getElements(jobTypeList)
    for counter in range(len(getJobTypesList)):
        print(getJobTypesList[counter].text)
    #assert "NEXT" in verConfBox[counter].text, "confirmation Box is not displaying c


@step("can search the list by entering text\.")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchbyJobType,'Nurse Manager')
    time.sleep(2)
    #driver.pressEnte
    driver.pressKeyDown()


@step("can select one")
def step_impl(context):
    time.sleep(5)
    #print(driver.getElements(selectedJobType))
    driver.moveToElement(selectedJobType)
    driver.elementClick(selectedJobType)


@step("have clicked the \+ Job Type button")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(jobType)
    driver.elementClick(jobType)
    time.sleep(2)


@then("the job type I selected is indicated above the result list")
def step_impl(context):
    print(driver.getTextForElement(jobTyperesult))
    assert driver.getTextForElement(jobTyperesult) == 'Associate Nurse Manager', "Selected Job type is not displaying correctly"


@step("any previously selected job type is replaced")
def step_impl(context):
    time.sleep(2)
    driver.elementClick(closeJobType)
    time.sleep(2)
    driver.waitOnElement(jobType)
    driver.elementClick(jobType)
    time.sleep(2)
    driver.enterValues(searchbyJobType, 'RN Clinical I')
    time.sleep(2)
    driver.pressEnter()
    driver.waitOnElement(selectedJobType)
    driver.elementClick(selectedJobType)



@step("the results list is updated to show only people with my selected job type\.")
def step_impl(context):
    time.sleep(2)
    print(driver.getTextForElement(jobTyperesult))
    assert driver.getTextForElement(jobTyperesult) == 'RN Clinical I', "Selected Job type is not replaced correctly"
    time.sleep(2)


