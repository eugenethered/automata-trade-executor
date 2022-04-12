from core.trade.CurrencyTradeOrder import CurrencyTradeOrder
from utility.json_utility import as_data


def deserialize_currency_trade(trade) -> CurrencyTradeOrder:
    currency_from = as_data(trade, 'currency_from')
    currency_to = as_data(trade, 'currency_to')
    quantity = as_data(trade, 'quantity')
    side = as_data(trade, 'side')
    return CurrencyTradeOrder(currency_from, currency_to, quantity, side)
