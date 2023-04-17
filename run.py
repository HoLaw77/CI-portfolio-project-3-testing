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
SHEET = GSPREAD_CLIENT.open('lunch_survey')


def survey_input():
    """
    Create input for user to input survey data
    """
    while True:
        print('It is an anonymous survey on lunch choice. we do not need to know your name.\n')
        print('But we need your age, gender, Food choice and are you willing to buy again\n')
        print('Food choice: Fish and Chip/Salad/Sandwich/Noodle\n')
        print('buy again: yes/no\n')

        age_input_str = input("Enter your age here:\n")
        gender_input_str = input("Enter your gender here:\n")
        Food_Choice_input_str = input("Enter your food choice here:\n")
        buy_again_input_str = input("Enter your if you will buy again here:\n")

        print(f' you are {age_input_str} years old\n')
        print(f' your gener is {gender_input_str}\n')
        print(f' your lunch choice is {Food_Choice_input_str}\n') 
        print(f' you answer {buy_again_input_str} for buying again\n')

        lunch_choice = []
        lunch_choice.append(age_input_str)
        lunch_choice.append(gender_input_str)
        lunch_choice.append(Food_Choice_input_str)
        lunch_choice.append(buy_again_input_str)
        print(lunch_choice)
        #for n in (age_input_str, gender_input_str, Food_Choice_input_str, buy_again_input_str):
        #    lunch_choice.append(n)
        print(lunch_choice)
        if validate_survey(lunch_choice):
            print("survey input valid.")
            break
    return lunch_choice

def validate_survey(values):
    """
    Test if each value type matches. String for gender, food_choice, buy_again_choice, and number for age in the try statement 
    """
    try: 
        if values["Age"].isnumeric() != True:
            raise ValueError(
                f'Exact number is required for age, you have entered {values["Age"]}'
                )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False      

    try:
        if values["Gender"] not in ("Male", "Female"):
            raise ValueError(
                f'You can only be either Male or Female, you have entered {values["Gender"]}'
            )      
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False
    
    try:
        if values["Food_Choice"] not in ("Fish and Chip", "Salad", "Sandwich", "Noodle"):
            raise ValueError(
                f'We are researching on the most common lunch type you can get on Tesco, you have chosen {values["Food_Choice"]}'
            )     
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False
    
    try:
        if values["Buy_Again_Choice"] not in ("Yes", "No"):
            raise ValueError(
                f'You can either say yes or no for buy again, you have chosen {values["Buy_Again_Choice"]}'
            )     
    except ValueError as e:
        print(f'Invalid data: {e}, please try again\n')
        return False
    return True

def update_worksheet(data):
    """
    Update google spreadsheet for survey input
    """
    survey_worksheet = SHEET.worksheet("sales")
    survey_worksheet.append_row(data)
    print("updating worksheet")
    print("Worksheet updated successfully.\n")


data = survey_input()
lunch_survey_data = [i for i in "lunch_choice"]
update_worksheet(data)