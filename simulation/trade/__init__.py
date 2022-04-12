from cache.holder.RedisCacheHolder import RedisCacheHolder

from simulation.trade.TradeConductorSimulator import TradeConductorSimulator

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_KEY': 'simulation:trade'
    }

    RedisCacheHolder(options)

    simulator = TradeConductorSimulator(options)
    simulator.store_and_fetch_trade_for_execution()
