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

#business = SHEET.worksheet('business')
#business_data = business.get_all_values()

def get_survey_data():
    """
    Get survey data for the user
    """

    print("\nThank you for taking part in our Train Stop survey.\n")
    print("You will now be asked a few quetsions about your experiance.\n")
    print("Question 1:")
    print("Did you use the train today for, business or lesiure?")

    data_str = input("Please answer Business or Lesiure here: ")
    print(f"The answer you proved was {data_str}")

get_survey_data()