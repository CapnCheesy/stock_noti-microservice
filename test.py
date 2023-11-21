import requests
import json

app_url = 'http://127.0.0.1:5000/set_alert'  # replace with actual app URL (this is valid if running locally)

data = {
    'stock_name': 'AAPL',  # replace with the desired stock name
    'target_price': 150.0   # replace with the desired target price
}

# Make a POST request to set the alert
response = requests.post(app_url, json=data)

# Check the response
if response.status_code == 200:
    print("Alert set successfully!")
else:
    print("Failed to set the alert.")

print("Reponse: ", response.text)