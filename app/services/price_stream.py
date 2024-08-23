from binance import ThreadedWebsocketManager

def start_price_stream(symbol, callback):
    twm = ThreadedWebsocketManager(api_key='your_api_key', api_secret='your_api_secret')
    twm.start()

    def handle_socket_message(msg):
        if msg['e'] == 'trade':
            price = float(msg['p'])
            callback(price)

    twm.start_trade_socket(callback=handle_socket_message, symbol=symbol)
    twm.join()
