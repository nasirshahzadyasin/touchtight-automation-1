Feature: Touchtight Signup feature
  Scenario: Signup to touchtight with valid parameters
    Given I open touchtight app
    When I open touchtight Signup page
    And Enter email "testns0222+e24o@gmail.com"
    And Click get started button
    And Enter fullname "testns"
    And Enter password "P@ss1234"
    And Enter application secret key
    And Enter club name "new club"
    And Click Create Account button
    Then Verify that user account created successfully
