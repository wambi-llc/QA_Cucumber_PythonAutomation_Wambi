# Created by Wambi-Asad at 10/16/20
Feature: Add Ambassador
  # Enter feature description here

  @AT-9
  Scenario: Add a New Ambassador when logged in as a SE User
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I hover on Ambassadors Tab Solution
    And I click on "Add a Ambassador" option
    And I select a random facility, random clinic/department
    And I generate a random number between 3 and 50 digits for the Abassador ID
    Then I press Submit at the bottom of the Ambassador Registration Page
    When I click on Ambassadors Tab Solution
    And Search for the newly created Ambassador  Name in the Search bar
    Then I validate that the new Ambassador does show up in search results



