Feature: Touchtight login feature

  Scenario: Login to touchtight with valid parameters
    Given I launch chrome browser
    When I open touchtight login page
    And Enter login email "testns0222+0290@gmail.com"
    And Enter login password "P@ss1234"
    And Click the login button
    Then User must successfully login to the touchtight

# Scenario Outline: Login to touchtight with valid parameters
#    Given I launch chrome browser
#    When I open touchtight login page
#    And Enter username "<email>" and password "<password>"
#    And Click the login button
#    Then User must successfully login to the touchtight
#   Examples:
#     | email                      | password |
#     | testns0222+9200@gmail.com  | P@ss1234 |
#     | testns0222+9500@gmail.com  | P@ss1234 |
#     | testns0222+9600@gmail.com  | P@ss1234 |
