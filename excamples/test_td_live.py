from gmsdk import td, get_strerror
from gmsdk.enums import *
from gmsdk.util import *


def on_execrpt(execrpt):
    print('got execrpt report: ', execrpt_to_dict(execrpt))


def on_order_status(o):
    print('got order: ', order_to_dict(o))


def on_error(code, message):
    print('got error: %s=%s' % (code, message))


def on_login():
    # place 4 orders
    order1 = td.open_long('CFFEX', 'IF1512', 0, 100)
    order2 = td.open_short('CFFEX', 'IF1512', 0, 100)
    order3 = td.close_long('CFFEX', 'IF1512', 0, 10)
    order4 = td.close_short('CFFEX', 'IF1512', 0, 10)

    print('placed 4 orders: \n', order_to_dict(order1), order_to_dict(order2), order3, order4)
    # try to cancel order1
    td.cancel_order(order1.cl_ord_id)

    # query order
    order = td.get_order(order2.cl_ord_id)
    print('query order: ', order_to_dict(order) if order else '')

    # query cash
    cash = td.get_cash()
    print('query cash: ', cash_to_dict(cash) if cash else '')

    # query position
    position = td.get_position('CFFEX', 'IF1512', OrderSide_Bid)
    print('query position: ', position_to_dict(position) if position else '')

    # query all positions
    positions = td.get_positions()
    print('query all positions: ', positions)

    # get unfinished orders
    orders = td.get_unfinished_orders()
    print('query unfinished orders: ', orders)

# register callbacks
td.ev_execrpt += on_execrpt
td.ev_error += on_error
td.ev_login += on_login
td.ev_order_status += on_order_status

# init td
ret = td.init('demo@myquant.cn', '123456', 'strategy_2', 'localhost:8001')
print('td init result: ', ret)
td.run()
