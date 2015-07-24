from gmsdk.api import md


def on_tick(tick):
    print('tick: ', tick.sec_id, ' ', tick.last_price, ' ', tick.utc_time)


def on_bar(bar):
    print('bar: ', bar.symbol, ' ', bar.open, ' ', bar.bar_time)


md.ev_tick += on_tick
md.ev_bar += on_bar
ret = md.init(username='demo@myquant.cn',
              password='123456',
              mode=4,
              subscribe_symbols='CFFEX.IF1512.tick',
              start_time='2015-05-27 00:00:00',
              end_time='2015-05-27 09:30:00')

print('init result: ', ret)
md.run()
