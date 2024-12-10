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
    while True:
        print("\nThank you for taking part in our Train Stop Survey.\n")
        print("You will now be asked a few questions about your experience.\n")
        print("Did you use the train today for business or leisure?")

        opening_data = input("Please answer business or leisure here: ")

        if validate_opening_question(opening_data):
            print("Your answer are valid, please move onto the next section.")
            break

    return opening_data

def validate_opening_question(answer):
    print(answer)
    """
    Check to see if opening question is correct, either business or leisure.
    """
    if answer not "business" or not "leisure":
        print("Please choose either, business or leisure") 
    else:
        return True

#def get_survey_data():
#    """
#    Get survey data from customer input.
#    """
#    while True:
#        print("\nThank you for taking part in our Train Stop Survey.\n")
#        print("You will now be asked a few questions about your experience.\n")
#        print("Please answer the following questions giving them a rating from 1-5.")
#        print("1 being very dissatisfied, 3 neither and 5 being satisfied.\n")
#        print("Please separate your answers with a commas. Example: 4,3,1,2,5,5\n")

#        print("Question 1: Overall satisfaction of the train.")
#        print("Question 2: Punctuality and reliability of service.")
#        print("Question 3: Value for money.")
#        print("Question 4: Level of crowding on the train.")
#        print("Question 5: Comfort of seats.")
#        print("Question 6: Frequency of the trains on route.\n")

#        data_str = input("Enter your data here: ")
#        survey_data = data_str.split(",")
        
#        if validate_data(survey_data):
#            print("Your answers are valid")
#            break
    
#    return survey_data

#def validate_data(values):
#    """
#    Check to see if questionnaire data is correct and converted to an int, raise error if string 
#    is incorrect and not between numbers 1-5.
#    """
#    try:
#        [int(value) for value in values]
#        if len(values) != 6:
#            raise ValueError(f"Exactly 6 values are required, you entered {len(values)}")
#    except ValueError as e:
#        print(f"Invalid data: {e}, please try again.\n")
#        return False
#    return True


get_opening_survey_data()
