# Created by Wambi-Asad at 12/14/20
Feature: Login via Office365 SSO
  # Enter feature description here

  @WP-1432
  Scenario: Login via Office 365 SSO URL
    Given Navigate to https://dev-w4.wambiapp.com/api/site/oauth/office365/login for the first time
    And Accept and grant permissions for the Office365 SSO
    Then  Login to Office365 using your Wambi Login and complete all steps