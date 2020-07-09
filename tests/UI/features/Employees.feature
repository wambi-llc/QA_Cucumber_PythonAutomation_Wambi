# Created by Wambi-Asad at 6/1/20
Feature: Employee Tab
  # Enter feature description here

  @412 @UI-Regression
  Scenario: Download Employee Tab Report
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I click on Employees Tab Solution
    And I click on Excel button
    Then I validate the Excel sheet downloads

  @UI-Regression
  Scenario: Add a New Employee when logged in as a SE User
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I hover on Employees Tab Solution
    And I click on "Add a New Employee" option
    Then I choose random option from the User Type dropdown
    And I select a random facility, random clinic/department, and a random discipline
    And I generate a random number between 3 and 50 digits for the Employee ID
    And I generate a random string of letters for First Name, Last Name and Display Name
    Then I press Submit at the bottom of the Employee Registration Page
    When I click on Employees Tab Solution
    And Search for the newly created employees First Name in the Search bar
    Then I validate that the new employee does show up in search results








#  @415
#  Scenario: Inactive users should only show for SE users and not SA users
#    Given I navigate to Wambi Application
#    And I click on Team Member Login
#    And I enter username and password and click Login to login as SE User
#    When I click on Employees Tab Solution
#    And I click on delete icon under the Actions tab to make that Employee Inactive
#    Then I search for that employee and validate that employee is still showing for SE user but doesn't have delete sign anymore
#    Then I logout of the Application
#    Given I navigate to Wambi Application
#    And I click on Team Member Login
#    And I enter username and password and click Login(change this to as SA User)
#     When I click on Employees Tab Solution
#    And I click on delete icon under the Actions tab to make that Employee Inactive
#    Then I search for that employee and validate that employee IS NOT pulling up for SA user
