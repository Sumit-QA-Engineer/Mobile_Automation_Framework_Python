Feature: User Logout
  Verify user is able to logout from the applicaton

  Scenario: Successful Logout
    Given User is logged in the application
    When User taps on Profile Icon at toolbar
    Then Tap on Logout option on the Profile screen
    And Tap on Logout button on Logout confirmation pop up
    And Verify user logouts from the application