# Created by Wambi-Asad at 10/12/20
Feature: Start a review - Location Test Scripts
  All Test Cases related to selecting updating/changing locations.

  @WP-523
  Scenario: Validate Select Location to Preview
    Given I am a patient portal user
    And have searched for a location Or scrolled to find my desired location
    When I tap on the location tile
    Then I am shown a confirmation box
    And the box contains the image, name, and address
    And a Next button
    And an X button

  @WP-523
  Scenario: Validate Close Confirmation
    Given I am a patient portal user
    And I have previewed a location
    When I click the X button and then the confirmation box closes
    And I can resume my search for a location
    And select another location

  @WP-523
  Scenario: Next Button to Select Location--Not Authenticated
    Given I am a patient portal user
    And I have previewed a location
    When I click the Next button
    Then I am taken to the Patient Portal Login page

  @WP-523
  Scenario: Next Button to Select Location--Verified Authentication
    Given I am a patient portal user
    And I previewed a location
    When I click the Next button
    Then I am taken to the Team member search

    @WP-524
  Scenario: Open Hamburger Menu to View Location
    Given I am a patient portal user
    And have selected my location and have authenticated
    When I tap the Hamburger menu
    Then a menu opens up
    And I can see my current selected location
    And I can tap to change my location
    Then I signout from PortalUser

  @WP-524
  Scenario: Change Location
    Given I am a patient portal user
    And have selected my location
    When I tap to change my location
    Then I am taken to the Location Search page
    And can change my location without re-authenticating
