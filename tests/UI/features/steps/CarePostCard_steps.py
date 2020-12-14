from behave import *
from pageElement.carepostcardElements import *
import utilities.config as sconfig
from utilities.driverUtil import driver
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
use_step_matcher("re")
from selenium import webdriver

driver.clear_cookies()

@given("I navigate to the Carepostcard application")
def step_impl(context):
    driver.navigate(sconfig.careurl)

@step("I sign in as an admin")
def step_impl(context):

    driver.waitOnElement(signInButton)
    driver.elementClick(signInButton)

    driver.waitOnElement(emailInput)
    driver.elementClick(emailInput)
    driver.enterValues(emailInput, 'cpcstagingadm@gmail.com')
    driver.elementClick(sendEmailButton)

@step("I sign in as a regular user")
def step_impl(context):

    driver.waitOnElement(signInButton)
    driver.elementClick(signInButton)

    driver.waitOnElement(emailInput)
    driver.elementClick(emailInput)
    driver.enterValues(emailInput, 'cpcstaging@gmail.com')
    driver.elementClick(sendEmailButton)
    driver.waitOnElement(postButton)

@then("I am directed to create a new account")
def step_impl(context):
    driver.waitOnElement(createNewUserName)
    driver.waitOnElement(createNewEmail)

@then("I create a new user")
def step_impl(context):
    driver.waitOnElement(createNewUserName)
    driver.waitOnElement(createNewEmail)
    random_user_num = randint(1000, 9999)
    driver.elementClick(createNewUserName)
    driver.enterValues(createNewUserName, "Test {}".format(random_user_num))
    random_user_num = randint(1000, 9999)
    driver.elementClick(createNewEmail)
    driver.enterValues(createNewEmail, "Test{}@faketest.com".format(random_user_num))
    driver.waitOnElement(joinNowButton)
    driver.elementClick(joinNowButton)

@step("I create a Carepostcard before signing in")
def step_impl(context):
    driver.waitOnElement(createCardButton)
    driver.elementClick(createCardButton)
    #load validations
    driver.waitOnElement(addressedTo)
    driver.waitOnElement(cardBody)
    driver.waitOnElement(cardLocation)
    driver.waitOnElement(disabledCreateCard)
    #Carepostcard creation
    global random_addressee_num
    random_addressee_num = randint(1000, 9999)
    driver.elementClick(addressedTo)
    driver.enterValues(addressedTo, "Test {}".format(random_addressee_num))
    driver.elementClick(cardBody)
    global random_body_num
    random_body_num = randint(1000, 9999)
    driver.enterValues(cardBody, "{}".format(random_body_num))
    driver.elementClick(cardLocation)
    driver.waitOnElement(cardLocationSearch)
    driver.enterValues(cardLocationSearch, 'Columbus ALZ')
    driver.elementClick(locationSelection)
    driver.waitOnElement(createCard)
    driver.elementClick(createCard)

@when("I create a Carepostcard")
def step_impl(context):
    driver.waitOnElement(postButton)
    driver.elementClick(postButton)
    #load validations
    driver.waitOnElement(addressedTo)
    driver.waitOnElement(cardBody)
    driver.waitOnElement(cardLocation)
    driver.waitOnElement(disabledCreateCard)
    #Carepostcard creation
    global random_addressee_num
    random_addressee_num = randint(1000, 9999)
    driver.elementClick(addressedTo)
    driver.enterValues(addressedTo, "Test {}".format(random_addressee_num))
    driver.elementClick(cardBody)
    global random_body_num
    random_body_num = randint(1000, 9999)
    driver.enterValues(cardBody, "{}".format(random_body_num))
    driver.elementClick(cardLocation)
    driver.waitOnElement(cardLocationSearch)
    driver.enterValues(cardLocationSearch, 'Columbus ALZ')
    driver.elementClick(locationSelection)
    driver.waitOnElement(createCard)
    driver.elementClick(createCard)
    time.sleep(5)
    driver.waitOnElement(firstCard)

@when("I create a Carepostcard with a unique hashtag")
def step_impl(context):
    driver.waitOnElement(postButton)
    driver.elementClick(postButton)
    #load validations
    driver.waitOnElement(addressedTo)
    driver.waitOnElement(cardBody)
    driver.waitOnElement(cardLocation)
    driver.waitOnElement(disabledCreateCard)
    #Carepostcard creation
    global random_addressee_num
    random_addressee_num = randint(1000, 9999)
    driver.elementClick(addressedTo)
    driver.enterValues(addressedTo, "Test {}".format(random_addressee_num))
    driver.elementClick(cardBody)
    global random_hashtag
    random_hashtag = "#ahash{}".format(randint(1000, 9999))
    driver.enterValues(cardBody, "check out my hashtag {}".format(random_hashtag))
    driver.elementClick(cardLocation)
    driver.waitOnElement(cardLocationSearch)
    driver.enterValues(cardLocationSearch, 'Columbus ALZ')
    driver.elementClick(locationSelection)
    driver.waitOnElement(createCard)
    driver.elementClick(createCard)
    time.sleep(5)
    driver.waitOnElement(firstCard)

