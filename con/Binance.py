from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

api_key = "mkqrEjGweL1x4uUDTM4wp7NQwG2BggDBx9y2drE6IBLUgfmkAbIafvhRCSS5xKqS"
api_secret = "TVN7GZ9qCrtYW0uTDsrLucxFt8WS3PV3TRlIowoiDPlhNJDR4m8xse1TEaY8koI5"

client = Client(api_key, api_secret)


depth = client.get_symbol_info(symbol="DASHUSDT")
for row in depth:
    print(depth[row])