Feature: Delete content from the application
  Verify user is able to delete the content from the application

  Scenario: Delete Folder
    Given User is logged in the application
    Given "Automation_Demo_1" folder is present on home screen
    When User taps on three dot menu button of "Automation_Demo_1" folder
    Then Tap Delete option from the pop up menu
    And Tap Delete button on the Delete confirmation pop up
    And Verify "Automation_Demo_1" folder is deleted


  Scenario: Delete File
    Given User is logged in the application
    Given "image_1.jpg" file is present on home screen
    When User taps on three dot menu button of "image_1.jpg" file
    Then Tap Delete option from the pop up menu
    And Tap Delete button on the Delete confirmation pop up
    And Verify "image_1.jpg" file is deleted