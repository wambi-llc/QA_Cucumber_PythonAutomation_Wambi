Feature: Wambi Platform Regression
  Navigating and interacting with the Wambi Platform

  @wambi_platform @smoke
  Scenario: Log in failure testing
    Given I have navigated to the Wambi application
    When I attempt to log in without entering a username or password
    Then I will not be able to click the log in button
    When I attempt to log in without entering a password
    Then I will not be able to click the log in button
    When I input a username with an incorrect password
    Then I will be able to click the log in button
    But I will not be able to log in and an error message will display
    When I enter the 'Trouble signing in' section
    And I input my phone or email and click 'send code'
#    Then I will be able to sign in using a code sent to me

  @wambi_platform @smoke
  Scenario: Collect a review through the Wambi application
    Given I have navigated to the Wambi application
    When I log in to Wambi
    And I click the button to enter the review section
    And I search for and select a ACME as my portal and location
    And I search and select an ACME employee to review
    Then I will be able to answer all the expected questions for the ACME employee (perfect score)
    And I will be able to complete a carepostcard
    And I can click the donation button and see the wambi.org URL
    And I can choose to give another review
    Then I can sign out of the review process

  @wambi_platform @smoke
  Scenario: Submitting a ticket through the Help and Support section
    Given I have navigated to the Wambi application
    When I log in to Wambi
    And I enter the Help and Support Section
    When I input all the required fields
    Then I will be able to submit a ticket
    Then I can sign out of the Wambi platform

  @wambi_platform @smoke
  Scenario: Editing a profile picture
    Given I have navigated to the Wambi application
    When I log in to Wambi
    And I enter the edit profile screen
    And I upload a new picture
    And I play with the zoom toggle
    And I save the new picture
    Then the new profile picture will be displayed
    Then I can sign out of the Wambi platform

  @wambi_platform @smoke
  Scenario: Newsfeed scrolling and reacting
    Given I have navigated to the Wambi application
    When I log in to Wambi
    And I navigate to the home page
    Then 10 items from the newsfeed will be loaded
    And I will be able to add and remove emoticons
    And I am able to see at least one other newsfeed item after scrolling down the page
    Then I can sign out of the Wambi platform