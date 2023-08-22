import configparser
import os
def get_main_project_directory(project_name):
    current_directory = os.getcwd()
    project_directory = current_directory.split(project_name)[0] + project_name
    return project_directory


class readProperties:
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        prop_dir = get_main_project_directory("mobile_aautomation_pytest_bdd")+"\\propertiesFile\\" + file_name
        print(prop_dir)
        self.config.read(prop_dir)

    def get_key(self, section, key_name):
        return self.config.get(section, key_name)
