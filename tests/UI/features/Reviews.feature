# Created by Wambi-Asad at 9/4/20
Feature: Review Tabs Testing Scnearios
  # Enter feature description here

    @WP-575-02
    Scenario: Add Spell Check on Peer Recognition-Reviews
      Given I navigate to Wambi Application
      And I click on Team Member Login
      And I enter username and password and click Login to login as SA User
      Then I click on Reviews Tab
      And click submit, click on a person, press start review, and navigate through the review until I reach the comment page
      Then in the comment bubble I add a random text and validate the spellcheck error line show after pressing space