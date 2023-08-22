Feature: Upload Content in Application
  Verify user is able to upload content in application

#  @run(order=1)
  Scenario: Upload File
    Given Driver is Up
    Given User is logged in the application
    When User tap on Add button
    Then Tap on Upload Content option
    And Tap on "Select files to upload" option
    And Select the "image_1.jpg" from the device manager
    And Verify "image_1.jpg" is uploaded in the application