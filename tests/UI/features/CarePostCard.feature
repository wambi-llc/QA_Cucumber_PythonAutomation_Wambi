Feature: CarePostCard Regression
  Navigating CarePostCard.com

  Scenario: CarePostCard creation happy path - Admin account
    Given I navigate to the Carepostcard application
    And I sign in as an admin
    When I create a Carepostcard
    And I click on my last created Carepostcard
    Then the expected Carepostcard data will be present

  Scenario: CarePostCard creation happy path - Regular account
    Given I navigate to the Carepostcard application
    And I sign in as a regular user
    When I create a Carepostcard
    And I click on my last created Carepostcard
    Then the expected Carepostcard data will be present

  Scenario: CarePostCard creation happy path - New account
    Given I navigate to the Carepostcard application
    And I create a Carepostcard before signing in
    Then I am directed to create a new account
    And I create a new user
    When I click on my last created Carepostcard
    Then the expected Carepostcard data will be present

  Scenario: CarePostCard creation and editing - Admin account
    Given I navigate to the Carepostcard application
    And I sign in as an admin
    When I create a Carepostcard
    And I navigate to the admin panel
    When I edit the body text of a Carepostcard
    And reload the admin page
    Then the edited text should persist

  Scenario: CarePostCard creation and hiding - Admin account
    Given I navigate to the Carepostcard application
    And I sign in as an admin
    When I create a Carepostcard
    And I navigate to the admin panel
    When I hide the most recently created Carepostcard
    And reload the admin page
    Then the expected Carepostcard should remain hidden

  Scenario: CarePostCard creation and featuring - Admin account
    Given I navigate to the Carepostcard application
    And I sign in as an admin
    When I create a Carepostcard
    And I navigate to the admin panel
    When I feature the most recently created Carepostcard
    And return to the home page
    Then the expected Carepostcard should be featured

  Scenario: Attempting to access admin panel as regular user - Regular account
    Given I navigate to the Carepostcard application
    And I sign in as a regular user
    When I navigate to the admin panel
    Then I am re-directed to the home page

  Scenario: CarePostCard manage hashtags - Admin account
    Given I navigate to the Carepostcard application
    And I sign in as an admin
    When I create a Carepostcard with a unique hashtag
    And I navigate to the manage hashtags section

  Scenario: CarePostCard Twitter link - Regular account
    Given I navigate to the Carepostcard application
    And I sign in as a regular user
    When I create a Carepostcard
    And I click on my last created Carepostcard
    And I click the Twitter link
    Then I will be redirected to the Twitter site

#  Scenario Outline: CarePostCard social media - Regular account
#    Given I navigate to the Carepostcard application
#    And I sign in as a regular user
#    When I create a Carepostcard
#    And I click on my last created Carepostcard
#    And I click the <social media> link
#    Then I will be redirected to the <social media> site
#
#  Examples:
#    |social media |
#    |facebook     |
#    |twitter      |
#    |linkedin     |

#  Scenario: Attempting to access manage hashtags section as regular user - Regular account
#    Given I navigate to the Carepostcard application
#    And I sign in as a regular user
#    When I navigate to the manage hashtags section
#    Then I am re-directed to the home page
#
#  Scenario: Creating a Carepostcard with a new hashtag and featuring the new hashtag
#    Given I navigate to the Carepostcard application
#    And I sign in as an admin
#    When I create a Carepostcard with a new hashtag
#    And I navigate to the manage hashtags section
#    When I decide to feature the new hashtag
#    And return to the home page
#    Then the expected Carepostcard should be featured in the expected section