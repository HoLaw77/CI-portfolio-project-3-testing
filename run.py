import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
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
        print('But we need your age, gender, Food choice and are you willing to buy again\n')
        print('Food choice: Fish and Chip/Salad/Sandwich/Noodle\n')
        print('buy again: yes/no\n')

        age_input_str = input("Enter your age here:\n")
        gender_input_str = input("Enter your gender here:\n")
        Food_Choice_input_str = input("Enter your food choice here:\n")
        buy_again_input_str = input("Enter your if you will buy again here:\n")
        
        print(f' you are {age_input_str} years old\n') 
        print(f' your gener is {gender_input_str}\n')
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
       # if validate_survey(lunch_choice):
        #    print("survey input valid.")
        break

    return lunch_choice

def validate_survey(values):
    """
    Test if each value type matches. String for gender, food_choice, buy_again_choice, and number for age in the try statement 
    """
    try:
        [int(value) for value in values]
        raise ValueError(f'Please answer all questions required.')

    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        
        



def update_worksheet(data):
    """
    Update google spreadsheet for survey input
    """
    survey_worksheet = SHEET.worksheet("sales")
    survey_worksheet.append_row(data)
    print("updating worksheet")
    print("Worksheet updated successfully.\n")

def Get_popular_product(data):
    """
    Get popular product from the buy_again_input and compare with food_choice_input
    """
    print('Sales survey result processing...')
    sales = SHEET.worksheet("sales").get_all_values()
    salad_sales = SHEET.worksheet("salad_sales").get_all_values()
    fish_and_chip_sales = SHEET.worksheet("fish_and_chip_sales").get_all_values()
    noodle_sales = SHEET.worksheet("noodle_sales").get_all_values()
    sandwich_sales = SHEET.worksheet("sandwich_sales").get_all_values()
    pprint(sales)

def import_salad_sales(data):
    """
    import sales data limited to salad to worksheet
    """
    for x in data[3]:
        if x == "salad":
           print(x)    


def main():
    """Run all programme function"""
    data = survey_input()
    lunch_survey_data = [i for i in "lunch_choice"]
    update_worksheet(data)
    Get_popular_product(data)
    import_salad_sales(data)
print("Welcome to Lunch Survery Data Automation\n")
main()