@step("I click on my last created Carepostcard")
def step_impl(context):
    driver.waitOnElement(firstCard)
    driver.elementClick(firstCard)

@then("the expected Carepostcard data will be present")
def step_impl(context):
    #validating that expected addressee and body text persist from creation
    driver.waitOnElement(cardReviewAddressedTo)
    addressed_to_text = driver.getTextForElement(cardReviewAddressedTo)
    if str(addressed_to_text) != "To: Test {}".format(random_addressee_num):
        raise ValueError('Addressed to line does not contain expected text')
    driver.waitOnElement(cardReviewBody)
    body_text = driver.getTextForElement(cardReviewBody)
    if str(body_text) != str(random_body_num):
        raise ValueError('Body does not contain expected text')
    driver.waitFor(5)

@step("I navigate to the admin panel")
def step_impl(context):
    time.sleep(3)
    driver.navigate('https://stage.carepostcard.com/admin')

@when("I edit the body text of a Carepostcard")
def step_impl(context):
    driver.waitOnElement(adminCardBody)
    driver.elementClick(adminCardBody)
    global random_edit_num
    random_edit_num = randint(1000, 9999)
    driver.enterValues(cardBody, " #TestHash{}".format(random_edit_num))
    driver.waitOnElement(adminUpdate)
    driver.elementClick(adminUpdate)
    time.sleep(3)

@step("reload the admin page")
def step_impl(context):
    driver.navigate('https://stage.carepostcard.com/admin/')

@then("the edited text should persist")
def step_impl(context):
    driver.waitOnElement(adminCardBody)
    edited_text = driver.getTextForElement(adminCardBody)
    if str(edited_text) != "{}".format(random_body_num) + " #TestHash{}".format(random_edit_num):
        raise ValueError('Edited card body does not contain expected text')

@when("I hide the most recently created Carepostcard")
def step_impl(context):
    driver.waitOnElement(adminCardBody)
    driver.waitOnElement(adminHide)
    driver.elementClick(adminHide)
    time.sleep(2)

@then("the expected Carepostcard should remain hidden")
def step_impl(context):
    driver.waitOnElement(adminCardBody)
    first_card_text = driver.getTextForElement(adminCardBody)
    if str(first_card_text) == "{}".format(random_body_num):
        raise ValueError('Carepostcard not hidden')


@when("I feature the most recently created Carepostcard")
def step_impl(context):
    time.sleep(3)
    driver.waitOnElement(adminCardBody)
    driver.waitOnElement(adminFeature)
    driver.elementClick(adminFeature)
    driver.waitOnElement(adminUnfeature)

@step("return to the home page")
def step_impl(context):
    driver.waitOnElement(homeLink)
    driver.elementClick(homeLink)

@then("the expected Carepostcard should be featured")
def step_impl(context):
    driver.waitOnElement(featuredCardBody)
    featured_text = driver.getTextForElement(featuredCardBody)
    if str(featured_text) != str(random_body_num):
        raise ValueError('Expected card not first featured')
    driver.waitFor(5)

@then("I am re-directed to the home page")
def step_impl(context):
    driver.waitOnElement(liveFeedImage)

@when("I navigate to the manage hashtags section")
def step_impl(context):
    time.sleep(3)
    driver.navigate('https://stage.carepostcard.com/admin/manage-hashtags/')

@step("I validate that the unique hashtag is visible")
def step_impl(context):
    time.sleep(3)
    if ("{}".format(random_hashtag) in driver.driver.page_source) != True:
        raise ValueError('hashtag missing')

@then("I will be redirected to the Twitter site")
def step_impl(context):
    time.sleep(4)
    driver.driver.switch_to_window(driver.driver.window_handles[1])
    current_url = driver.driver.current_url
    if current_url.startswith('https://twitter.com/intent/tweet?url=https://api.carepostcard.com/'):
        pass
    else:
        raise ValueError('Not on Twitter')

@step("I click the Twitter link")
def step_impl(context):
    driver.waitOnElement(twitterButton)
    driver.elementClick(twitterButton)
    time.sleep(5)


