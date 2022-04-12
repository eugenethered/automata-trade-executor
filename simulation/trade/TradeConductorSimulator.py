from core.trade.CurrencyTradeOrder import CurrencyTradeOrder

from trade.TradeConductor import TradeConductor


class TradeConductorSimulator:

    def __init__(self, options):
        self.trade_conductor = TradeConductor(options)

    @staticmethod
    def obtain_trade():
        return CurrencyTradeOrder('USDT', 'BTC', 10, 'BUY')

    def store_and_fetch_trade_for_execution(self):
        trade = self.obtain_trade()
        self.trade_conductor.store_trade_to_execute(trade)
        stored_trade = self.trade_conductor.fetch_trade_to_execute()
        print(f'the stored trade -> {stored_trade}')
