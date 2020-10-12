from behave import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
import utilities.config as sconfig
import requests
import json
import time
import os
use_step_matcher("re")



@given("I am a patient portal user")
def step_impl(context):
    driver.clear_cookies()
    driver.navigate(sconfig.patientPortalURL)
    time.sleep(2)
    driver.waitOnElement(startReview)
    driver.elementClick(startReview)
    time.sleep(4)



@step("have searched for a location Or scrolled to find my desired location")
def step_impl(context):
    #driver.clearElement(searchLoc)
    driver.waitOnElement(previewLocation)
    #driver.elementClick(previewLocation)
    time.sleep(2)



@when("I tap on the location tile")
def step_impl(context):
    print(driver.getTextForElement(previewLocation))
    #driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)


@then("I am shown a confirmation box")
def step_impl(context):
    global counter
    global verConfBox
    verConfBox = driver.getElements(confBox)
    for counter in range(len(verConfBox)):
        print(verConfBox[counter].text)
    assert "NEXT" in verConfBox[counter].text, "confirmation Box is not displaying correctly"


@step("the box contains the image, name, and address")
def step_impl(context):
    assert "Arbor Longterm Care" in verConfBox[counter].text, " Name is not displaying correctly"
    assert "Indianapolis, IN" in verConfBox[counter].text, "Address is not displaying correctly"


@step("an X button")
def step_impl(context):
    driver.pressTab()
    driver.pressEnter()


@step("a Next button")
def step_impl(context):
    assert "NEXT" in verConfBox[counter].text, "Next button is not displaying correctly"
    time.sleep(2)


@step("have previewed a location")
def step_impl(context):
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)


@when("I click the X button and then the confirmation box closes")
def step_impl(context):
    driver.pressTab()
    driver.pressEnter()



@step("I can resume my search for a location")
def step_impl(context):
    assert driver.getCurrentURL() == sconfig.patientPortalLocation, "Location URL is not pointing correctly"


@step("select another location")
def step_impl(context):
    driver.clearElement(searchLoc)
    driver.enterValues(searchLoc, "Seattle")
    driver.pressEnter()







@given("I am a patient portal user and have not authenticated")
def step_impl(context):
    driver.clear_cookies()
    driver.navigate(sconfig.patientPortalURL)
    time.sleep(2)
    driver.waitOnElement(startReview)
    driver.elementClick(startReview)
    time.sleep(2)

@when("I click the Next button")
def step_impl(context):
    driver.pressTab()
    driver.pressTab()
    driver.pressEnter()


@then("I am taken to the Patient Portal Login page")
def step_impl(context):
    time.sleep(4)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == sconfig.patientPortalLoginpage, "It is not pointing to Patent Portal Login page"
    driver.pressTab()
    time.sleep(1)
    driver.pressTab()
    time.sleep(1)
    driver.pressTab()
    time.sleep(1)
    driver.pressTab()
    time.sleep(1)
    driver.pressTab()
    driver.pressEnter()



@step("I have previewed a location")
def step_impl(context):
    time.sleep(2)
    #driver.pressTab()
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)


@step("I previewed a location")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(previewLocation1)
    driver.elementClick(previewLocation1)


@then("I am taken to the Team member search")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(emailInput,'cpcstaging@gmail.com')
    time.sleep(5)
    driver.waitOnElement(Submit)
    driver.elementClick(Submit)
    time.sleep(5)
    # Get OTP
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
        print(getOTP)
        print(patientId)
    driver.enterValues(enterOTP,getOTP)
    time.sleep(2)
    driver.waitOnElement(chkTerms)
    driver.elementClick(chkTerms)
    time.sleep(2)
    driver.waitOnElement(submitbtn)
    driver.elementClick(submitbtn)
    driver.pressTab()
    driver.pressEnter()
    time.sleep(2)
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "It is not pointing to Team Member Search"