# Created by Wambi-Asad at 6/1/20
Feature: Download Employee Tab
  # Enter feature description here

  @412 @UI-Regression
  Scenario: Download Employee Tab Report
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login
    When I click on Employees Tab Solution
    And I click on Excel button
    Then I validate the Excel sheet downloads