# Created by Wambi-Asad at 12/31/20
Feature: Collect Reviews
  # Enter feature description here

  @WP-1208-01
  Scenario: Navigate to My Only Portal
    Given Navigate to https://dev-w4.wambiapp.com/auth/login
    And I enter username and password and click Login to login as Admin User
    Then You are taken to https://dev-w4.wambiapp.com/admin
    And Click on your profile icon
    And Click on Collect Patient Gratitude
    Then User is routed to the /portal/location page and can select their location
    Then There should be more than one location
    And Select your location and click Continue
    Then User is routed to the /portal/employee (Who would you like to recognize)
    When Attempt to access wambi app
    Then User should not be able to   access the Wambi app without reauthetcating


    @WP-1208-02
  Scenario: Navigate to One of Portals
    Given I am a leader
    And I have permissions to collect reviews for team members
    When I click on the Collect Patient Gratitude menu item
    Then I am prompted to select one of my available portals
    And am taken directly to the portal
    And am already authenticated as a portal user
    And am logged out of the team member interface
