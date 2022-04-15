from core.trade.InstrumentTrade import InstrumentTrade
from utility.string_utility import is_empty


def serialize_trade(trade: InstrumentTrade) -> dict:
    serialized = {
        'instrument_from': trade.instrument_from,
        'instrument_to': trade.instrument_to,
        'quantity': trade.quantity,
        'status': trade.status.value
    }
    if not is_empty(trade.description):
        serialized['description'] = trade.description
    return serialized
