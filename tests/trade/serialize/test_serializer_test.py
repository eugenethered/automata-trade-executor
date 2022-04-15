import unittest

from core.trade.InstrumentTrade import InstrumentTrade, Status

from trade.serialize.trade_serializer import serialize_trade


class TradeSerializeTestCase(unittest.TestCase):

    def test_currency_trade_order_serializes(self):
        trade = InstrumentTrade('USDT', 'BTC', 10)
        actual = serialize_trade(trade)
        result = {
            'instrument_from': 'USDT',
            'instrument_to': 'BTC',
            'quantity': 10,
            'status': 'new'
        }
        self.assertEqual(actual, result)

    def test_currency_trade_order_serializes_with_status_and_description(self):
        trade = InstrumentTrade('USDT', 'BTC', 10, Status.ERROR, 'Not enough funds')
        actual = serialize_trade(trade)
        result = {
            'instrument_from': 'USDT',
            'instrument_to': 'BTC',
            'quantity': 10,
            'status': 'error',
            'description': 'Not enough funds'
        }
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()
