
Feature: user_login
  Verify the user is able to login successfully or not

#  @smoke @run(order=3)
  Scenario Outline: Successful login
    Given Driver is up and launch the application
    When User taps Log In button
    Then Enter the email "<email>" in email field
    And Tap Next button
    Then Enter the psw "<password>" in password field
    And Tap Login button
    And Verify user is login successfully


    Examples:
    | email               | password   |
    | subassan8@gmail.com | #ABC123@   |

