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
            save_weekly_spread = None
            return True
        elif save_contract_value == "N":
            print(f'Contract value discarded \n')
            return False
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

        new_bill_data = input('Enter Bill Rate here: \n')

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

        contract_duration = input('Enter Contract Duration here: \n')

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

        client_burdens = input('Enter Client Burdens here: \n')

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
        print("If standard T&M contract Liabilities = 0")
        print("If service contract Liabilities = X.XX")

        company_liabilities = input('Enter Company Liabilities here: \n')

        if validate_liabilities(company_liabilities):
            print("Data input valid \n")
            break
    return company_liabilities

# function commented out as following up function requires additional time and logic. 
#def get_total_spread():
#    """
#    Function to get the total amount of weekly spread
#    """
#    deals_worksheet = SHEET.worksheet('deals')
#    spread_column = deals_worksheet.col_values(2)
#    spread_values = [float(value) for value in spread_column if value]
#    total_spread = sum(spread_values)
#    return total_spread

def save_contract():
    """
    Asks the user if the calculated deal value should be saved or discarded.
    Runs a WHILE loop to collect valid data from the user via the terminal.
    The loop will repeat the request until valid input is entered.
    """
    while True:
        print("Would you like to save the calculated contract value?")
        print("If 'No', the calculation will be discarded \n")
        save_contract_value = input("Y/N: \n")
        if validate_deal(save_contract_value):
            print(f'Contract value saving... \n')
            break
    return save_contract_value

def calculate_pay_rate(new_bill_data, ideal_margin):
    """
    function to alculate the pay rate a consultant can take with a given contract. 
    calculation is done based on new_bill_data multiplied by the ideal margins (15%)
    """
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
    hourly_contract = contract_int * 160
    contract_value = bill_int * hourly_contract
    print(f'Total deal value calculated: {contract_value} \n')
    return contract_value

def calculate_margin(client_burdens, company_liabilities):
    """
    Function to calculate the what margins are required which is used to calculate the weekly spread 
    client_burdens and company_liabilities are converted into floats and rounded to 2 decimal places 
    rounded_burden is added to rounded_liabilities and 100 is added. 
    the figure is then divided by 100 in order to get the correct margin amount.
    """
    burden_float = float(client_burdens)
    rounded_burden = round(burden_float, 2)
    liabilities_float = float(company_liabilities)
    rounded_liabilities = round(liabilities_float, 2)
    second_margin = (rounded_burden + rounded_liabilities) + 100
    final_margin = second_margin / 100
    return final_margin

def calculate_weekly_spread(final_margin, new_bill_data, pay_rate):
    """
    calculates the weekly spread by converting final_margin, new_bill_data and pay_rate 
    into floats and rounds them to 2 decimal places. 
    rounded_margin is subtracted from rounded_bill which is multiplied by rounded_pay
    and then multipled by 40 to indicate 40 hours in a week. 
    """
    margin_float = float(final_margin)
    rounded_margin = round(margin_float, 2)
    bill_float = float(new_bill_data)
    rounded_bill = round(bill_float, 2)
    pay_float = float(pay_rate)
    rounded_pay = round(pay_float, 2)
    weekly_spread = (rounded_bill-(rounded_margin)*rounded_pay)*40
    return weekly_spread

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
    print(f'Saving deal to workseet...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row([int(data)])
    print(f'Deal saved to worksheet: {worksheet} \n')

def update_weekly_spread(data, worksheet):
    """
    updates the worksheet with the calculated weekly spread into worksheet: deals, column: weekly spread
    """
    print(f'Updating worksheet: {worksheet}')
    worksheet_to_update = SHEET.worksheet(worksheet)
    last_row_index = len(worksheet_to_update.col_values(1))
    worksheet_to_update.update_cell(last_row_index, 2, float(data))
    print(f'Weekly spread saved to {worksheet}')

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
    final_margin = calculate_margin(client_burdens, company_liabilities)
    weekly_spread = calculate_weekly_spread(final_margin, new_bill_data, pay_rate)
    save_weekly_spread = update_weekly_spread(weekly_spread, "deals")
    save_contract()

if __name__ == "__main__":
    main()
