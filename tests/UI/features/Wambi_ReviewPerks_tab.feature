# Created by Wambi-Asad at 10/20/20
Feature: Review Perks Tab
  # Enter feature description here

  @AT-13/WP-1161
  Scenario: Review Perks Tab
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    And I click on Perks tab
    Then I validate that available gift cards, Post Perk and PerkAlert email buttons are displayed
    And I click on PostPerk button
    Then I validate add reward page displays
    And I click on PERK Alert email button
    Then I validate PERK Alert email page displays
    And I check the Edit and Delete icon present on any available gift cards
    And I click on Edit button in gift card
    Then I validate the gift cards can be edited
    And I click on delete button
    Then I validate popup message displays with Cancel and Yes,delete it options

    @AT-12/WP-1160
    Scenario: Review Perks Tab
      Given I navigate to Wambi Application
      And I click on Team Member Login
      And I enter username and password and click Login to login as SE User
      And I hover on Perks tab
      And I click on Perk History subtab
      And I enter a valid text in search field and click on search button
      Then I validate the results  displayed as per the valid search data


