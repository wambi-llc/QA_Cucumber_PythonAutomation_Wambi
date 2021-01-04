# Created by Wambi-Asad at 10/16/20
Feature: Send Individual Award
  # Enter feature description here

  @AT-11/@WP-1163
  Scenario: Send Individual Award when logged in as a SE User
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I hover on Awards Tab Solution
    And I click on "Post Award" option
    And I click on Individual Award
    And I select a Select Individuals, Employee Award,AwardType, Spedify details,TimePeriod and Badge
    Then I press Submit individual award at the bottom of the Page
    When I click on Awards Tab Solution
    And Search for the newly created Individual Award in the Search bar
    Then I validate that the new created Award does show up in search results
