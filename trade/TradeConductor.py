from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.trade.CurrencyTradeOrder import CurrencyTradeOrder

from trade.serialize.trade_deserializer import deserialize_currency_trade
from trade.serialize.trade_serializer import serialize_currency_trade


class TradeConductor:

    def __init__(self, options):
        self.options = options
        self.cache = RedisCacheHolder()

    def store_trade_to_execute(self, trade: CurrencyTradeOrder):
        trade_key = self.build_trade_key()
        trade_to_store = serialize_currency_trade(trade)
        self.cache.store(trade_key, trade_to_store)

    def fetch_trade_to_execute(self) -> CurrencyTradeOrder:
        trade_key = self.build_trade_key()
        raw_trade = self.cache.fetch(trade_key, as_type=dict)
        return deserialize_currency_trade(raw_trade)

    def build_trade_key(self):
        return self.options['TRADE_KEY']

