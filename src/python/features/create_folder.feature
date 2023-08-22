Feature: Create Folder
Verify user is able to create folder

#  @smoke @run(order=2)
  Scenario: Create_folder
  Given User is logged in to the application
  When User taps on the Add button
  Then User taps on the New Folder option
  And User enters folder name "Automation_Demo_1" in the input field
  When User taps on the Create button
  Then Verify "Automation_Demo_1" folder is created successfully



