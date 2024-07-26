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
SHEET = GSPREAD_CLIENT.open('margin-calculator')

margins = SHEET.worksheet('margins')

def get_bill_rate():
    """
    Get bill rate data from the user.
    run while loop to collect valid data from the user 
    via the terminal, which must be an integer. The loop will 
    repeatedly request data until the input is valid
    """
    while True:
        print("Please enter hourly bill rate data from client")
        print("Data should be in number format. No need to add '/h'")
        print("Example: 800 or 1000\n")

        bill_data = input('Enter Bill Rate here: \n')

        if validate_data(bill_data):
            print("Data input valid")
            break
    return bill_data
    get_contract_duration()

def get_contract_duration():
    """
    Get the contract duration from the user. 
    runs while loop to collect valid data from the user
    via the terminal, which must be an integer. The loop will 
    repeatedly request data until the input is valid
    """
    while True:
        print("Please enter the duration of the contract")
        print("Data should be in number format. No need to add 'months' etc.")
        print("Example: 6 or 12")

        contract_duration = input('Enter Contract Duration here: \n')

        if validate_data(contract_duration):
            print("Data input valid")
            break
    return contract_duration

start = get_bill_rate()
print(start)