Feature: Imperative Version of Happy Path

  Scenario: CarePostCard creation happy path - Admin account (Imperative)
    Given I navigate to the Carepostcard application
    And I click on the sign in button
    When I sign in as an admin using my email
    And I enter the post creation screen
    When I validate that the address to section loads properly
    And I validate that the Carepostcard body loads properly
    And I validate that the location section loads properly
    And I validate that the Carepostcard creation button starts off disabled
    When I fill out the addressee section with a random number
    And I fill out the Carepostcard body with a random number
    And I select a location
    When I post the CarePostCard
    And I click on my last created Carepostcard
    Then I validate that the CarePostCard loads properly
    And I validate that the expected addressee text is present
    And I validate that the expected body text is present