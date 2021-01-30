class OMath(object):
    def __init__(self):
        pass

def get_call_sell_expiry_pl(current_price, stock_price, strike):
    '''
    Get profit/loss on expiry day for selling call
    :param current_price: Current Price against call strike
    :param stock_price: Price of underlying Stock
    :param strike: Target Strike
    :return:
    e.g. BANKNIFTY strike: 32500, stock_price: 32200, current_price: 280
    '''
    return (current_price - max(0, (stock_price - strike)))

def get_call_buy_expiry_pl(current_price, stock_price, strike):
    '''
    Get profit/loss on expiry day for selling call
    :param current_price: Current Price against call strike
    :param stock_price: Price of underlying Stock
    :param strike: Target Strike
    :return:
    e.g. BANKNIFTY strike: 32500, stock_price: 32200, current_price: 280
    '''
    return max(0, (stock_price - strike)) - current_price

def get_put_sell_expiry_pl(current_price, stock_price, strike):
    '''

    :param current_price: Current Price against put strike
    :param stock_price: Price of underlying Stock
    :param strike: Target Strike
    :return:
    e.g. BANKNIFTY strike: 32500, stock_price: 32200, current_price: 280
    '''
    return (current_price - max(0, (stock_price - strike)))

def get_put_buy_expiry_pl(current_price, stock_price, strike):
    '''

    :param current_price: Current Price against put strike
    :param stock_price: Price of underlying Stock
    :param strike: Target Strike
    :return:
    e.g. BANKNIFTY strike: 32500, stock_price: 32200, current_price: 280
    '''
    return max(0, (stock_price - strike)) - current_price
