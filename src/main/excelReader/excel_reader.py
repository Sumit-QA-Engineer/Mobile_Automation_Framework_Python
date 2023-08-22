import openpyxl

from src.main.utilities.propertiesReader import get_main_project_directory


def excel_reader(file_name):
    test_data = []
    workbook = openpyxl.load_workbook(get_main_project_directory("MobileAutomation(POM)")+"//data//"+file_name)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_data.append(row)

    return test_data
