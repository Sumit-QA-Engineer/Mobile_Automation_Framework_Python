# Mobile Automation Framework with Python and pytest-bdd

This repository contains a mobile automation framework built using Python as the scripting language and pytest-bdd as the framework model. The framework is designed to facilitate the automation of mobile applications using behavior-driven development (BDD) principles, allowing for efficient collaboration between developers, testers, and product owners.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Writing and Organizing Tests](#writing-and-organizing-tests)
- [Executing Tests](#executing-tests)
- [Comprehensive Reporting](#comprehensive-reporting)
- [Integrating with PyCharm](#integrating-with-pycharm)
- [Additional Essential Software](#additional-essential-software)
- [Contributing](#contributing)

## Introduction

This framework provides an organized and scalable approach to automate mobile application testing using the pytest-bdd framework. It allows you to define test scenarios using Gherkin syntax, which enhances collaboration among cross-functional teams and improves the readability of test scenarios.

## Features

- Integration of Python and pytest-bdd for BDD-style test automation.
- Supports mobile applications on Android and iOS platforms.
- Well-defined folder structure for easy test case management and maintenance.
- Customizable configuration options for different environments and devices.
- Allure reporting to track and visualize test execution results.
- Reusable test functions for efficient scripting.

## Getting Started

### Prerequisites

Before diving into the framework, ensure you have the following software components installed:

- **Python (>= 3.6)**: The programming language that powers the framework.
- **pip**: The package installer for Python.
- **Appium**: The mobile automation framework for Android and iOS.
- **Android SDK**: Necessary for Android app testing.
- **Xcode**: Required for iOS app testing.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Sumit-QA-Engineer/Mobile-Automation-Framework-Python-and-Pytest-bdd.git

2. Create a virtual environment (recommended):

   ```bash
   cd mobile-automation-framework
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Project Structure

The framework employs a modular structure for efficient management and organization of your test suite. Here's a brief overview of the core directories:

1. features: Contains Gherkin feature files outlining test scenarios.
2. pages: Houses Page Objects, encapsulating interactions with app screens.
3. tests: Hosts test modules that utilize Page Objects and step definitions.
4. properties: Stores configuration properties settings for test execution.
5. allure-report: Stores allure reports generated after test execution.
6. app: Place your test apk or ipa files here

```bash
   mobile-automation-framework/
   ├── allure-report
   ├── app
   ├── properties_files
      ├── config.properties
      └── ...
   ├── reports
   ├── runner_files
      ├── main_runner.py
      └── ...
   ├── screenshots
   ├── src
      ├── main
         ├── driver
            ├── driver.py
         ├── excelReader
            ├── excel_reader.py
         ├── logging
            ├── bdd_logging.py
         ├── pages
            ├── base_page.py
            └── ...
         ├── utilities
            ├── capture_screenshot.py
            └── ...
      ├── python
         ├── features
            ├── user_login.feature
            └── ...
         ├── tests
            ├── test_TC_001_user_login.feature
            └── ... 
   ├── pytest.ini
   ├── requirement.txt

```

## Writing and Organizing tests
Tests are articulated using Gherkin syntax within feature files, located in the features directory. Corresponding step definitions are implemented in the steps directory. Page Objects, residing in the pages directory, facilitate interactions with app screens, promoting a cleaner and more maintainable test suite.

## Executing Tests
1. Set the environment and os on which you want to run the test in config.properties files
```bash
[Configuration]
# set the platform bs or local
platform = bs

# set the os iOS or Android
os_name = android

#for local servers set the port
port = 4723

#for BS set the username and access_key
user_name = ...
access_key = ...
```

2. Set the app path or ids in respective local.properties and browserStack.properties

- **Note**: This framework is basically build for box application. You can download it from playstore or download it from this link - https://box.en.uptodown.com/android/download

3. Execute tests with the following command:

- **Note** - Make sure your terminal is in the project directory
```bash
   python runner_files/main_runner.py
```

## Comprehensive Reporting

Test execution outcomes are meticulously captured in allure reports, available in the allure-reports directory. These reports provide a clear and comprehensive overview of test results, assisting in identifying issues and gauging overall test coverage

## Integrating with PyCharm

This framework seamlessly integrates with the PyCharm IDE, providing an enriched development experience with features such as code completion, debugging, and seamless navigation. Open the project directory in PyCharm to leverage these capabilities.

## Additional Essential Software
In addition to the core framework, the following software components are indispensable:

1. PyCharm: A powerful IDE that streamlines project management and coding tasks.
2. Git: The version control system of choice for collaborative development.
3. Appium Desktop: A GUI application for managing the Appium server and inspecting app elements.
4. Android Studio: An IDE crucial for Android development, necessary for Android testing.
5. Xcode: The essential IDE for iOS development, required for iOS testing.

## Contributing
Contributions to this framework are highly encouraged and welcomed! Feel free to submit issues and pull requests for improvements, bug fixes, or new features.
