from cache.holder.RedisCacheHolder import RedisCacheHolder


class TradeConductor:

    def __init__(self, options):
        self.options = options
        self.cache = RedisCacheHolder()

    def fetch_trade_to_execute(self):
        trade_key = self.build_trade_key()
        return self.cache.fetch(trade_key, as_type=dict)

    def build_trade_key(self):
        return self.options['TRADE_KEY']
