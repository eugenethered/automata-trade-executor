from core.trade.InstrumentTrade import InstrumentTrade
from utility.json_utility import as_data


def deserialize_trade(trade) -> InstrumentTrade:
    instrument_from = as_data(trade, 'instrument_from')
    instrument_to = as_data(trade, 'instrument_to')
    quantity = as_data(trade, 'quantity')
    return InstrumentTrade(instrument_from, instrument_to, quantity)
