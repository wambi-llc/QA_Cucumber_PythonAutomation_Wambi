from behave import *
from selenium import webdriver
from pageElement.loginpageFeatureElements import *
from utilities.driverUtil import *


use_step_matcher("re")

@then('I validate attribute for username and password FORM page is set to "autocomplete=off"')
def step_impl(context):
        frmattribute = driver.tagAttributes(AutoCompleteattr,'autocomplete')
        print('attribute for autocomplete set to', frmattribute)
        assert frmattribute == "off", "Username and Password Form not set to automcomplete as off"

        driver.closeBrowser()