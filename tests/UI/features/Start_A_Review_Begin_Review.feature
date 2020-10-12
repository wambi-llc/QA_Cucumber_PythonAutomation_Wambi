# Created by Wambi-Asad at 10/12/20
Feature: Start a review - Begin Review Test Cases
  All the test scripts after user starts a review.

  @WP-540
  Scenario: Leave Comment
    Given I am a patient portal user
    And have searched for the person I want to recognize
    And am reviewing someone
    When I rate a question at or below the configured setting to prompt for a comment (  )
    Then I am prompted to enter a comment
    And I can tap to enter a comment
    And my comment text is checked for spelling errors by my browser
    Then I signout from PortalUser

  @WP-540
  Scenario: Toggle “Contact Me”
    Given I am a patient portal user
    And have searched for the person I want to recognize
    And am reviewing someone
    When I rate a question at or below the configured setting to prompt for a comment (  )
    Then I am prompted to enter a comment
    When I toggle On the setting to “Contact Me”
    Then a form appears asking me for my contact information.
    And my phone # or email address is already entered (from authentication WP-525)
    When I tap on the Wambi bird (the design may change) in the top left,
    Then I am redirected back to the Search Location screen
    Then I signout from PortalUser

  @WP-537
  Scenario: Review Back Questions Scenario
    Given I am a patient portal user
    And  have searched for the person I want to recognize
    And I have started the survey questions for my selected person
    And want to change my answer or see how I responded
    When I tap on “Back” Then I am returned to the previous review question
    And can change my response
    When I tap on the Wambi bird (the design may change) in the top left,
    Then I am redirected back to the Search Location screen
    Then I signout from PortalUser

  @WP-536
  Scenario: Exit Review without answering the Questions
    Given I am a patient portal user
    And  have searched for the person I want to recognize
    And I have started the survey questions for my selected person
    When I tap on the Wambi bird (the design may change) in the top left,
    Then I am redirected back to the Search Location screen
    Then I signout from PortalUser

  @WP-534
  Scenario: Confirm Person Begin Review
    Given I am a patient portal user
    And I have searched for the person I want to recognize
    And the modal is open with the correct person’s information
    And the correct Unit/Department is selected
    When I tap on the Begin Review button
    Then I am navigated to the 1st step in the Survey questions for my selected person
    When I tap on the Wambi bird (the design may change) in the top left,
    Then I am redirected back to the Search Location screen
    Then I signout from PortalUser

  @WP-542
  Scenario:Complete Share Your Gratitude Screen
    Given I am a patient portal user
    And   searched for the person I want to recognize
    And I have completed a review for a nurse
    When I have completed OR skipped the Share your Gratitude screen
    Then I am taken to the “Nominate This Nurse” screen
    When I complete all of the prompts for “Nominate This Nurse” screen
    Then I see the Submit button switch from gray to blue
    And I can submit my nomination
    Then I signout from PortalUser