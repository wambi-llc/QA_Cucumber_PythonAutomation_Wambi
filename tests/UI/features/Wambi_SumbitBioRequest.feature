# Created by Wambi-Asad at 11/3/20
Feature: Submit Bio Request
  # Enter feature description here

  @WW-1024
  Scenario: Submit Bio Request
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    And click on UsersProfile image
    And click on users name
    And Scroll down to the Bio Info section and hover over the "?" bubble
    #Then check for sample text:"15 years as a Registered Nurse. Enjoy reading Harry Potter"
    And enter text in Bio Info tab
    Then submit the Bio Request
    Then it should route to Mypage tab
