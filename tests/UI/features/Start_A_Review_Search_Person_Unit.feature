# Created by Wambi-Asad at 10/12/20
Feature: Start A Review Search
  Test Scripts related to searching Person/Unit

  @WP-529
  Scenario: Initial Scrollable List - 10 people
    Given I am a patient portal user
    And I have selected a location Or been sent directly to this page from the chatbot
    When the page loads
    Then I can see a list of the first 10 people
    And the list is sorted alphabetically by last name
    Then I signout from PortalUser

  @WP-529
  Scenario: Enter text to search
    Given I am a patient portal user
    And I have selected a location Or been sent directly to this page from the chatbot
    And I am on the search for person screen
    When I enter text in the search box
    Then the list of people is filtered to match my search text
    Then I signout from PortalUser

  @WP-531
  Scenario: Click “+ Unit” Button
    Given I am a patient portal user
    And  have searched for the person I want to recognize
    When I click the + Unit button
    Then I can see a list of Units
    And can search the list of Units by entering text.
    And can select one from the list of Units
    Then the unit I selected is indicated above the result list
    And any previously selected unit is replaced
    And the results list is updated to show only people with my selected unit.
    Then I signout from PortalUser

  @WP-530
  Scenario: Click “+ Job Type” Button
    Given I am a patient portal user
    And  have searched for the person I want to recognize
    When I click the Job Type button
    Then I can see a list of Job Types
    And can search the list by entering text.
    And can select one
    Then the job type I selected is indicated above the result list
    And any previously selected job type is replaced
    And the results list is updated to show only people with my selected job type.
    Then I signout from PortalUser