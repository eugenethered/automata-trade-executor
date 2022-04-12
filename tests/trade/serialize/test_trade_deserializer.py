import unittest

from trade.serialize.trade_deserializer import deserialize_currency_trade


class TradeDeserializeTestCase(unittest.TestCase):

    def test_currency_trade_order_deserializes(self):
        raw_trade = {
            'currency_from': 'USDT',
            'currency_to': 'BTC',
            'quantity': 10,
            'side': 'BUY'
        }
        trade = deserialize_currency_trade(raw_trade)
        self.assertEqual(trade.currency_from, 'USDT')
        self.assertEqual(trade.currency_to, 'BTC')
        self.assertEqual(trade.quantity, 10)
        self.assertEqual(trade.side, 'BUY')


if __name__ == '__main__':
    unittest.main()
