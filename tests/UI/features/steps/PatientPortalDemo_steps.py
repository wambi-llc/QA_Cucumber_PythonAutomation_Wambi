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

@step("Full Demo Step")
def step_impl(context):

    driver.navigate('https://portaldev.wambiapp.com')
    driver.waitOnElement(startReview)
    driver.elementClick(startReview)
    driver.waitOnElement(locationSearch)
    driver.enterValues(locationSearch, "Delta Harbor Health")
    driver.elementClick(firstLocation)
    driver.waitOnElement(locationNext)
    driver.elementClick(locationNext)
    driver.waitOnElement(emailInput)
    driver.enterValues(emailInput, "vlad.sharkov@wambi.org")
    driver.elementClick(sendCode)

    time.sleep(3)
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
    time.sleep(3)
    driver.elementClick(termsCheck)
    driver.elementClick(submitCode)

    driver.waitOnElement(openMenu)
    driver.elementClick(openMenu)
    driver.waitOnElement(locationTile)
    if re.match(r"Delta", str(driver.getTextForElement(locationTile))) == None:
       raise ValueError('Expected location not displayed')
    time.sleep(3)
    driver.elementClick(closeMenu)
    driver.waitOnElement(employeeSearch)
    driver.enterValues(employeeSearch, "Jackie C")
    time.sleep(2)
    driver.elementClick(firstEmployee)
    time.sleep(1)
    driver.waitOnElement(selectUnit)
    driver.elementClick(selectUnit)
    driver.waitOnElement(firstUnit)
    driver.elementClick(firstUnit)
    time.sleep(2)
    driver.waitOnElement(beginReview)
    driver.elementClick(beginReview)
    driver.waitOnElement(employeeTile)
    time.sleep(5)
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
    driver.waitOnElement(gratitudeInput)
    time.sleep(1)
    driver.enterValues(gratitudeInput, "Test Test Test")
    time.sleep(3)
    driver.elementClick(gratitudeSubmit)
    driver.waitOnElement(noThanks)
    driver.elementClick(noThanks)
    driver.waitOnElement(nextReview)
    driver.elementClick(nextReview)
    time.sleep(2)



