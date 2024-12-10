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


def get_opening_survey_data():
    """
    Get survey data for the user
    """
    
    print("\nThank you for taking part in our Train Stop Survey.\n")
    print("You will now be asked a few questions about your experience.\n")
    print("First of all we would like to know if you used the train today for business or leisure?")

    opening_question = input("Please answer business or leisure here: ")
    validate_opening_question(opening_question)

def validate_opening_question(answer):
    try:
        answers = answer
        if answer == "business" or "leisure":
            raise ValueError(f"Please answer either business or leisure.")
    except ValueError as e:
        print(f"Invalid data: {e}")
        print(answer)



get_opening_survey_data()    

