Feature: Awards Tab

#  https://app.assembla.com/spaces/Current-Platform/tickets/realtime_cardwall?ticket=413

  @413
  Scenario: Zoom in on to validate page spatial relationships are preserved for Awards Sub Tabs(Date, Action) in Chrome
    Given I navigate to Wambi Application
    And I click on Team Member Login
    And I enter username and password and click Login to login as SE User
    When I click on Awards Tab
    And I Zoom In to Screen to max Zoom In allowed
    Then I validate the Date sub tab is showing all the text
    Then I validate the Action sub tab is showing all the text
