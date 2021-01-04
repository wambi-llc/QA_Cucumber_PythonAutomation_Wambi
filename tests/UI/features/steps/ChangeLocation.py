from behave import *
from utilities.driverUtil import driver
from pageElement.SelectConfirmationLocationPageElements import *
from pageElement.changLocationPageElements import *
from pageElement.RefineSearchbyJobTypePageElements import *
import utilities.config as sconfig
import requests
import json
import time
import os
use_step_matcher("re")


@step("have selected my location and have authenticated")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)
    driver.pressTab()
    driver.pressTab()
    driver.pressEnter()
    time.sleep(2)
    driver.enterValues(emailInput, 'cpcstaging@gmail.com')
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
    driver.enterValues(enterOTP, getOTP)
    time.sleep(2)
    driver.waitOnElement(chkTerms)
    driver.elementClick(chkTerms)
    time.sleep(2)
    driver.waitOnElement(submitbtn)
    driver.elementClick(submitbtn)
    #driver.pressEnter()
    time.sleep(2)
    assert driver.getCurrentURL() == sconfig.teamMemberSearch, "It is not pointing to Team Member Search"


@when("I tap the Hamburger menu")
def step_impl(context):
    time.sleep(3)
    driver.waitOnElement(portalMenu)
    driver.elementClick(portalMenu)
    time.sleep(2)



@then("a menu opens up")
def step_impl(context):
    global counter
    global hamBurgerMenu
    hamBurgerMenu = driver.getElements(hamburgerMenuitems)
    for counter in range(len(hamBurgerMenu)):
     print(hamBurgerMenu[counter].text)
     assert "Help" in hamBurgerMenu[counter].text, "Hamburger Menu is not displaying correctly"


@step("I can see my current selected location")
def step_impl(context):
    assert "Arbor Longterm Care" in hamBurgerMenu[counter].text, "Selected current location is not displaying correctly"


@step("I can tap to change my location")
def step_impl(context):
    assert "CHANGE LOCATION" in hamBurgerMenu[counter].text, "Unable to tap the CHANGE LOCATION"
    #print(hamBurgerMenu[0].text)
    time.sleep(2)
    driver.waitOnElement(changeLocation)
    driver.elementClick(changeLocation)
    time.sleep(2)
    changeLoc = driver.getTextForElement(changedLocationTo)
    driver.waitOnElement(changedLocationTo)
    driver.elementClick(changedLocationTo)
    time.sleep(2)
    driver.waitOnElement(NEXT)
    driver.elementClick(NEXT)
    time.sleep(2)
    print(changeLoc)
    assert changeLoc == 'UHA Healthcare',"Changed Location is not displaying correctly"


@step("have selected my location")
def step_impl(context):
    time.sleep(4)
    driver.waitOnElement(previewLocation)
    driver.elementClick(previewLocation)
    time.sleep(2)
    driver.waitOnElement(NEXT)
    driver.elementClick(NEXT)
    time.sleep(5)
    driver.waitOnElement(Back)
    driver.elementClick(Back)


@when("I tap to change my location")
def step_impl(context):
   time.sleep(2)
   driver.waitOnElement(portalMenu)
   driver.elementClick(portalMenu)
   time.sleep(2)
   driver.waitOnElement(changeLocation)
   driver.elementClick(changeLocation)
   time.sleep(2)
   driver.waitOnElement(changedLocationTo)
   driver.elementClick(changedLocationTo)
   time.sleep(2)
   driver.waitOnElement(NEXT)
   driver.elementClick(NEXT)
   time.sleep(2)
   driver.waitOnElement(Back)
   driver.elementClick(Back)


@then("I am taken to the Location Search page")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == sconfig.patientPortalLocation, "It is not pointing to Location Search Page"


@step("can change my location without re-authenticating")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(portalMenu)
    driver.elementClick(portalMenu)
    time.sleep(2)
    print(driver.getTextForElement(changedLocationTo))
    assert driver.getTextForElement(changedLocationTo) == "UHA Healthcare", "Location has not changed correctly"

@then("I signout from PortalUser")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(portalMenu)
    driver.elementClick(portalMenu)
    time.sleep(4)
    driver.waitOnElement(signOut)
    driver.elementClick(signOut)
    driver.clear_cookies()