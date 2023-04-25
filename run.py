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
        if values[0].isnumeric() == False:
            raise ValueError(f'Please provide a number for age')
            
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")    
        
    try:  
        if values[1] != ("Male" or "Female"):
            raise ValueError(f'Please provide a valid gender')
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        
    try:                
        if values[2] != ("salad" or "Noodle" or "sandwich" or "Fish and Chip"):
            raise ValueError(f'Please choose from the provided options')
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.")
        
    try:
        if values[3] != ("Yes" or "No"):
            raise ValueError(f'Please specify you willingness to buy again')   
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
    print(f'The number of people who wants to buy salad again is {number_salad}, male:{male_salad}, female:{female_salad}')
    
    fish_and_chip_result = SHEET.worksheet("fish_and_chip_sales").get_all_values()
    number_fish_and_chip = sum(num.count("Yes") for num in fish_and_chip_result) 
    male_fish_and_chip = sum(x.count("Male") for x in fish_and_chip_result)
    female_fish_and_chip = sum(y.count("Female") for y in fish_and_chip_result) 
    print(f'The number of people who wants to buy fish and chip again is {number_fish_and_chip}, male:{male_fish_and_chip}, female:{female_fish_and_chip}')

    sandwich_result = SHEET.worksheet("sandwich_sales").get_all_values()
    number_sandwich = sum(num.count("Yes") for num in sandwich_result)
    male_sandwich = sum(x.count("Male") for x in sandwich_result)
    female_sandwich = sum(y.count("Female") for y in sandwich_result) 
    print(f'The number of people who wants to buy sandwich again is {number_sandwich}, male:{male_sandwich}, female:{female_sandwich}')

    noodle_result = SHEET.worksheet("noodle_sales").get_all_values()
    number_noodle = sum(num.count("Yes") for num in noodle_result)
    male_noodle = sum(x.count("Male") for x in noodle_result)
    female_noodle = sum(y.count("Female") for y in noodle_result) 
    print(f'The number of people who wants to buy noodle again is {number_noodle}, male:{male_noodle}, female:{female_noodle}')


def main():
    """Run all programme function"""
    data = survey_input()
    lunch_survey_data = [i for i in "lunch_choice"]
    validate_survey(data)
    update_worksheet(data)
    Get_popular_product(data)
    update_salad_sales(data)
    update_Noodles_sales(data)
    update_sandwich_sales(data)
    update_Fish_and_Chip_sales(data)
    survey_result(data)
print("Welcome to Lunch Survery Data Automation\n")
main()