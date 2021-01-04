# Created by Wambi-Asad at 10/16/20
Feature: Review Button Security Update
  # Enter feature description here

  @AT-4
  Scenario: Review Button Security Update
    Given I am a Wambi Admin (SE, SA)
    And I am logged in
    When I click on Reviews Tab
    Then I logged out from Wambi Site and navigate to Patient Portal
