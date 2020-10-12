from behave import *
from pageElement.loginPageElements import *
from pageElement.HomePageElements import *
from selenium.webdriver import *
import utilities.config as sconfig
from utilities.driverUtil import driver
import time
import string
import calendar
import datetime
import re

use_step_matcher("re")


@step("I enter username and password and click Login to login as SA User")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(userNameLoginPage)
    driver.elementClick(userNameLoginPage)
    driver.enterValues(userNameLoginPage, sconfig.usrnameSA)
    driver.elementClick(passwordLoginPage)
    driver.enterValues(passwordLoginPage, sconfig.pword)
    driver.elementClick(submitButtonLoginPage)

@then("I click on Home Tab")
def step_impl(context):
    #time.sleep(10)
    #driver.waitOnElement(lineIcon)
    #driver.elementClick(lineIcon)
    time.sleep(10)
    #driver.waitOnElement(HomePage)
    #driver.elementClick(HomePage)



@then("I validate at the bottom of the chart I see all 4 options \(Weekly, Monthly, Quarterly, Yearly\)")
def step_impl(context):
    assert 'Weekly' == driver.getTextForElement(Weekly),"Weekly Option is not displayed"
    assert 'Monthly' == driver.getTextForElement(Monthly),"Monthly Option is not displayed"
    assert 'Quarterly' == driver.getTextForElement(Quarterly),"Quarterly option is not displayed"
    assert 'Yearly' == driver.getTextForElement(Yearly),"Yearly option is not displayed"


@step("I click on Weekly option at the bottom of the home chart")
def step_impl(context):
     time.sleep(10)
     driver.waitOnElement(Weekly)
     driver.elementClick(Weekly)

@then("I validate at the bottom of the chart I see the time on X Axis in Weekly increments")
def step_impl(context):
    time.sleep(10)
    weeklydata1 = driver.getTextForElement(Week1)
    weeklydata2 = driver.getTextForElement(Week2)
    weeklydata3 = driver.getTextForElement(Week3)
    weeklydata4 = driver.getTextForElement(Week4)
    weeklydata5 = driver.getTextForElement(Week5)
    weeklydata6 = driver.getTextForElement(Week6)
    weeklydata7 = driver.getTextForElement(Week7)

    wklylist1 = re.findall(r'\d+', weeklydata1)
    wklylist2 = re.findall(r'\d+', weeklydata2)
    wklylist3 = re.findall(r'\d+', weeklydata3)
    wklylist4 = re.findall(r'\d+', weeklydata4)
    wklylist5 = re.findall(r'\d+', weeklydata5)
    wklylist6 = re.findall(r'\d+', weeklydata6)
    wklylist7 = re.findall(r'\d+', weeklydata7)
    #wkdays1 = ' '
    wkdays1 = list(map(int,wklylist1))
    wkdays2 = list(map(int,wklylist2))
    wkdays3 = list(map(int,wklylist3))
    wkdays4 = list(map(int,wklylist4))
    wkdays5 = list(map(int,wklylist5))
    wkdays6 = list(map(int,wklylist6))
    wkdays7 = list(map(int,wklylist7))
    assert wkdays1[1]-wkdays1[0] == 6 or wkdays2[1]-wkdays2[0] == 6 or wkdays3[1]-wkdays3[0] == 6 or wkdays4[1]-wkdays4[0] == 6 or wkdays5[1]-wkdays5[0] == 6 or wkdays6[1]-wkdays6[0] == 6 or wkdays7[1]-wkdays7[0] == 6, "Weeks are not incremented by 1 at a time"


@step("I click on Monthly option at the bottom of the home chart")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(Monthly)
    driver.elementClick(Monthly)
    time.sleep(10)


@then("I validate at the bottom of the chart I see the time on X Axis in Monthly increments")
def step_impl(context):
    ValidateMonths = driver.getTextForElement(Increments)
    assert len(ValidateMonths)!=0,"Months are not displaying on X Axis"
    time.sleep(10)

@then("I also validate the months are incrementing by 1 month at a time")
def step_impl(context):
    month_x1 = driver.getTextForElement(Monthx1)
    month1 = datetime.datetime.strptime(month_x1,'%b %Y').month
    month_x2 = driver.getTextForElement(Monthx2)
    month2 = datetime.datetime.strptime(month_x2,'%b %Y').month
    month_x3 = driver.getTextForElement(Monthx3)
    month3 = datetime.datetime.strptime(month_x3, '%b %Y').month
    month_x4 = driver.getTextForElement(Monthx4)
    month4 = datetime.datetime.strptime(month_x4, '%b %Y').month
    month_x5 = driver.getTextForElement(Monthx5)
    month5 = datetime.datetime.strptime(month_x5,'%b %Y').month
    month_x6 = driver.getTextForElement(Monthx6)
    month6 = datetime.datetime.strptime(month_x6, '%b %Y').month
    month_x7 = driver.getTextForElement(Monthx7)
    month7 = datetime.datetime.strptime(month_x7, '%b %Y').month
    month_x8 = driver.getTextForElement(Monthx8)
    month8 = datetime.datetime.strptime(month_x8, '%b %Y').month
    month_x9 = driver.getTextForElement(Monthx9)
    month9 = datetime.datetime.strptime(month_x9, '%b %Y').month
    month_x10 = driver.getTextForElement(Monthx10)
    month10 = datetime.datetime.strptime(month_x10, '%b %Y').month
    assert month2 - month1 == 1 or month4 - month3 == 1 or month6 - month5 == 1 or month8 - month7 == 1 or month10 -month9 ==1, "Months are not incrementing as expected on X Axis"

