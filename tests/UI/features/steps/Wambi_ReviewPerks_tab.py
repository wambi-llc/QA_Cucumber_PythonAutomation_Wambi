from behave import *
from pageElement.HomePageElements import *
from pageElement.PerksTabPageElements import *
from utilities.driverUtil import driver
import utilities.config as sconfig
import time
import os
import string
import random

use_step_matcher("re")


@step("I click on Perks tab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(Perks)
    driver.elementClick(Perks)


@then("I validate that available gift cards, Post Perk and PerkAlert email buttons are displayed")
def step_impl(context):
    time.sleep(2)
    assert driver.getTextForElement(postPerkbutton) == 'Post Perk', "Post Perk button is not displaying in Perks tab detail page"
    assert driver.getTextForElement(perkalertemailbutton) == 'Perk Alert Email', "Perk Alert Email button is not displaying in Perk Alert Email tab detail page"
    assert "Lunch with the CEO" in driver.getTextForElement(giftCards), "gift cards details are not available in Perks tab detail page"


@step("I click on PostPerk button")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(postPerkbutton)
    driver.elementClick(postPerkbutton)


@then("I validate add reward page displays")
def step_impl(context):
    time.sleep(2)
    print(driver.getCurrentURL())
    assert driver.getCurrentURL() == 'https://dev.wambiapp.com/admin/reward/add', "reward page is not displaying correctly"
    time.sleep(2)
    driver.waitOnElement(Perks)
    driver.elementClick(Perks)
    time.sleep(2)


@step("I click on PERK Alert email button")
def step_impl(context):
    driver.waitOnElement(perkalertemailbutton)
    driver.elementClick(perkalertemailbutton)
    time.sleep(2)


@then("I validate PERK Alert email page displays")
def step_impl(context):
    assert driver.getCurrentURL() == 'https://dev.wambiapp.com/admin/reward/perk-alert-email',"Perk Alert email page is not displaying correctly"
    time.sleep(2)
    driver.waitOnElement(Perks)
    driver.elementClick(Perks)


@step("I check the Edit and Delete icon present on any available gift cards")
def step_impl(context):
    time.sleep(2)
    assert driver.getElements(editIcon) is not None, "Edit Icon is not present in gift cards"
    assert driver.getElements(deleteIcon) is not None, "Delete Icon is not present in gift cards"
    time.sleep(2)

@step("I click on Edit button in gift card")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(editIcon)
    driver.elementClick(editIcon)


@then("I validate the gift cards can be edited")
def step_impl(context):
    time.sleep(2)
    assert driver.getCurrentURL() == 'https://dev.wambiapp.com/admin/reward/edit/7', "gift cards cannot be edited"
    time.sleep(2)
    driver.waitOnElement(Perks)
    driver.elementClick(Perks)


@step("I click on delete button")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(deleteIcon)
    driver.elementClick(deleteIcon)
    time.sleep(2)


@then("I validate popup message displays with Cancel and Yes,delete it options")
def step_impl(context):
    assert driver.getTextForElement(cancelButton) == 'Cancel', "Cancel button is not displaying in popup message"
    time.sleep(2)
    assert 'delete' in driver.getTextForElement(deleteButton), "Delete button is not displaying in popup message"
    time.sleep(2)
    driver.waitOnElement(cancelButton)
    driver.elementClick(cancelButton)


@step("I hover on Perks tab")
def step_impl(context):
    time.sleep(2)
    driver.moveToElement(Perks)


@step("I click on Perk History subtab")
def step_impl(context):
    time.sleep(2)
    driver.waitOnElement(perksHistory)
    driver.elementClick(perksHistory)


@step("I enter a valid text in search field and click on search button")
def step_impl(context):
    time.sleep(2)
    driver.enterValues(searchtext,sconfig.perksearchText)
    time.sleep(4)
    driver.waitOnElement(searchbtn)
    driver.elementClick(searchbtn)


@then("I validate the results  displayed as per the valid search data")
def step_impl(context):
    time.sleep(2)
    assert driver.getTextForElement(verSearchres) == sconfig.perksearchText, "The search results are not displaying correctly"
