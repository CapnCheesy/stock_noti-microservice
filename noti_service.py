from flask import Flask, request
import requests
import time

app = Flask(__name__)

alerts = {}

def check_stock_price(stock_name, target_price):
    api_key = "E21TRZ6ZY52QY01N"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_key}"

    while True:
        response = requests.get(url)
        data = response.json()

        if "Global Quote" in data:
            stock_data = data["Global Quote"]
            current_price = float(stock_data["05. price"])

            if current_price == target_price:
                return True
            
        # check price every 5 mins
        time.sleep(300)


@app.route('/set_alert', methods=['POST'])
def set_alert():
    data = request.json
    stock_name = data.get('stock_name')
    target_price = data.get('target_price')

    if stock_name and target_price:
        alerts[stock_name] = target_price
        return (f"Alert set for {stock_name} at {target_price}")
    
    return "Invalid request" # if stock doesn't exist return error

@app.route('/check_alerts')
def check_alerts():
    for stock_name, target_price in alerts.items():
        if check_stock_price(stock_name, target_price):
            # return alert
            print(f"{stock_name} has reached the target price {target_price}")
            # delete alert once triggered
            del alerts[stock_name]

    return "Checked alerts"

if __name__ == '__main__':
    app.run(debug=True)