from behave import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
from pageElement.Prompt_NomintateNurseDaisyAwardPageElements import *
from pageElement.reviewBackQuestionsPageElements import *
from pageElement.confirmPersonBeginReviewPageElements import *
import utilities.config as sconfig
import time
import os
import requests
import json
use_step_matcher("re")

@step("I have searched for the person I want to recognize")
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

    time.sleep(2)

    driver.enterValues(searchPerson, 'Brittany J')


@step("the modal is open with the correct person’s information")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(selectPerson)
    driver.elementClick(selectPerson)
    time.sleep(2)
    chkModal = driver.getElements(checkModalbox)
    for counter in range(len(chkModal)):
        print(chkModal[counter].text)
    assert "Brittany J" in chkModal[counter].text, "Modal Box is not displaying correctly"

@step("the correct Unit/Department is selected")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(selectUnit_Dept)
    getUnit_Deptlist = driver.getElements(selectUnit_Dept)
    time.sleep(2)
    getUnit_Deptlist[0].click()
    time.sleep(2)
    driver.waitOnElement(unitList)
    driver.elementClick(unitList)
    time.sleep(2)


@when("I tap on the Begin Review button")
def step_impl(context):
    driver.pressTab()
    driver.pressEnter()


@then("I am navigated to the 1st step in the Survey questions for my selected person")
def step_impl(context):
    time.sleep(2)
    checkFirstStep = driver.getTextForElement(chkstep)
    print(driver.getTextForElement(chkstep))
    assert driver.getTextForElement(chkstep) == "1 / 5","Navigated to the 1st step in Survey Questions"
    time.sleep(2)

