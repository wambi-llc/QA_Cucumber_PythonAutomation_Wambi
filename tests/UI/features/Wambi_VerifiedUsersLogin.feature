# Created by Wambi-Asad at 10/16/20
Feature: Login for Verified Users
 @AT-8

 Scenario: Verified User: Employee User, Super Admin
   Given I am a User that has logged into the Wambi platform
   And completed verification steps
   And I enter my User ID and Password on the login page as Employee or SA users
   And I click Submit
   Then I am routed to My Page

 Scenario: Verified User: Super Exec
   Given I am a User that has logged into the Wambi platform
   And completed verification steps
   And I enter my  User ID and Password on the login page as SE user
   And I click Submit
   Then I am routed to the Ratings tab