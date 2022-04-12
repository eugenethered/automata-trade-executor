import unittest

from core.trade.CurrencyTradeOrder import CurrencyTradeOrder

from trade.serialize.trade_serializer import serialize_currency_trade


class TradeSerializeTestCase(unittest.TestCase):

    def test_currency_trade_order_serializes(self):
        trade = CurrencyTradeOrder('USDT', 'BTC', 10, 'BUY')
        actual = serialize_currency_trade(trade)
        result = {
            'currency_from': 'USDT',
            'currency_to': 'BTC',
            'quantity': 10,
            'side': 'BUY'
        }
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()
