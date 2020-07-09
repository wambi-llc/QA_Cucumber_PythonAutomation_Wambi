# Created by Wambi-Asad at 6/12/20
Feature: Login Page
  # Enter feature description here

  @418
  Scenario: Attribute "autocomplete=off" set for Username and
  FORM
    Given I navigate to Wambi Application
    And I click on Team Member Login
    Then I validate attribute for username and password FORM page is set to "autocomplete=off"


