# Stock_Noti Microservice

## Introduction
This microservice returns an alert whenever a specified stock reaches a specified price threshold.

## Requirements
- Python 3.x
- Flask
- Requests

## Installation and Setup
1. Clone the repository or download it as a zip
2. Navigate to the directory where the repository is installed
3. Install the required packages

## Running the Program
Run the program with the command: 'python noti_service.py'
The program will be found at 'http://127.0.0.1:5000/set_alert'

## How to REQUEST data from noti_service:
Set an app url variable in your own app to the url for noti_service
(this can be 'http://127.0.0.1:5000/set_alert' if running locally)

Create a data structure with the 'stock_name' and 'target_price' variables, and set the values to your desired stock name and target price
Example:
data = {
    'stock_name': 'AAPL',
    'target_price': 150.0
}

Make a POST request to set the alert:
response = requests.post(app_url, json=data)

OR, you may use the provided test file: test.py.
To use it, simply run the test file while the microservice is already running.

## How to RECIEVE data from noti_service:
Check response code:
if response.status_code == 200:
    print("Alert set successfully!")
else:
    print("Failed to set the alert.")

You can print out the response text as well:
print(response.text)

## UML Diagram
