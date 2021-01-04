from behave import *
from pageElement.patientportalElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")
from selenium import webdriver
import re

@step("I validate language options on the landing page and begin the patient portal review process")
def step_impl(context):

    driver.navigate('https://portaldev.wambiapp.com')
    driver.waitOnElement(startReview)
    if re.match('Moments', str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/span').text)) == None:
        raise ValueError('Expected English text not displayed')
    driver.elementClick(landingLanguage)
    time.sleep(1)
    if re.match('Los momentos', str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/span').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(startReview)

@step("I validate language options before searching for selecting a location")
def step_impl(context):

    driver.waitOnElement(languageSelect)
    driver.waitOnElement(locationSearch)
    if re.match('Reconoce', str(driver.driver.find_element_by_xpath('// *[ @ id = "__next"] / main / section / div[1] / span').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(languageSelect)
    time.sleep(1)
    if re.match('Recognize', str(driver.driver.find_element_by_xpath('// *[ @ id = "__next"] / main / section / div[1] / span').text)) == None:
        raise ValueError('Expected English text not displayed')
    driver.elementClick(languageSelect)
    time.sleep(1)
    if re.match('Reconoce', str(driver.driver.find_element_by_xpath('// *[ @ id = "__next"] / main / section / div[1] / span').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.enterValues(locationSearch, "Delta Harbor Health")
    driver.elementClick(firstLocation)
    driver.waitOnElement(locationNext)
    driver.elementClick(locationNext)

@step("I validate language before logging in using my email")
def step_impl(context):

    driver.waitOnElement(emailInput)
    if re.match('Reconoce', str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/div/span').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
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

@step("I validate language options in the side bar")
def step_impl(context):

    driver.waitOnElement(openMenu)
    driver.elementClick(openMenu)
    driver.waitOnElement(locationTile)
    if re.match('Ayuda', str(driver.driver.find_element_by_xpath(
            '//*[@id="help-btn"]').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(sideLanguage)
    time.sleep(1)
    if re.match('Help', str(driver.driver.find_element_by_xpath(
            '//*[@id="help-btn"]').text)) == None:
        raise ValueError('Expected English text not displayed')
    driver.elementClick(sideLanguage)
    time.sleep(1)
    if re.match('Ayuda', str(driver.driver.find_element_by_xpath(
            '//*[@id="help-btn"]').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(closeMenu)

@step("I validate language options on employee search before beginning a review")
def step_impl(context):

    driver.waitOnElement(employeeSearch)
    driver.waitOnElement(languageSelect)
    time.sleep(1)

# Spanish text breaking matcher in this section. Needs fixing.

    # if re.match('A qui', (driver.driver.find_element_by_xpath(
    #         '//*[@id="__next"]/main/section/div[1]/span').text)) == None:
    #     raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(languageSelect)
    time.sleep(1)
    if re.match('Who would', str(driver.driver.find_element_by_xpath(
            '//*[@id="__next"]/main/section/div[1]/span').text)) == None:
        raise ValueError('Expected English text not displayed')
    driver.elementClick(languageSelect)
    time.sleep(1)
    # if re.match('A qui', (driver.driver.find_element_by_xpath(
    #         '//*[@id="__next"]/main/section/div[1]/span').text)) == None:
    #     raise ValueError('Expected Spanish text not displayed')
    driver.enterValues(employeeSearch, "Jackie C")
    time.sleep(2)
    driver.elementClick(firstEmployee)
    driver.waitOnElement(selectUnit)
    driver.elementClick(selectUnit)
    driver.waitOnElement(firstUnit)
    driver.elementClick(firstUnit)
    driver.waitOnElement(beginReview)
    driver.elementClick(beginReview)

@step("I validate expected questions are displayed in Spanish throughout review process")
def step_impl(context):

    driver.waitOnElement(employeeTile)
    if re.match(r"Jackie C", str(driver.getTextForElement(employeeTile))) == None:
       raise ValueError('Expected username not displayed')
    time.sleep(1)
    if re.match('Le brin',
             (driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]/p[1]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Le expli',
                (driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    # question validation missing
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    # question validation missing
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Respond',
                (driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)

@step("I validate language on the Carepostcard and Daisy Award sections")
def step_impl(context):
    driver.waitOnElement(gratitudeInput)
    if re.match('Comparte', (driver.driver.find_element_by_xpath('// *[ @ id = "__next"] / main / section / section / div').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(skipButton)
    driver.waitOnElement(nominateButton)
    if re.match('Nominar', (driver.driver.find_element_by_xpath('// *[ @ id = "__next"] / main / section / section / div').text)) == None:
        raise ValueError('Expected Spanish text not displayed')
    driver.elementClick(skipButton)

    #end of review
    driver.waitOnElement(nextReview)
    driver.elementClick(nextReview)
    time.sleep(2)