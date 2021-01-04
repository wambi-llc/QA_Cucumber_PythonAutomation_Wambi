# Created by Wambi-Asad at 10/16/20
Feature: Send Group Award
  # Enter feature description here

  @AT-10
  Scenario: Send Group Award when logged in as a SE User
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I hover on Awards Tab Solution
    And I click on "Post Award" option
    And I select a random facility, random clinic/department,AwardType, TimePeriod and Badge
    #And I select Award Type,TimePeriod and Badge
    #And I generate a random number between 3 and 50 digits for specify details field
    Then I press Submit at the bottom of the Page
    When I click on Awards Tab Solution
    And Search for the newly created Group Award in the Search bar
    Then I validate that the new Group Award does show up in search results
