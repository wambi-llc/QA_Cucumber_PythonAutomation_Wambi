# Created by Wambi-Asad at 9/4/20
Feature: My Page Test Scenarios
  # Enter feature description here

    @WP-575-01
    Scenario: Add Spell Check on Peer Recognition
     Given I navigate to Wambi Application
      And I click on Team Member Login
      And I enter username and password and click Login to login as SA User
      Then I click on My Page Tab
      And I click on Send Peer CarePost Card
      Then I write a random generated phrase in the write message box and validate it's highlighted as error.

  @WP-1154
  Scenario: Sending Peer Carepostcard as a Super Admin
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on My Page Tab
    And I click on Send Peer CarePost Card
    And fill out a Carepostcard to another employee
    Then the review Carepostcard screen will pop up
    And I can send the Carepostcard