from core.trade.InstrumentTrade import InstrumentTrade


def serialize_trade(trade: InstrumentTrade) -> dict:
    return {
        'instrument_from': trade.instrument_from,
        'instrument_to': trade.instrument_to,
        'quantity': trade.quantity
    }
