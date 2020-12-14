from behave import *
from pageElement.myPageElements import *
from pageElement.HomePageElements import *
from selenium.webdriver import *
import utilities.config as sconfig
from utilities.driverUtil import driver
import time
import string
import random
import re

use_step_matcher("re")


@then("I click on My Page Tab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(MyPage)
    driver.elementClick(MyPage)
    time.sleep(2)


@step("I click on Send Peer CarePost Card")
def step_impl(context):
    time.sleep(3)
    driver.waitOnElement(PeerCarePostCard)
    driver.elementClick(PeerCarePostCard)
    time.sleep(2)


@then("I write a random generated phrase in the write message box and validate it's highlighted as error\.")
def step_impl(context):

    Text = ''.join(random.choice(string.ascii_letters) for i in range(10))
    driver.waitOnElement(writeMessage)
    driver.enterValues(writeMessage,Text)
    assert driver.tagAttributes(textAreaElem,'spellcheck') == "true","spell check is not highlighted as  "

