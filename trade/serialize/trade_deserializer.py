from core.trade.InstrumentTrade import InstrumentTrade, Status
from utility.json_utility import as_data
from utility.string_utility import is_empty


def deserialize_trade(trade) -> InstrumentTrade:
    instrument_from = as_data(trade, 'instrument_from')
    instrument_to = as_data(trade, 'instrument_to')
    quantity = as_data(trade, 'quantity')
    status = as_data(trade, 'status')
    description = as_data(trade, 'description')
    deserialized_trade = InstrumentTrade(instrument_from, instrument_to, quantity)
    set_status_as_available(deserialized_trade, status)
    set_description_as_available(deserialized_trade, description)
    return deserialized_trade


def set_status_as_available(deserialized_trade, value):
    if value is not None:
        result = [member for name, member in Status.__members__.items() if member.value == value]
        deserialized_trade.status = result[0]


def set_description_as_available(deserialized_trade, value):
    if not is_empty(value):
        deserialized_trade.description = value


