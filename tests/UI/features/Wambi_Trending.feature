# Created by Wambi-Asad at 10/27/20
Feature: Create Trending Feed Post
  # Enter feature description here

  @WW-1028
  Scenario: Create Trending Feed Post
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I hover on Trending Tab
    And I click on "Add Post" option
    And I select Title, Facility,Clinic and Tag People to Post values
    Then I press Submit at the bottom of the Page
    When I click on Trending Tab Solution
    And Search for the newly created post in the Search bar
    Then I validate that the new created Trending feed post does show up in search results
