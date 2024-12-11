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
SHEET = GSPREAD_CLIENT.open('train_stop_survey')


def get_survey_data():
    """
    Get survey data for the user
    """
    
    print("\nThank you for taking part in our Train Stop Survey.\n")
    print("You will now be asked a few questions about your experience.\n")

    while True:
        print("Please answer the below 6 questions giving them a rating from 1-5.")
        print("1 very dissatisfied, 2 dissatisfied 3 neither, 4 satisfied, 5 very satisfied.\n")
        print("Please separate your answers with a commas. Example: 4,3,1,2,5,5\n")

        print("Question 1: Overall satisfaction of the train.")
        print("Question 2: Punctuality and reliability of service.")
        print("Question 3: Value for money.")
        print("Question 4: Level of crowding on the train.")
        print("Question 5: Comfort of seats.")
        print("Question 6: Frequency of the trains on route.\n")

        survey_str = input("Enter your answers here: ")
        
        survey_data = survey_str.split(",")
        validate_survey(survey_data)

        if validate_survey(survey_data):
            print("The answers you provided are valid, thank you for your feedback.")
            break

    return survey_data


def validate_survey(answers):
    """
    Check to see if questionnaire data is correct and converted to an int, raise error if string 
    is incorrect and not between numbers 1-5.
    """
    try:
        [int(answer) for answer in answers]
        if len(answers) != 6:
            raise ValueError(f"We require all 6 questions to be answered, you answered {len(answers)}")
#        if answers <= 0 or answers >= 6:
#            raise ValueError(f"Please make sure your answers are between 1-5.")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_survey_data(data):
    """
    Update survey work sheet.
    """
    print("Updating survey worksheet...\n")
    survey_worksheet = SHEET.worksheet("survey")
    survey_worksheet.append_row(data)
    print("Survey worksheet has now been updated.\n")


data = get_survey_data()    
survey_data = [int(num) for num in data]
update_survey_data(survey_data)