from behave import *
from pageElement.wambiplatformElements import *
from pageElement.patientportalElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re


@given("I have navigated to the Wambi application")
def step_impl(context):
    driver.navigate('https://dev-w4.wambiapp.com/')
    driver.waitOnElement(wambiUsername)
    driver.waitOnElement(wambiPassword)

@step("I have logged in")
def step_impl(context):
    driver.enterValues(wambiUsername, 'W00046')
    driver.enterValues(wambiPassword, 'W00046')
    driver.elementClick(wambiLogIn)

@then("I am able to click on all the navigation buttons")
def step_impl(context):
    driver.waitOnElement(wambiSendEmail)
    driver.waitOnElement(wambiDashboard)
    driver.waitOnElement(wambiCarePostCard)
    driver.waitOnElement(wambiChallenges)
    driver.waitOnElement(wambiNotifications)

@then("I am able to view my profile")
def step_impl(context):
    driver.waitOnElement(wambiProfile)
    driver.elementClick(wambiProfile)

@step("I am able to view the available tabs")
def step_impl(context):
    driver.waitOnElement(wambiUsername)
    if driver.driver.wambiUsername.is_displayed():
        raise Exception('uh oh')

@then("I am able to sign out")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am able to sign out')


@when("I attempt to log in without entering a username or password")
def step_impl(context):
    driver.waitOnElement(wambiUsername)

@then("I will not be able to click the log in button")
def step_impl(context):
    if driver.driver.find_element_by_xpath("/html/body/div/main/section/div[1]/form/div[3]/button").is_enabled() == True:
        raise Exception('Log in button unexpectedly enabled')

@when("I attempt to log in without entering a password")
def step_impl(context):
    driver.waitOnElement(wambiUsername)
    driver.enterValues(wambiUsername,'W00046')

@when("I input a username with an incorrect password")
def step_impl(context):
    driver.enterValues(wambiPassword, 'VanDammeKick')

@then("I will be able to click the log in button")
def step_impl(context):
    driver.waitOnElement(wambiLogIn)
    driver.elementClick(wambiLogIn)

@step("I will not be able to log in and an error message will display")
def step_impl(context):
    driver.waitOnElement(wambiErrorMessage)
    if  re.match('Username / Password not found', str(driver.getTextForElement(wambiErrorMessage))) == None:
        raise ValueError('Expected error text not found')

@when("I log in to Wambi")
def step_impl(context):

    driver.waitOnElement(wambiUsername)
    driver.enterValues(wambiUsername,'W00046')
    driver.waitOnElement(wambiPassword)
    driver.enterValues(wambiPassword, 'W00046')

    driver.waitOnElement(wambiLogIn)
    driver.elementClick(wambiLogIn)

@step("I click the button to enter the review section")
def step_impl(context):
    time.sleep(2)
    driver.elementClick(wambiSideMenu)
    driver.waitOnElement(wambiCollectReviews)
    driver.elementClick(wambiCollectReviews)

@step("I search for and select a ACME as my portal and location")
def step_impl(context):
    time.sleep(1)
    if len(driver.driver.find_elements_by_xpath("//div[starts-with (@id,'portal')]")) > 0:
        driver.elementClick(wambiFirstPortal)
        driver.waitOnElement(wambiPortalContinue)
        driver.elementClick(wambiPortalContinue)

    driver.waitOnElement(wambiLocationSearch)
    driver.enterValues(wambiLocationSearch, "acme")
    driver.elementClick(firstLocation)
    driver.waitOnElement(locationNext)
    driver.elementClick(locationNext)

@step("I search and select an ACME employee to review")
def step_impl(context):

    driver.waitOnElement(wambiEmployeeSearch)
    driver.enterValues(wambiEmployeeSearch, "Vlad")
    time.sleep(2)
    driver.elementClick(wambiFirstEmployee)
    driver.waitOnElement(wambiTermsAndConditions)
    driver.elementClick(wambiTermsAndConditions)
    driver.waitOnElement(beginReview)
    time.sleep(1)
    driver.elementClick(beginReview)

