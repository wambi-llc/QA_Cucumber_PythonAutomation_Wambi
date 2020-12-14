Feature: Wambi Platform Regression
  Navigating and interacting with the Wambi Platform

  @wambi_platform @smoke
  Scenario: Early environment testing

    #Todo: Put together test when dev is ready (navigation buttons currently unclickable)
    Given I have navigated to the Wambi application
    And I have logged in
    Then I am able to click on all the navigation buttons
    Then I am able to view my profile
    And I am able to view the available tabs
    Then I am able to sign out

  Scenario: Log in failure testing
    Given I have navigated to the Wambi application
    When I attempt to log in without entering a username or password
    Then I will not be able to click the log in button
    When I attempt to log in without entering a password
    Then I will not be able to click the log in button
    When I input a username with an incorrect password
    Then I will be able to click the log in button
    But I will not be able to log in and an error message will display