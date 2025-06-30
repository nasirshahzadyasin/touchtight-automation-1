Feature: Test Pricing functionality

  Scenario: Click Pricing button on home page
    Given I am on the homepage
    When I click Pricing link button
    Then I should navigate to billing page and verified "Finalize Your Subscription"
