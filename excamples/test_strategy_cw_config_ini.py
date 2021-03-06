from gmsdk.api import StrategyBase
import time

g_count = 0


class MyStrategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        super(MyStrategy, self).__init__(*args, **kwargs)
        self.flag = True

    def on_tick(self, tick):
        global g_count
        g_count += 1
        print("symbol: %s price: %s count: %d" % (tick.sec_id, tick.last_price, g_count))

        if g_count % 1600 == 0:
            o = self.open_long(tick.exchange, tick.sec_id, tick.last_price, 1)
            if o:
                print("Open long %s" % o.cl_ord_id)
                print("strategy: %s" % o.strategy_id)
                print("symbol: %s" % o.sec_id)
                print("price: %f" % o.price)
                print("volume: %f" % o.volume)
            else:
                print("error")
        elif g_count % 800 == 0:
            o = self.open_short(tick.exchange, tick.sec_id, 0, 1)
            if o:
                print("Open short: %s" % o.cl_ord_id)
                print("strategy: %s" % o.strategy_id)
                print("symbol: %s" % o.sec_id)
                print("price: %f" % o.price)
                print("volume: %f" % o.volume)
            else:
                print("error")
        elif g_count % 400 == 0:
            o = self.close_long(tick.exchange, tick.sec_id, tick.last_price, 2)
            if o:
                print("Close long: %s" % o.cl_ord_id)
                print("strategy: %s" % o.strategy_id)
                print("symbol: %s" % o.sec_id)
                print("price: %f" % o.price)
                print("volume: %f" % o.volume)
            else:
                print("error")
        elif g_count % 20 == 0:
            o = self.close_short(tick.exchange, tick.sec_id, 0, -1)
            if o:
                print("Close short: %s" % o.cl_ord_id)
                print("strategy: %s" % o.strategy_id)
                print("symbol: %s" % o.sec_id)
                print("price: %f" % o.price)
                print("volume: %f" % o.volume)
            else:
                print("error")
        else:
            pass

    def on_bar(self, bar):
        print("synbol: %s price:%s" % (bar.sec_id, bar.close))

    def on_execrpt(self, res):
        print("execrpt: ")
        print("strategy: %s" % res.strategy_id)
        print("symbol: %s" % res.sec_id)
        print("price: %s" % res.price)
        print("volume: %s" % res.volume)

    def on_order_new(self, res):
        print("order_new: %s %s" % (res.strategy_id, res.price))

    def on_order_filled(self, res):
        print("order_filled: %s %s" % (res.strategy_id, res.price))

    def on_order_partiall_filled(self, res):
        print("order_partiall_filled: %s %s" % (res.strategy_id, res.price))

    def on_order_stop_executed(self, res):
        print("order_stop_executed: %s %s" % (res.strategy_id, res.price))

    def on_order_canceled(self, res):
        print("order_canceled: %s %s" % (res.strategy_id, res.price))

    def on_order_cancel_rejected(self, res):
        print("order_cancel_rejected: %s %s" % (resstrategy_id, res.price))


if __name__ == '__main__':
    ret = MyStrategy(config_file='test_strategy.ini').run()
    print(('exit code: ', ret))
