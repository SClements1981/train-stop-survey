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

    print("\nThank you for taking part in our Train Stop Survey.\n")
    print("You will now be asked a few quetsions about your experiance.\n")
    print("Did you use the train today for, business or lesiure?")

    data_str = input("Please answer Business or Lesiure here: ")
    print(f"Thank you, you answered {data_str}\n")

    print("Please answer the following questions from 1-5, separated by commas.")
    print("1 being very dissatisfied, 3 neither and 5 being satisfied.\n")
    print("Example: 4,3,1,2,5\n")

    print("Question 1: Overall satisfaction of the train.")
    print("Question 2: Punctuality and relability of service.")
    print("Question 3: Value for money.")
    print("Question 4: Level of crowding on the train.")
    print("Question 5: Frequency of the trains on route.\n")

    data_questions = input("Please provide your answers here: ")
    print(f"Thank you for your feedback you answered {data_questions}")

get_survey_data()