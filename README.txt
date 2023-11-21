README for noti_service microservice for stock price notifications.

How to REQUEST data from noti_service:
-set an app url variable in your own app to the url for noti_service
(this can be 'http://127.0.0.1:5000/set_alert' if running locally)

-create a data structure with the 'stock_name' and 'target_price' variables, and set the values to your desired stock name and target price
Example:
data = {
    'stock_name': 'AAPL',
    'target_price': 150.0
}

-make a POST request to set the alert:
response = requests.post(app_url, json=data)

How to RECIEVE data from noti_service:
-check response code:
if response.status_code == 200:
    print("Alert set successfully!")
else:
    print("Failed to set the alert.")

-you can print out the response text as well:
print(response.text)