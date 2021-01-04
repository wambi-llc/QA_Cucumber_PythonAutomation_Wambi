# Created by Wambi-Asad at 12/10/20
Feature: Edit User Profile
  # Enter feature description here

  @WP-1155
  Scenario: Submit Bio Request and validate
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    And click on UsersProfile image
    And click on users name
    And enter text in Bio Info tab
    Then submit the Bio Request
    Then it should route to Mypage tab
    Then  I validate that the Bio Info has been changed