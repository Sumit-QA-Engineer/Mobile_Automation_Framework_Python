import os
import subprocess

import pytest

# Get the path to the 'tests' directory
tests_directory = r"C:\Users\subassan\PycharmProjects\mobile_aautomation_pytest_bdd"

print(tests_directory)
# Run all the test cases using pytest and generate the Allure report

# pytest.main([tests_directory, "--alluredir", "allure-report"])
pytest.main([
    tests_directory,
    "-m", "smoke",
    f"--alluredir={os.path.join(tests_directory, 'reports')}",
    "--clean-alluredir"
])
# subprocess.run([tests_directory, "allure", "serve", "allure-report"])
os.system(
    f"allure generate {os.path.join(tests_directory, 'reports')} --clean -o {os.path.join(tests_directory, 'allure-report')}")
