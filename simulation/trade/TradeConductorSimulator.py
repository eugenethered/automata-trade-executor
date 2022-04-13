from core.trade.InstrumentTrade import InstrumentTrade

from trade.TradeConductor import TradeConductor
from trade.executor.TradeExecutor import TradeExecutor


class TradeConductorSimulator:

    def __init__(self, options):
        # trade_executor - not required for this simulation
        trade_executor: TradeExecutor = None
        self.trade_conductor = TradeConductor(options, trade_executor)

    @staticmethod
    def obtain_trade():
        return InstrumentTrade('USDT', 'BTC', 10)

    def store_and_fetch_trade_for_execution(self):
        trade = self.obtain_trade()
        self.trade_conductor.store_trade_to_execute(trade)
        stored_trade = self.trade_conductor.fetch_trade_to_execute()
        print(f'Stored trade -> {stored_trade}')
