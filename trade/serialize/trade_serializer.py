from core.trade.CurrencyTradeOrder import CurrencyTradeOrder


def serialize_currency_trade(trade: CurrencyTradeOrder) -> dict:
    return {
        'currency_from': trade.currency_from,
        'currency_to': trade.currency_to,
        'quantity': trade.quantity,
        'side': trade.side.upper()
    }
