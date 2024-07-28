![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Contract Weekly Spread Calculator
This app is meant to be a margins calculator used by business professionals to quickly calculate and store data pertaining 
to contract values.

## Enter Bill Rate 
First the user is prompted to input the bill rate that is provided by the client. This data is stored automatically in a separate spreadsheet called "margins calculator" in googlesheets and stores the data row after row in the same column "bill rate" 

The bill rate is validated with the validate_bill_rate function which ensures that the input data is a number and not a string. 
If a string is entered, a ValueError is thrown and the question is repeated until valid data is input. 

## Enter Contract Duration
Second step, the user is prompted to input the contract duration provided by the client. This data is stored automatically in a separate spreadsheet called "margins calculator" in googlesheets and stores the data row after row in the same column, "comtract duration". 

The contract duration is validated with the validate_contract_duration function which ensures the input data is a number and not a string. If a string is entered, a ValueError is thrown and the question is repeated until valid data is input. 

## Enter Burdens 
Third step, the user is prompted to input the burdens of the contract. Burdens are typically known by the business professionals as it is outlined in the overall suppliers contract with the client. These values are stored automatically in a separate spreadsheet called "margins calculator" in googlesheets and stores the data row after row in the same column, "burdens". 

The burdens are validated with the "validate burdens" function which ensures the input data is a number and not a string. The number is converted into a float as typically burdens hold decimal places. The float is rounded using a round() function as decimal places beyond that point are insignificant. 

If a string is entered, a ValueError message is thrown and the question is repeated until valid data is input. 

## Enter Liabilities
Fourth step, the user is prompted to input the liabilities of the contract. This is typically based on the type of delivery required by the clients. These values are stored automatically in a separate spreadsheet called "margins calculator" in googlesheets and stores the data row after row in the same column, "liabilities" 

The liabilities are validated with the validate_liabilities function which ensures the input data is a number and not a string. The input data is converted into a float and rounded to 2 decimal places as beyond 2 decimal places, the data is insignificant. 

If a string is entered, a ValueError message is thrown and the question is repeated until valid data is input.

## Calculate Pay Rate 
using the input bill rate provided by the client, the pay rate is calculated by taking the bill rate multiplied by the ideal margins (0.85).

both the bill rate and ideal margins are converted into floats in order for the calculation to function properly. 

This function needs some additional work as using a static "ideal_margins" is not infact, ideal. Later I would like to use the input burden and liabilities to calculate the actual pay rates. 

The returned data is automaticall stored in the separate worksheet "margins-calculator" row after row in the same column "pay rate"

## Calculating the contract value
Using the bill rate and the contract duration, the contract value is created. Both bill rate and contract duration are converted into integers. The contract duration is then multiplied by 160 (the amount of hours in 1 month). 

The new contract duration which is now in hours is multiplied by the bill rate to provide a total deal value. 

The value is returned in the terminal but is not stored. 

### Save Contract 
Once the contract value is calculated and posted to the terminal, the user is prompted if they would like to save the contract to the spreadsheet. The user must input either "Y" or "N". 

The input is validated using an IF statement where the system checks if the input data is a string with either "Y" or "N". If the input data is invalid a ValueError message is thrown and the question repeated. 

(For some reason I cant get the program to terminate if the input data is "N")

If "Y" is entered, the contract data is saved to the spreadsheet "margins-calculator" in worksheet "deals" under the column "contract value" row after row. 

## Margins calculated 
Once the contract is saved, the margins are calculated. Here the burdens and liabilities are converted into floats and rounded to 2 decimal places. It is rounded to only 2 decimal places as beyond that point, the data is irrelevant. 

The rounded floats are then added together and then added to 100. This is then divided by 100 to provide a 2 decimal place float which can be used in a later function. 

The values are not stored anywhere as this data is not relevant to keep. 

## Calculate Weekly Spread 
Once the Margins are calculated, the final margins, bill_rate and pay_rate are used to calculate the weekly spread. 

all values are converted into floats and rounded to 2 decimal places. they are rounded to 2 decimal places as beyond this point, the data is irrelevant. 

the rounded bill rate as the rounded margins subtracted and then multiplied by the rounded pay rate. This is then multiplied by 40 (the average amount of workin hours in a week) to provide the weekly sread amount. 

The data is then saved along with the contract value in the googlesheet "margins calculator" in worksheet "deals", row after row in column "weekly spread"

## Deployment 
The app was deployed using Heroku. 

The steps I took were as follows: 
- I created a new app in Heroku. 
- within the settings, i chose the app name "weekly-spread-calculator-pp3"
- within the "Reveal config vars" i pasted in the CREDS.JSON contents & PORT 8000. 
- 2 Buildpacks were added, "python" and "node.js" 
- within the deploy sector, GitHub was selected as the deployment method
- I decided to deploy manually rather than automatically as I plan to continue to modify the application and do not want to break the deployed version while I continue to add more complex logic
- the requirements.txt file was updated using the pip3 freeze > requirements.txt in the terminal. 

## Credits
No external material was used in the making of this program. Some logic was aided by the use of co-pilot, however, this could only be done with segments of code already written rather than having the AI assistant actually write any code. 
