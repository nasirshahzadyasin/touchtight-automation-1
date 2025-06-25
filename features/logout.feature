Feature: Test Logout Functionality

  @login_required
  Scenario: Logout from the application
    Given I am on the home page
    When I click the profile icon
    And I click the logout button
    Then I should see confirmation of successful logout