# Created by Wambi-Asad at 6/24/20
Feature: Home Tab

  Scenario: Validate home chart timing preferences.
  Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate at the bottom of the chart I see all 4 options (Weekly, Monthly, Quarterly, Yearly)


  Scenario: Validate Weekly Option shows time on X Axis in Weekly increments
    Given I navigate to Wambi Application
      And I click on Team Member Login
      And I enter username and password and click Login to login as SA User
      Then I click on Home Tab
      And I click on Weekly option at the bottom of the home chart
      Then I validate at the bottom of the chart I see the time on X Axis in Weekly increments

  Scenario: Validate Monthly Option shows time on X Axis in Weekly increments
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    And I click on Monthly option at the bottom of the home chart
    Then I validate at the bottom of the chart I see the time on X Axis in Monthly increments
    Then I also validate the months are incrementing by 1 month at a time

  Scenario: Validate Quarterly Option shows time on X Axis in Weekly increments
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    And I click on Quarterly option at the bottom of the home chart
    Then I validate at the bottom of the chart I see the time on X Axis in Quarterly increments
    Then I also validate the quarters are incrementing by 1 quarter at a time.

  Scenario: Validate Yearly Option shows time on X Axis in Weekly increments
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    And I click on Yearly option at the bottom of the home chart
    Then I validate at the bottom of the chart I see the time on X Axis in Yearly increments
    Then I also validate years are incrementing 1 year at a time.

  Scenario: Validate Location drop down is showing correctly in the top bar
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate Select location has a drop down present

  #Scenario: Validate the text for Location in the top bar reads "Select Location"
  # Given I navigate to Wambi Application
    #And I click on Team Member Login
    #And I enter username and password and click Login to login as SA User
    #Then I click on Home Tab
    #Then I validate select location text on the top bar is "Select Location"

  Scenario: Validate menu bar includes all tabs: Home, My Page, Awards, Trending, Employees, Patients, Ambassadors, Data, Comments, Perks, Reviews
   Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate the menu bar includes all the tabs: Home, My Page, Awards, Trending, Employees, Patients, Ambassadors, Data, Comments, Perks, Reviews

  Scenario: Validate Profile icon is present on the top left
   Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate profile icon is present on the top left of the screen

  Scenario: Validate Home Button is present on the top left
   Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate Home button icon is present on the top left of the screen


  Scenario: Validate alerts icon is present on the top left
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SA User
    Then I click on Home Tab
    Then I validate notification icon is present on the top left of the screen
