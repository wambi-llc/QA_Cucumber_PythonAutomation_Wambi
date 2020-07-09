# Created by Wambi-Asad at 6/10/20
Feature: Data Tab
  # Enter feature description here

  @414-1 @PositiveScenario @Regression
  Scenario: Validate search function is returning proper results
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I click on Data Tab
    And I click on Detailed Review History under Data Tab
    And I enter a careproviders name in the search field {Alessandra Smith} and click search
    #Then I change show entries to 100 from the show entries dropdown
    Then I validate all the returned results are only for the careprovider that was searched

  @414-2 @NegativeScenario
  Scenario: Validate search function is returning proper results
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I click on Data Tab
    And I click on Detailed Review History under Data Tab
    And I enter a careprovider's name that doesn't exist{asfdlkjvixlkcjv} and click search
    Then I validate no results are returned