@step("I click on Quarterly option at the bottom of the home chart")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(Quarterly)
    driver.elementClick(Quarterly)
    time.sleep(10)


@then("I validate at the bottom of the chart I see the time on X Axis in Quarterly increments")
def step_impl(context):
    QuarterlyValidations = driver.getTextForElement(Increments)
    assert len(QuarterlyValidations) != 0, "Quarterly increments are not displayed on X Axis"
    time.sleep(10)


@then("I also validate the quarters are incrementing by 1 quarter at a time\.")
def step_impl(context):
    qtrseries1 = driver.getTextForElement(Quarterx1)
    qtrseries2 = driver.getTextForElement(Quarterx2)
    qtrseries3 = driver.getTextForElement(Quarterx3)
    qtrseries4 = driver.getTextForElement(Quarterx4)
    qtrseriesvalue1 = re.findall(r'\d+', qtrseries1)
    qtrseriesvalue2 = re.findall(r'\d+', qtrseries2)
    qtrseriesvalue3 = re.findall(r'\d+', qtrseries3)
    qtrseriesvalue4 = re.findall(r'\d+', qtrseries4)

    if (int(qtrseriesvalue1[0])) == 4 :
            int(qtrseriesvalue1[0]) == 0
    elif (int(qtrseriesvalue3[0])) == 4 :
            int(qtrseriesvalue3[0]) == 0

    assert int(qtrseriesvalue2[0]) - int(qtrseriesvalue1[0]) == 1 or int(qtrseriesvalue4[0]) - int(qtrseriesvalue3[0]) == 1, "Quarters are not incrementing by 1 at a time"


@step("I click on Yearly option at the bottom of the home chart")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(Yearly)
    driver.elementClick(Yearly)

@then("I validate at the bottom of the chart I see the time on X Axis in Yearly increments")
def step_impl(context):
    time.sleep(10)
    YearlyValidations = driver.getTextForElement(Increments)
    assert len(YearlyValidations) != 0, "Yearly increments are not displayed on bottom of X Axis"



@then("I also validate years are incrementing 1 year at a time\.")
def step_impl(context):
    Year1 = driver.getTextForElement(Yearx1)
    Year2 = driver.getTextForElement(Yearx2)
    Year3 = driver.getTextForElement(Yearx3)
    Year4 = driver.getTextForElement(Yearx4)
    Year5 = driver.getTextForElement(Yearx5)
    Year6 = driver.getTextForElement(Yearx6)

    assert int(Year2) - int(Year1) == 1 or int(Year4) - int(Year3) == 1 or int(Year6) - int(Year5) == 1, "Years are not incrementing by 1 year"

    #driver.closeBrowser()


@then("I validate Select location has a drop down present")
def step_impl(context):
    try:
        driver.waitOnElement(DropdownButton)
        time.sleep(10)
        driver.elementClick(DropdownArrow)
    except:
        print('Select Location has no dropdrown present')

@then('I validate select location text on the top bar is "Select Location"')
def step_impl(context):
    SelectLocText = driver.getTextForElement(SelLoclabel)
    assert SelectLocText == 'Select Location', "Select Location text is not correct"

@then("I validate the menu bar includes all the tabs: Home, My Page, Awards, Trending, Employees, Patients, Ambassadors, Data, Comments, Perks, Reviews")
def step_impl(context):
    time.sleep(10)
    assert driver.getTextForElement(Awards) == 'Awards', "Awards tab is not included in Home page Menu bar"
    #assert driver.getTextForElement(HomePage) == "Home", "Home tab is not included in Home Page Menu bar"
    assert driver.getTextForElement(MyPage) == 'My Page',  "My Page tab is not included in Home Page Menu bar"
    assert driver.getTextForElement(Trending) == 'Trending', "Trending tab is not included in Home Page Menu "
    assert driver.getTextForElement(Employees) == 'Employees', "Employees tab is not included in Home Page Menu "
    assert driver.getTextForElement(Patients) == 'Patients', "Patients tab is not included in Home Page Menu "
    assert driver.getTextForElement(Ambassadors) == 'Ambassadors', "Ambassadors tab is not included in Home Page Menu"
    assert driver.getTextForElement(Data) == 'Data', "Data tab is not included in Home Page Menu "
    assert driver.getTextForElement(Comments) == 'Comments', "Comments tab is not included in Home Page Menu "
    assert driver.getTextForElement(Perks) == 'Perks', "Perks tab is not included in Home Page Menu "
    assert driver.getTextForElement(Reviews) == 'Reviews', "Reviews tab is not included in Home Page Menu "


@then("I validate profile icon is present on the top left of the screen")
def step_impl(context):
    try:
        time.sleep(10)
        driver.getElements(Profile)
    except:
        print('Profile Icon is not present on top left of the screen')


@then("I validate Home button icon is present on the top left of the screen")
def step_impl(context):
    try:
        time.sleep(10)
        driver.getElements(Homeicon)
    except:
        print('Home button icon is present on the top left of the screen')


@then("I validate notification icon is present on the top left of the screen")
def step_impl(context):
    try:
        time.sleep(10)
        driver.getElements(Notifications)
    except:
        print('Notifications Icon is not present on top left of the screen')


@then("I click on line icon")
def step_impl(context):
    time.sleep(10)
    driver.waitOnElement(lineIcon)
    driver.elementClick(lineIcon)