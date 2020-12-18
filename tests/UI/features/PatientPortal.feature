Feature: Patient Portal Regression
  Navigating and interacting with the Patient Portal application

  @patient_portal @smoke
  Scenario: Validating location selection, employee selection, review questions, going through the full
  patient review process with a perfect score, sending a Carepostcard, nominating the employee for a
  Daisy Award

    Given I have begun the patient portal review process
    And I search for and select a location
    And I am able to log in using my email
    When I validate the selected location
    And I search and select a specific employee to review
    Then I will be able to answer all the expected questions for the expected employee (perfect score)
    And I will be able to complete a carepostcard
    And I will be able to nominate the employee for a Daisy Award

  @patient_portal
  Scenario: Going through the full patient review process with a subpar score, skipping the CarepostCard and
  Daisy Award Nomination

    Given I have begun the patient portal review process
    And I search for and select a location
    And I am able to log in using my email
    When I validate the selected location
    And I search and select a specific employee to review
    Then I will be able to answer all the expected questions for the expected employee (subpar score)
    Then I will be able to give feedback on what could have been done better
    And I will be able to skip the Carepostcard and Daisy Award sections

  @patient_portal
  Scenario: Validating Spanish/English language selection throughout review process

    Given I validate language options on the landing page and begin the patient portal review process
    And I validate language options before searching for selecting a location
    And I validate language before logging in using my email
    Then I validate language options in the side bar
    And I validate language options on employee search before beginning a review
    Then I validate expected questions are displayed in Spanish throughout review process
    And I validate language on the Carepostcard and Daisy Award sections

#  Scenario: Smoke Test Demo
#    * Full Demo Step
