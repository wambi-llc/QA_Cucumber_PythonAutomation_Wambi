from behave import *
from pageElement.patientportalElements import *
from pageElement.wambiplatformElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")
from selenium import webdriver
import re

@step("I have begun the patient portal review process")
def step_impl(context):

    driver.navigate('https://portaldev.wambiapp.com')
    driver.waitOnElement(startReview)
    driver.elementClick(startReview)

@step("I search for and select a location")
def step_impl(context):

    driver.waitOnElement(locationSearch)
    driver.enterValues(locationSearch, "Delta Harbor Health")
    driver.elementClick(firstLocation)
    driver.waitOnElement(locationNext)
    driver.elementClick(locationNext)

@step("I am able to log in using my email")
def step_impl(context):

    driver.waitOnElement(emailInput)
    driver.enterValues(emailInput, "vlad.sharkov@wambi.org")
    driver.elementClick(sendCode)

    driver.driver.execute_script("window.open('');")
    time.sleep(1)
    driver.driver.switch_to.window(driver.driver.window_handles[1])
    driver.navigate('https://portaldev.wambiapp.com/api/utilities/getOTPToken?patientId=282&secret=pineapples')
    time.sleep(1)
    code = re.findall(r"\d+", str(driver.driver.page_source))[1]
    time.sleep(1)
    driver.driver.switch_to.window(driver.driver.window_handles[0])
    driver.waitOnElement(codeInput)
    driver.enterValues(codeInput, "{}".format(code))
    driver.elementClick(termsCheck)
    driver.elementClick(submitCode)

@step("I validate the selected location")
def step_impl(context):

    driver.waitOnElement(openMenu)
    driver.elementClick(openMenu)
    driver.waitOnElement(locationTile)
    if re.match(r"Delta", str(driver.getTextForElement(locationTile))) == None:
       raise ValueError('Expected location not displayed')
    driver.elementClick(closeMenu)

@step("I search and select a specific employee to review")
def step_impl(context):

    driver.waitOnElement(employeeSearch)
    driver.enterValues(employeeSearch, "Jackie C")
    time.sleep(2)
    driver.elementClick(firstEmployee)
    driver.waitOnElement(selectUnit)
    driver.elementClick(selectUnit)
    driver.waitOnElement(firstUnit)
    driver.elementClick(firstUnit)
    driver.waitOnElement(beginReview)
    driver.elementClick(beginReview)

@step("I will be able to answer all the expected questions for the expected employee \(perfect score\)")
def step_impl(context):

    driver.waitOnElement(employeeTile)
    if re.match(r"Jackie C", str(driver.getTextForElement(employeeTile))) == None:
       raise ValueError('Expected username not displayed')
    time.sleep(1)
    if re.match('Provided you with consistent information during your stay',
             str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Explained things in a way you could understand',
             str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Included you in decisions regarding your care in a compassionate manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Treated you with respect and dignity',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Responded to your request in a timely manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()

@step("I will be able to answer all the expected questions for the expected employee \(subpar score\)")
def step_impl(context):

    driver.waitOnElement(employeeTile)
    if re.match(r"Jackie C", str(driver.getTextForElement(employeeTile))) == None:
       raise ValueError('Expected username not displayed')
    time.sleep(1)
    if re.match('Provided you with consistent information during your stay',
             str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[2]/img').click()
    time.sleep(1)
    if re.match('Explained things in a way you could understand',
             str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Included you in decisions regarding your care in a compassionate manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('/html/body/div/main/section/section/div[4]/div[3]/img').click()
    time.sleep(1)
    if re.match('Treated you with respect and dignity',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Responded to your request in a timely manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()

@step("I will be able to give feedback on what could have been done better")
def step_impl(context):
    driver.waitOnElement(betterComment)
    driver.enterValues(betterComment, 'Try doing a Van Damme helicopter kick')

    #This section removed from app?? Leaving it commented out in case it's actually situational in some
    #way I don't udnerstand yet.
    # driver.elementClick(betterSwitch)
    # driver.waitOnElement(betterFirst)
    # driver.enterValues(betterFirst, 'Hrithik')
    # driver.enterValues(betterLast, 'Roshan')
    # driver.enterValues(betterPhone, '1231231234')

    driver.waitOnElement(betterNext)
    driver.elementClick(betterNext)

@step("I will be able to complete a carepostcard")
def step_impl(context):

    driver.waitOnElement(gratitudeInput)
    driver.enterValues(gratitudeInput, "Test Test Test")
    driver.elementClick(gratitudeSubmit)

@step("I will be able to nominate the employee for a Daisy Award")
def step_impl(context):
    driver.waitOnElement(noThanks)
    driver.elementClick(nominateButton)
    driver.waitOnElement(daisyFirst)
    driver.enterValues(daisyFirst, 'Hrithik')
    driver.enterValues(daisyLast, 'Roshan')
    driver.enterValues(daisyPhone, '1231231234')
    driver.enterValues(daisyEmail, 'greekgodhrithik@faketest.com')
    driver.enterValues(daisyComment, ' test test test')
    driver.waitOnElement(daisySubmit)
    driver.elementClick(daisySubmit)

    #end of review
    driver.waitOnElement(nextReview)
    driver.elementClick(nextReview)
    driver.waitOnElement(openMenu)
    time.sleep(1) #wait_until_clickable method would be great
    driver.elementClick(openMenu)
    time.sleep(2)
    driver.driver.find_element_by_xpath('/html/body/div/main/header/div/div[2]/div/div/a[3]').click()
    time.sleep(1)

@step("I will be able to skip the Carepostcard and Daisy Award sections")
def step_impl(context):
    driver.waitOnElement(gratitudeInput)
    driver.elementClick(skipButton)
    driver.waitOnElement(nominateButton)
    driver.elementClick(skipButton)

    #end of review
    driver.waitOnElement(nextReview)
    driver.elementClick(nextReview)
    driver.waitOnElement(openMenu)
    time.sleep(1)  # wait_until_clickable method would be great
    driver.elementClick(openMenu)
    time.sleep(2)
    driver.driver.find_element_by_xpath('/html/body/div/main/header/div/div[2]/div/div/a[3]').click()
    time.sleep(1)
