import requests

def get_ticker(order_currency="BTC", payment_currency="KRW"):

    url = "https://api.bithumb.com/public/ticker/{}_{}".format(order_currency, payment_currency)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    return response.text

def get_orderbook(order_currency="BTC", payment_currency="KRW", count=5):

    url = "https://api.bithumb.com/public/orderbook/{}_{}".format(order_currency, payment_currency)
    headers = {"accept": "application/json"}
    data = {"count": 5}
    response = requests.get(url, headers=headers, data=data)

    return response.text