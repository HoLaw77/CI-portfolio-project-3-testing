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

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

def survey_input():
    """
    Create input for user to input survey data
    """
    while True:
        print('It is an anonymous survey on lunch choice. we do not need to know your name.')
        print('But we need your age, gender, Food choice and are you willing to buy again')
        print('Food choice: Fish and Chip/Salad/Sandwich/Noodle')
        print('buy again: yes/no')

        age_input_str = input("Enter your age here:\n")
        gender_input_str = input("Enter your gender here:\n")
        Food_Choice_input_str = input("Enter your food choice here:\n")
        buy_again_input_str = input("Enter your if you will buy again here:\n")

        print(f' you are {age_input_str} years old')
        print(f' your gener is {gender_input_str}')
        print(f' your lunch choice is {Food_Choice_input_str}') 
        print(f' you answer {buy_again_input_str} for buying again')
    
survey_data = survey_input()
print(survey_data)