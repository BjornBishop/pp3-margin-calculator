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

def validate_bill_rate(bill_data):
    """
    Inside the TRY, converts the input data to an integer.
    Raise a ValueError if data cannot be converted
    or if multiple values are input.
    """
    try:
        int(bill_data)
    except ValueError as e:
        print(f'Invalid input {e}, please try again\n')
        return False
    return True

def validate_contract(contract_duration):
    """
    Inside the TRY, convert the input data into an integer. 
    Raise a ValueError if data can not be converted 
    or if multiple values are input
    """
    try:
        int(contract_duration)
    except ValueError as e:
        print(f'Invalid input {e}, please try again\n')
        return False
    return True

def validate_burdens(client_burdens):
    """
    inside the TRY, conver the input data into a floating integer.
    Raise a ValueError if data can not be converted
    or if multiple values are input
    """
    try:
        original_float = float(client_burdens)
        rounded_float = round(origin_float, 2)
        return rounded_float
    except ValueError as e:
        print('Invalid input {e}, please try again \n')
        return False
    return True

def get_bill_rate():
    """
    Get bill rate data from the user.
    Run a while loop to collect valid data from the user
    via the terminal, which must be an integer. The loop will
    repeatedly request data until the input is valid.
    """
    while True:
        print("Please enter hourly bill rate data from the client.")
        print("Data should be in number format. No need to add '/h'.")
        print("Example: 800 or 1000 \n")

        bill_data = input('Enter Bill Rate here: ')

        if validate_bill_rate(bill_data):
            print("Data input valid \n")
            break
    return bill_data

def get_contract_duration():
    """
    Get the contract duration from the user.
    Run a while loop to collect valid data from the user
    via the terminal, which must be an integer. The loop will
    repeatedly request data until the input is valid.
    """
    while True:
        print("Please enter the duration of the contract.")
        print("Data should be in number format. No need to add 'months' etc.")
        print("Example: 6 or 12 \n")

        contract_duration = input('Enter Contract Duration here: ')

        if validate_contract(contract_duration):
            print("Data input valid \n")
            break
    return contract_duration

def get_burdens():
    """
    Gets the associated burdens held with the client contract 
    Run a while loop to collect valid data from the user 
    via the terminal, which much be a float. The loop will 
    repeatedly request data until the input is valid 
    """
    print("Please enter the burdens held with the client.")
    print("data should be in number format, no need to add '%'")
    print("Example: 2.5")

    client_burdens = input('Enter Client Burdens here: ')

    if validate_burdens(client_burdens):
        print("Data input valid \n")
        break
    return client_burdens

def get_liabilities():
    """
    Gets the associated liabilities held with the client contract 
    Run a while loop to collect valid data from the user 
    via the terminal, which much be a float. The loop will 
    repeatedly request data until the input is valid 
    """
    print("Please enter the liabilities held with the client.")
    print("data should be in number format, no need to add '%'")
    print("Example: 2.5")

    company_liabilities = input('Enter Client Burdens here: ')

    if validate_liabilities(company_liabilities):
        print("Data input valid \n")
        break
    return company_liabilities


# Call the functions to start data collection
def main():
    """
    Main function holding queue of function for calculating margins
    """
    get_bill_rate()
    get_contract_duration()
    get_burdens()
    get_liabilities()

main()