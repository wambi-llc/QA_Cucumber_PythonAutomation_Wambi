from behave import *
from utilities.driverUtil import driver
from pageElement.confirmPersonBeginReviewPageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.Prompt_NomintateNurseDaisyAwardPageElements import *
from pageElement.reviewBackQuestionsPageElements import *
from pageElement.ReviewCommentsContactMePageElements import *
import utilities.config as sconfig
import time
import os
import requests
import json
use_step_matcher("re")

@step("I have completed a review for a nurse")
def step_impl(context):

    time.sleep(2)
    driver.waitOnElement(selectNurse)
    driver.elementClick(selectNurse)
    time.sleep(2)
    driver.waitOnElement(clickClinic)
    driver.elementClick(clickClinic)

    time.sleep(2)
    driver.waitOnElement(selectClinic)
    driver.elementClick(selectClinic)
    time.sleep(2)

    driver.pressTab()
    time.sleep(2)
    driver.pressEnter()
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


@when("I have completed OR skipped the Share your Gratitude screen")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(textareaInput, 'test')
    time.sleep(2)

    driver.elementClick(toggleContactMe)
    time.sleep(2)
    driver.waitOnElement(firstName)
    driver.enterValues(firstName, 'test')
    time.sleep(2)
    driver.waitOnElement(lastName)
    driver.enterValues(lastName, 'test')
    time.sleep(2)
    driver.waitOnElement(phone)
    driver.enterValues(phone,'1234567890')
    time.sleep(2)
    driver.waitOnElement(Next)
    driver.elementClick(Next)


@then("I am taken to the “Nominate This Nurse” screen")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(gratitudeTextarea,'test')
    time.sleep(2)
    driver.waitOnElement(Next)
    driver.elementClick(Next)
    time.sleep(2)

    assert driver.getTextForElement(nominateNursetext) == 'Nominate this nurse', "It is not navigated to Nominate this Nurse screen"
    time.sleep(2)
    driver.waitOnElement(nominate)
    driver.elementClick(nominate)
    time.sleep(2)

@when("I complete all of the prompts for “Nominate This Nurse” screen")
def step_impl(context):
    driver.waitOnElement(fName)
    driver.enterValues(fName,'test')
    time.sleep(2)
    driver.waitOnElement(lName)
    driver.enterValues(lName,'test')
    time.sleep(2)
    driver.waitOnElement(enterPhone)
    driver.enterValues(enterPhone,'1234567890')
    time.sleep(2)
    driver.waitOnElement(enterText)
    driver.enterValues(enterText,'textarea')




@then("I see the Submit button switch from gray to blue")
def step_impl(context):
    time.sleep(2)
    print(driver.getColorForElement(submit))


@step("I can submit my nomination")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(submit)
    driver.elementClick(submit)
    time.sleep(2)



@step("searched for the person I want to recognize")
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
    time.sleep(2)

    driver.enterValues(searchPerson,'Wambi')
    time.sleep(5)
    #driver.pressEnter()
    #time.sleep(5)
