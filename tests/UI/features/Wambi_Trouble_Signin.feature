# Created by Wambi-Asad at 12/31/20
Feature: Trouble Signin
  # Enter feature description here

  @WP-1414
  Scenario: Trouble Signin
   Given I am Tina
   And I have navigated to the Wambi URL
   And I do not remember my username/password Or I do not have a username/password
   When I click the “Trouble signing in?” link
   Then the Sign In Help window appears
