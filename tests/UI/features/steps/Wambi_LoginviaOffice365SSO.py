from behave import *
import mysql.connector
import utilities.config as sConfig
import random
import string
import re
use_step_matcher("re")


@given("Navigate to https://dev-w4\.wambiapp\.com/api/site/oauth/office365/login for the first time")
def step_impl(context):
    dbConn = mysql.connector.connect(host=sConfig.h,user=sConfig.u,passwd=sConfig.p,database=sConfig.d)
    print(dbConn)
    if dbConn:
        print('Connection established successfully')
    else:
        print('Connection not established')
    dbCursor = dbConn.cursor()
    dbCursor.execute("SELECT code from concept.reviewers where mobile = '2158631018'")
    result = dbCursor.fetchall()
    assert result != None, "code records are not returned for corresponding mobile number"
    for rows in result:
        res = int(''.join(map(str,rows)))
        print(res,"NOT NULL")


#write an assertion to look at the results and validate that no results have a
#null value for code

#Then I validate that all the records returned have a code in the code field and not null