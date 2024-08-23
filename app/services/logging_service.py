import logging

logging.basicConfig(filename='logs/trading_bot.log', level=logging.INFO)

def log_trade(message: str):
    logging.info(message)
