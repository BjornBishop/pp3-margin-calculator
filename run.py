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
deals = SHEET.worksheet('deals')

ideal_margin = 0.85

def validate_bill_rate(new_bill_data):
    """
    Inside the TRY, converts the input data to an integer.
    Raise a ValueError if data cannot be converted
    or if multiple values are input.
    """
    try:
        int(new_bill_data)
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
        rounded_float = round(original_float, 2)
        return rounded_float
    except ValueError as e:
        print(f'Invalid input {e}, please try again \n')
        return False
    return True

def validate_liabilities(company_liabilities):
    """
    inside the TRY, convert the input data into a floating integer.
    Raise a ValueError if data can not be converted
    or if multiple values are input
    """
    try:
        original_float = float(company_liabilities)
        rounded_float = round(original_float, 2)
        return rounded_float
    except ValueError as e:
        print(f'Invalid input {e}, please try again \n')
        return False
    return True

def validate_deal(save_contract_value):
    """
    within the TRY there is an IF statement that checks if the input is Y or N. 
    if Y - the contract value is saved to "deals" worksheet. 
    if N - the values are discarded. 
    """
    try:
        if save_contract_value == "Y":
            save_contract_selected = None
            return True
        elif save_contract_value == "N":
            print(f'Contract value discarded \n')
            pass
        else:
            raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
    except ValueError as e:
        print(f'Invalid input: {e}. Please try again. \n')
        return False


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

        new_bill_data = input('Enter Bill Rate here: ')

        if validate_bill_rate(new_bill_data):
            print("Data input valid \n")
            break
    return new_bill_data

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
    while True:
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
    while True:
        print("Please enter the liabilities held with the client.")
        print("data should be in number format, no need to add '%'")
        print("Example: 2.5")

        company_liabilities = input('Enter Company Liabilities here: ')

        if validate_liabilities(company_liabilities):
            print("Data input valid \n")
            break
    return company_liabilities

def save_contract():
    """
    Asks the user if the calculated deal value should be saved or discarded.
    Runs a WHILE loop to collect valid data from the user via the terminal.
    The loop will repeat the request until valid input is entered.
    """
    while True:
        print("Would you like to save the calculated contract value?")
        print("If 'No', the calculation will be discarded \n")
        save_contract_value = input("Y/N: ")
        if validate_deal(save_contract_value):
            print(f'Contract value saving... \n')
            break
    return save_contract_value

def calculate_pay_rate(new_bill_data, ideal_margin):
    try:
        bill_rate = float(new_bill_data)  
    except ValueError:
        print("Invalid input. Please enter a valid numeric bill rate.")
        return None

    pay_rate = bill_rate * ideal_margin
    print(f"Pay rate calculated at: {pay_rate:.2f}")
    return pay_rate

def calculate_deal_value(new_bill_data, contract_duration):
    """
    Calculates the total value of the contract based on the bill rate multiplied by the contract duration
    """
    bill_int = int(new_bill_data)
    contract_int = int(contract_duration)
    contract_value = bill_int * contract_int
    print(f'Total deal value calculated: {contract_value}')
    return contract_value

def update_worksheet_bill(data, worksheet):
    """
    Updates the worksheet with the input data to worksheet: margins column: bill.
    """
    print(f'Updating worksheet: {worksheet}...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row([int(data)])
    print(f'Worksheet {worksheet} updated successfully \n')

def update_worksheet_contract(data, worksheet):
    """
    Updates the worksheet with the input data to worksheet: margins column: duration.
    """
    print(f'Updating worksheet: {worksheet}...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row_index = len(worksheet_to_update.col_values(1))
    worksheet_to_update.update_cell(last_row_index, 2, int(data))
    print(f'Worksheet {worksheet} updated successfully \n')

def update_worksheet_burden(data, worksheet):
    """
    updates the worksheet with the burden data to worksheet: margins, column: burdens
    """
    print(f'Updating worksheet: {worksheet}...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row_index = len(worksheet_to_update.col_values(1))
    worksheet_to_update.update_cell(last_row_index, 3, float(data))
    print(f'Worksheet {worksheet} updated successfully \n')

def update_worksheet_liabilities(data, worksheet):
    """
    updates the worksheet with the liabilities data to worksheet: margins, column: liabilities
    """
    print(f'Updating worksheet: {worksheet}...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row_index = len(worksheet_to_update.col_values(1))
    worksheet_to_update.update_cell(last_row_index, 4, float(data))
    print(f'Worksheet {worksheet} updated successfully \n')

def update_worksheet_pay(data, worksheet):
    """
    Updates the worksheet with the pay rate calculated into worksheet: margins, Column: pay rate
    """
    print(f'Updating worksheet: {worksheet}...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row_index = len(worksheet_to_update.col_values(1))
    worksheet_to_update.update_cell(last_row_index, 5, int(data))
    print(f'Worksheet {worksheet} updated')

def update_worksheet_value(data, worksheet):
    """
    Updates the worksheet with the calculated deal value into worksheet: deals, column: contract value
    """
    print(f'saving deal to workseet...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row([int(data)])
    print(f'Deal saved to worksheet: {worksheet}')


# Call the functions to start data collection
def main():
    """
    Main function holding queue of function for calculating margins
    """
    new_bill_data = get_bill_rate()
    update_worksheet_bill(new_bill_data, "margins")
    contract_duration = get_contract_duration()
    update_worksheet_contract(contract_duration, "margins")
    client_burdens = get_burdens()
    update_worksheet_burden(client_burdens, "margins")
    company_liabilities = get_liabilities()
    update_worksheet_liabilities(company_liabilities, "margins")
    pay_rate = calculate_pay_rate(new_bill_data, ideal_margin)
    update_worksheet_pay(pay_rate, "margins")
    contract_value = calculate_deal_value(new_bill_data, contract_duration)
    save_contract_selected = update_worksheet_value(contract_value, "deals")
    save_contract()

if __name__ == "__main__":
    main()
