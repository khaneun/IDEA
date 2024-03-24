from api.private_info import *
from api.public_info import *
import schedule
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

api_key = ""
api_secret = ""
api = XCoinAPI(api_key, api_secret)

unit_size = 5000
xCoins = ['BTC', 'ETH', 'BCH', 'ETC']
payment_currency = "KRW"
plan = "09:00"

def main():

    # 구매할 Coin Portfolio
    for xCoin in xCoins:

        # Coin 별 시장가 구매(unit size 고정) Unit 계산
        get_ticker(xCoin, payment_currency)
        orderbook_list = json.loads(get_orderbook(xCoin, payment_currency))
        current_price = orderbook_list["data"]['bids'][0]['price']
        unit = unit_size/int(current_price)
        unit = f"{unit:.8f}"
        logger.info("[{}] {} ==> {} unit(s)".format(xCoin, current_price, unit))

        # API Message 조립
        rgParams = {
            'endpoint': '/trade/market_buy',
            "payment_currency": "KRW",
            "order_currency": xCoin,
            "units": unit
        }

        # 매수
        result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
        logger.info(result)

def status_message():
    # 상태 확인 메시지 log
    logger.info("Running on the schedule at {}".format(plan))

# 실행 주기 설정
schedule.every(15).minutes.do(status_message)
schedule.every().day.at(plan).do(main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)