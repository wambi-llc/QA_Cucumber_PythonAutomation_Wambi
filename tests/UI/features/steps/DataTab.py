from behave import *
from utilities.driverUtil import driver
from pageElement.DataElements import *
import utilities.config as sconfig
from selenium.webdriver import *
from allure_behave import *
from allure_pytest import *
import pytest
import time
import os
use_step_matcher("re")



@when("I click on Data Tab")
def step_impl(context):
    time.sleep(20)
    driver.waitOnElement(dataTab)
    driver.elementClick(dataTab)


@step("I click on Detailed Review History under Data Tab")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(DetRevHistory)
    driver.elementClick(DetRevHistory)


@step("I enter a careproviders name in the search field \{Alessandra Smith\} and click search")
def step_impl(context):
    showentries = driver.getSelectedElements(showdropdown)
    showentries.select_by_index(3)
    driver.enterValues(searchText, sconfig.searchwith)
    driver.elementClick(search)

@then("I validate all the returned results are only for the careprovider that was searched")
def step_impl(context):
       time.sleep(2)
       searchData = driver.getTextForElement(searchList)
       ResultList = driver.getElements(searchList)
       for i in range(len(ResultList)):
        assert searchData == sconfig.searchwith,"Returned Results are not matching with CareProvider"
       driver.clear_cookies()

@step("I enter a careprovider's name that doesn't exist\{asfdlkjvixlkcjv\} and click search")
def step_impl(context):
   time.sleep(2)
   driver.enterValues(searchText,'\{asdflkjvixlckjv\}')
   driver.elementClick(search)


@then("I validate no results are returned")
def step_impl(context):
    driver.waitOnElement(searchNoresults)
    assert driver.getTextForElement(searchNoresults) == 'No data available in table', "Search results are not displaying data correctly"

    #driver.closeBrowser()