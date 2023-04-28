import gspread
from google.oauth2.service_account import Credentials
from statistics import mean
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('lunch_survey')


def survey_input():
    """
    Create input for user to input survey data
    """
    while True:
        print('It is an anonymous survey on lunch choice.\n')
        print('We need your age, gender, food choice and will you buy later\n')
        print('Food choice: Fish and Chip/Salad/Sandwich/Noodle\n')
        print('buy again: yes/no\n')

        age_input_str = input("Enter your age here:\n")
        while age_input_str.isnumeric() is not True:
            age_input_str = input("Error, please provide a number for age:")
        gender_input_str = input("Enter your gender here: male or female\n")
        while gender_input_str not in ("male", "female"):
            gender_input_str = input("Error, please enter your gender again:")
        food_choice_input_str = input("Enter your food choice: salad, noodle, sandwich, fish and chip\n")
        while food_choice_input_str not in ("salad", "noodle", "sandwich", "fish and chip"):
            food_choice_input_str = input("Error, please enter the provided food choice")
        buy_again_input_str = input("Enter your if you will buy again here: yes or no\n")
        while buy_again_input_str not in ("yes", "no"):
            buy_again_input_str = input("Error, please specify your choice of buy again:\n")
        print(f' you are {age_input_str} years old\n') 
        print(f' your gener is {gender_input_str}\n')
        print(f' your lunch choice is {food_choice_input_str}\n') 
        print(f' you answer {buy_again_input_str} for buying again\n')
        
        lunch_choice = []
        lunch_choice.append(age_input_str)
        lunch_choice.append(gender_input_str)
        lunch_choice.append(food_choice_input_str)
        lunch_choice.append(buy_again_input_str)
        print(lunch_choice)
        print(lunch_choice)
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


def update_Noodles_sales(data):
    """
    import sales data limited to noodles to worksheet
    """
    if data[2] == "Noodle":
        noodle_sheet = SHEET.worksheet("noodle_sales")
        noodle_sheet.append_row(data)
        print("noodle_sales sheet successfully updated")
    

def update_salad_sales(data):
    """
    import sales data limited to salad to worksheet
    """
    if data[2] == "salad":
        salad_sheet = SHEET.worksheet("salad_sales")
        salad_sheet.append_row(data)
        print("salad_sales sheet successfully updated")


def update_sandwich_sales(data):
    """
    import sales data limited to sandwich to worksheet
    """
    if data[2] == "sandwich":
        sandwich_sheet = SHEET.worksheet("sandwich_sales")
        sandwich_sheet.append_row(data)
        print("sandwich_sales sheet successfully updated")


def update_Fish_and_Chip_sales(data):
    """
    import sales data limited to Fish and Chips to worksheet
    """
    if data[2] == "Fish and Chip":
        fish_and_chip_sheet = SHEET.worksheet("fish_and_chip_sales")
        fish_and_chip_sheet.append_row(data)
        print("fish_and_chip_sales sheet successfully updated")


def survey_result(data):
    """
    Count the number of each food choice and print the result in console
    """
    salad_result = SHEET.worksheet("salad_sales").get_all_values()
    number_salad = sum(num.count("Yes") for num in salad_result)
    male_salad = sum(x.count("Male") for x in salad_result)
    female_salad = sum(y.count("Female") for y in salad_result)
    ages = SHEET.worksheet("salad_sales").get("A2:A99")
    # Flatten the list and convert strings to integers
    flat_ages = [int(age) for sublist in ages for age in sublist]
    # Now calculate the mean
    average_age = int(mean(flat_ages))
    print(f'Buy salad again: {number_salad}, male:{male_salad}, female:{female_salad}, average-age: {average_age}')
    
    fish_and_chip_result = SHEET.worksheet("fish_and_chip_sales").get_all_values()
    number_fish_and_chip = sum(num.count("Yes") for num in fish_and_chip_result) 
    male_fish_and_chip = sum(x.count("Male") for x in fish_and_chip_result)
    female_fish_and_chip = sum(y.count("Female") for y in fish_and_chip_result)
    ages = SHEET.worksheet("fish_and_chip_sales").get("A2:A99")
    # Flatten the list and convert strings to integers
    flat_ages = [int(age) for sublist in ages for age in sublist]
    # Now calculate the mean
    average_age = int(mean(flat_ages)) 
    print(f'Buy fish and chip again:{number_fish_and_chip}, male:{male_fish_and_chip}, female:{female_fish_and_chip}, average_age: {average_age}')

    sandwich_result = SHEET.worksheet("sandwich_sales").get_all_values()
    number_sandwich = sum(num.count("Yes") for num in sandwich_result)
    male_sandwich = sum(x.count("Male") for x in sandwich_result)
    female_sandwich = sum(y.count("Female") for y in sandwich_result) 
    ages = SHEET.worksheet("sandwich_sales").get("A2:A99")
    # Flatten the list and convert strings to integers
    flat_ages = [int(age) for sublist in ages for age in sublist]
    # Now calculate the mean
    average_age = int(mean(flat_ages)) 
    print(f'Buy sandwich again:{number_sandwich}, male:{male_sandwich}, female:{female_sandwich}, age: {average_age}')

    noodle_result = SHEET.worksheet("noodle_sales").get_all_values()
    number_noodle = sum(num.count("Yes") for num in noodle_result)
    male_noodle = sum(x.count("Male") for x in noodle_result)
    female_noodle = sum(y.count("Female") for y in noodle_result) 
    ages = SHEET.worksheet("noodle_sales").get("A2:A99")
    # Flatten the list and convert strings to integers
    flat_ages = [int(age) for sublist in ages for age in sublist]
    # Now calculate the mean
    average_age = int(mean(flat_ages)) 
    print(f'Buy noodle again{number_noodle} male:{male_noodle}, female:{female_noodle}, average-age:{average_age}')


def main():
    """Run all programme function"""
    data = survey_input()
    update_worksheet(data)
    update_salad_sales(data)
    update_Noodles_sales(data)
    update_sandwich_sales(data)
    update_Fish_and_Chip_sales(data)
    survey_result(data)
    survey_end = True
    while survey_end:
        ask = input("Do you want to resubmit? yes or no \n")
        if ask == "yes":
            main()
        if ask == "no":
            survey_end = False
            print("Thanks for joining, have a good day.")


print("Welcome to Lunch Survery Data Automation\n")
main()
