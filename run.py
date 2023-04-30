"""
Install statistics, gspread and google.oauth
"""
from statistics import mean
import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
try:
    SHEET = GSPREAD_CLIENT.open('lunch_survey')
except:
    SHEET = GSPREAD_CLIENT.create('lunch_survey')


def survey_input():
    """
    Create input for user to input survey data
    """
    while True:
        print('It is an anonymous survey on lunch choice.\n')
        print('We need your age, gender, food choice and will you buy later\n')
        print('Food choice: fish and chip/salad/sandwich/noodle\n')

        age_input_str = input("Enter your age here:\n")
        while age_input_str.isnumeric() is not True:
            age_input_str = input("Error, please provide a number for age:\n")
        gender_input_str = input("Enter your gender here: male or female\n")
        while gender_input_str.lower() not in ("male", "female"):
            gender_input_str = input("Error, please re-enter your gender:\n")
        food_choice_input_str = input(
            "Enter your food choice: salad, noodle, sandwich, fish and chip\n")
        while food_choice_input_str.lower() not in (
                "salad", "noodle", "sandwich", "fish and chip"):
            food_choice_input_str = input(
                "Error, please enter the provided food choice\n")
        buy_again_input_str = input(
            "Enter your if you will buy again here: yes or no\n")
        while buy_again_input_str.lower() not in ("yes", "no"):
            buy_again_input_str = input(
                "Error, please specify your choice of buy again:\n")
        print(f'you are {age_input_str} years old\n')
        print(f'your gender is {gender_input_str}\n')
        print(f'your lunch choice is {food_choice_input_str}\n')
        print(f'you answer {buy_again_input_str} for buying again\n')

        lunch_choice = []
        lunch_choice.append(age_input_str)
        lunch_choice.append(gender_input_str.lower())
        lunch_choice.append(food_choice_input_str.lower())
        lunch_choice.append(buy_again_input_str.lower())
        break

    return lunch_choice


def update_worksheet(data):
    """
    Update google spreadsheet for survey input
    """
    survey_worksheet = SHEET.worksheet("sales")
    survey_worksheet.append_row(data)
    print("updating worksheet")
    print("Worksheet updated successfully.\n")


def update_noodles_sales(data):
    """
    import sales data limited to noodles to worksheet
    """
    if data[2].lower() == "noodle":
        noodle_sheet = SHEET.worksheet("noodle_sales")
        noodle_sheet.append_row(data)
        print("noodle_sales sheet successfully updated")


def update_salad_sales(data):
    """
    import sales data limited to salad to worksheet
    """
    if data[2].lower() == "salad":
        salad_sheet = SHEET.worksheet("salad_sales")
        salad_sheet.append_row(data)
        print("salad_sales sheet successfully updated")


def update_sandwich_sales(data):
    """
    import sales data limited to sandwich to worksheet
    """
    if data[2].lower() == "sandwich":
        sandwich_sheet = SHEET.worksheet("sandwich_sales")
        sandwich_sheet.append_row(data)
        print("sandwich_sales sheet successfully updated")


def update_fish_and_chip_sales(data):
    """
    import sales data limited to Fish and Chips to worksheet
    """
    if data[2].lower() == "fish and chip":
        fish_and_chip_sheet = SHEET.worksheet("fish_and_chip_sales")
        fish_and_chip_sheet.append_row(data)
        print("fish_and_chip_sales sheet successfully updated")


def survey_result():
    """
    Count the number of each food choice and print the result in console
    """
    salad_result = SHEET.worksheet("salad_sales").get_all_values()
    number_salad = sum(num.count("Yes") for num in salad_result)
    male_salad = sum(x.count("Male") for x in salad_result)
    female_salad = sum(y.count("Female") for y in salad_result)
    ages = SHEET.worksheet("salad_sales").get("A2:A2000")
    # Flatten the list and convert strings to integers, advised by Tutor of CI
    num_ages = [int(age) for sublist in ages for age in sublist]
    # Now calculate the mean, advised by Tutor of CI
    average_age = int(mean(num_ages))
    # Print the satistics user who choose salad 
    print(
        f'Buy salad again: {number_salad}, '
        f'male: {male_salad}, '
        f'female: {female_salad}, '
        f'average-age: {average_age}')

    fish_and_chip_result = SHEET.worksheet(
        "fish_and_chip_sales").get_all_values()
    number_fish_and_chip = sum(num.count("Yes")
                               for num in fish_and_chip_result)
    male_fish_and_chip = sum(x.count("Male") for x in fish_and_chip_result)
    female_fish_and_chip = sum(y.count("Female") for y in fish_and_chip_result)
    ages = SHEET.worksheet("fish_and_chip_sales").get("A2:A99")
    num_ages = [int(age) for sublist in ages for age in sublist]
    average_age = int(mean(num_ages))
    # Print the satistics user who choose fish and chip 
    print(
        f'Buy fish and chip again: {number_fish_and_chip}, '
        f'male: {male_fish_and_chip}, '
        f'female: {female_fish_and_chip}, '
        f'average_age: {average_age}')

    sandwich_result = SHEET.worksheet("sandwich_sales").get_all_values()
    number_sandwich = sum(num.count("Yes") for num in sandwich_result)
    male_sandwich = sum(x.count("Male") for x in sandwich_result)
    female_sandwich = sum(y.count("Female") for y in sandwich_result)
    ages = SHEET.worksheet("sandwich_sales").get("A2:A99")
    num_ages = [int(age) for sublist in ages for age in sublist]
    average_age = int(mean(num_ages))
    # Print the satistics user who choose sandwich 
    print(
        f'Buy sandwich again: {number_sandwich}, '
        f'male: {male_sandwich}, '
        f'female: {female_sandwich}, '
        f'average-age: {average_age}')

    noodle_result = SHEET.worksheet("noodle_sales").get_all_values()
    number_noodle = sum(num.count("Yes") for num in noodle_result)
    male_noodle = sum(x.count("Male") for x in noodle_result)
    female_noodle = sum(y.count("Female") for y in noodle_result)
    ages = SHEET.worksheet("noodle_sales").get("A2:A99")
    num_ages = [int(age) for sublist in ages for age in sublist]
    average_age = int(mean(num_ages))
    # Print the satistics user who choose noodle
    print(
        f'Buy noodle again: {number_noodle}, '
        f'male: {male_noodle}, '
        f'female: {female_noodle}, '
        f'average-age: {average_age}')


def main():
    """Run all programme function"""
    data = survey_input()
    update_worksheet(data)
    update_salad_sales(data)
    update_noodles_sales(data)
    update_sandwich_sales(data)
    update_fish_and_chip_sales(data)
    survey_result()
    survey_end = True
    while survey_end:
        ask = input("Do you want to resubmit? yes or no \n")
        if ask == "yes":
            main()
        if ask == "no":
            survey_end = False
            print("Thanks for joining, have a good day.")


print("Welcome to Lunch Survey Data Automation\n")
main()
