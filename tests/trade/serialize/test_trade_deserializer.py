import unittest

from core.trade.InstrumentTrade import Status

from trade.serialize.trade_deserializer import deserialize_trade


class TradeDeserializeTestCase(unittest.TestCase):

    def test_currency_trade_order_deserializes(self):
        raw_trade = {
            'instrument_from': 'USDT',
            'instrument_to': 'BTC',
            'quantity': 10
        }
        trade = deserialize_trade(raw_trade)
        self.assertEqual(trade.instrument_from, 'USDT')
        self.assertEqual(trade.instrument_to, 'BTC')
        self.assertEqual(trade.quantity, 10)

    def test_currency_trade_order_deserializes_with_status_and_description(self):
        raw_trade = {
            'instrument_from': 'USDT',
            'instrument_to': 'BTC',
            'quantity': 10,
            'status': 'cancelled',
            'description': 'cancelled order:11',
        }
        trade = deserialize_trade(raw_trade)
        self.assertEqual(trade.instrument_from, 'USDT')
        self.assertEqual(trade.instrument_to, 'BTC')
        self.assertEqual(trade.quantity, 10)
        self.assertEqual(trade.status, Status.CANCELLED)
        self.assertEqual(trade.description, 'cancelled order:11')


if __name__ == '__main__':
    unittest.main()