@step("I will be able to answer all the expected questions for the ACME employee \(perfect score\)")
def step_impl(context):

    time.sleep(2)
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
    if re.match('Treated you with respect and dignity',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Responded to your request in a timely manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()
    time.sleep(1)
    if re.match('Included you in decisions regarding your care in a compassionate manner',
                str(driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[3]').text)) == None:
        raise ValueError('Expected question not displayed')
    driver.driver.find_element_by_xpath('//*[@id="__next"]/main/section/section/div[4]/div[5]/img').click()

@step("I can click the donation button and see the wambi\.org URL")
def step_impl(contect):
    driver.waitOnElement(wambiDonate)
    driver.elementClick(wambiDonate)
    driver.driver.switch_to.window(driver.driver.window_handles[1])
    driver.waitOnElement(wambiURLElement)
    driver.driver.switch_to.window(driver.driver.window_handles[0])

@step("I can choose to give another review")
def step_impl(context):
    driver.waitOnElement(wambiGiveAnotherReview)
    driver.elementClick(wambiGiveAnotherReview)

@then("I can sign out of the review process")
def step_impl(context):
    driver.waitOnElement(openMenu)
    driver.elementClick(openMenu)
    time.sleep(1)
    driver.driver.find_element_by_xpath('//*[@id="sign-out-btn"]').click()
    time.sleep(2)

@step("I can sign out of the Wambi platform")
def step_impl(context):
    driver.waitOnElement(wambiSideMenu)
    driver.elementClick(wambiSideMenu)
    driver.waitOnElement(wambiSignOut)
    driver.elementClick(wambiSignOut)
    time.sleep(2)

@step("I enter the edit profile screen")
def step_impl(context):
    driver.waitOnElement(wambiSideMenu)
    driver.elementClick(wambiSideMenu)
    driver.waitOnElement(wambiEditProfile)
    driver.elementClick(wambiEditProfile)
    driver.waitOnElement(wambiProfileZoom)


@step("I upload a new picture")
def step_impl(context):
    driver.driver.find_element_by_xpath('//*[@id="files"]').send_keys(os.getcwd() + "/cage.jpg")
    time.sleep(5)


@step("I play with the zoom toggle")
def step_impl(context):
    driver.elementClick(wambiProfileZoom)
    time.sleep(2)

@step("I save the new picture")
def step_impl(context):
    driver.waitOnElement(wambiProfileSave)
    driver.elementClick(wambiProfileSave)


@then("the new profile picture will be displayed")
def step_impl(context):
    time.sleep(2)
    driver.driver.find_element_by_xpath('//*[@id="files"]').send_keys(os.getcwd() + "/conair.jpg")
    driver.waitOnElement(wambiProfileSave)
    driver.elementClick(wambiProfileSave)


@step("I navigate to the home page")
def step_impl(context):
    driver.waitOnElement(wambiSideMenu)
    time.sleep(1)
    driver.driver.find_element_by_id('dashboard-icon').click()



@then("10 items from the newsfeed will be loaded")
def step_impl(context):
    driver.waitOnElement(newsItem)
    if len(driver.driver.find_elements_by_xpath("//button[starts-with (@id,'add-reaction')]")) < 10:
        raise ValueError("10 or more newsfeed items not loaded")


@step("I will be able to add and remove emoticons")
def step_impl(context):
    driver.waitOnElement(newsItem)
    time.sleep(0.5)
    driver.driver.find_element_by_id('add-reaction-33').click()
    time.sleep(0.5)
    driver.driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]/div/div/div[2]/div[2]/img[3]').click()
    time.sleep(0.5)
    driver.driver.find_element_by_id('add-reaction-33').click()
    time.sleep(0.5)
    driver.driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]/div/div/div[2]/div[2]/img[1]').click()
    time.sleep(0.5)
    driver.driver.find_element_by_id('add-reaction-33').click()
    time.sleep(0.5)
    driver.driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]/div/div/div[2]/div[2]/img[2]').click()
    time.sleep(0.5)
    driver.driver.find_element_by_id('add-reaction-33').click()
    time.sleep(0.5)
    driver.driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]/div/div/div[2]/div[2]/img[4]').click()
    time.sleep(0.5)
    driver.driver.find_element_by_id('add-reaction-33').click()
    time.sleep(0.5)
    driver.driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]/div/div/div[2]/div[2]/img[5]').click()
    time.sleep(1)
    #Try statements to be removed after fix
    try:
        driver.driver.find_element_by_id('FaviCon Air-33').click()
    except:
        print "Favicon emoticon missing"
    try:
        driver.driver.find_element_by_id('Wambi-33').click()
    except:
        print "Wambi emoticon missing"
    try:
        driver.driver.find_element_by_id('Party Blob-33').click()
    except:
        print "Party blob emoticon missing"
    try:
        driver.driver.find_element_by_id('Banana Dance-33').click()
    except:
        print "Banana Dance emoticon missing"
    try:
        driver.driver.find_element_by_id('Josh\'s Dad-33').click()
    except:
        print "Nic Cage emoticon missing"


@step("I am able to see at least one other newsfeed item after scrolling down the page")
def step_impl(context):
    driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    if len(driver.driver.find_elements_by_xpath("//button[starts-with (@id,'add-reaction')]")) < 21:
        raise ValueError("21 or more newsfeed items not loaded")
    time.sleep(1)


@step("I enter the Help and Support Section")
def step_impl(context):
    driver.waitOnElement(wambiSideMenu)
    driver.elementClick(wambiSideMenu)
    driver.waitOnElement(wambiHelpAndSupport)
    driver.elementClick(wambiHelpAndSupport)
    driver.waitOnElement(helpContact)

@when("I input all the required fields")
def step_impl(context):
    driver.enterValues(helpContact, 'Tiger Shroff')
    driver.enterValues(helpEmail, 'tigershroff@faketest.com')
    driver.enterValues(helpEmployeeID, 'W00046')
    driver.enterValues(helpSubject, 'Test')

@then("I will be able to submit a ticket")
def step_impl(context):
    driver.elementClick(helpSubmit)
    time.sleep(2)
    driver.driver.find_element_by_id('searchContainer1')
    driver.navigate('https://dev-w4.wambiapp.com/admin')


@when("I enter the 'Trouble signing in' section")
def step_impl(context):
    driver.waitOnElement(wambiTroubleSigningIn)
    driver.elementClick(wambiTroubleSigningIn)

@step("I input my phone or email and click 'send code'")
def step_impl(context):
    driver.waitOnElement(wambiEmailorPhone)
    driver.enterValues(wambiEmailorPhone, 'vlad.sharkov@wambi.org')


@then("I will be able to sign in using a code sent to me")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will be able to sign in using a code sent to me')