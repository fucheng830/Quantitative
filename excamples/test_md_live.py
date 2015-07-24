import time
from gmsdk.api import md


def on_tick(tick):
    print('%s %s %s %s' % (time.time(), tick.sec_id, tick.last_price, tick.utc_time))


def on_bar(bar):
    print('%s:%s %s:%s: %s %s %s' % (time.time(), bar.sec_id, bar.bar_type, bar.open, bar.high, bar.low, bar.close))


def on_error(code, message):
    print(code, message)


md.ev_tick += on_tick
md.ev_bar += on_bar
md.ev_error += on_error

ret = md.init(
    username='demo@myquant.cn',
    password='123456',
    mode=3,
    subscribe_symbols='CFFEX.IF1512.tick,CFFEX.IC1512.tick,CFFEX.IH1512.tick,CFFEX.TF1512.tick',
)

print('init result: ', ret)
md.run()
