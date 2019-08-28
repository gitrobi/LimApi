# LimApi.py
"""
说明:
此接口仅为lim trade.exe后端服务web接口的python封装,本接口不提供任何后端服务.

声明:
此代码仅限用于个人学习和研究目的；不得将上述内容用于商业或者非法用途，否则一切后果请用户自负!!!
本人与lim服务提供方没有任何关系, 此接口仅为lim trade.exe后端服务web接口的python封装,本接口不提供任何后端服务.
使用本接口碰到的任何问题,请自行解决.
@Date : 2019/08/28
@Author: Robi
"""

def ini2json(ini_file):
    import configparser
    d = {}
    cfg = configparser.ConfigParser()
    cfg.read(ini_file)
    for section in cfg.sections():
        for option in cfg.options(section):
            d[option] = cfg.get(section, option)
    return d


def web_http(url, params):
    import requests
    res = requests.get(url, params)
    return res.json()


class LimApi(object):

    def __init__(self):
        self.account_info = ini2json('LimAccount.ini')
        self.url_info = ini2json('LimConfig.ini')

    def login(self):
        url = self.url_info.get('server') + self.url_info.get('login')
        params = self.account_info
        return web_http(url, params)

    def logout(self):
        url = self.url_info.get('server') + self.url_info.get('logout')
        params = {'account' : self.account_info['account']}
        return web_http(url, params)

    def get_broker_count(self):
        url = self.url_info.get('server') + self.url_info.get('get_broker_count')
        return web_http(url, None)

    def query_user_info(self):
        url = self.url_info.get('server') + self.url_info.get('query_user_info')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_bank_info(self):
        url = self.url_info.get('server') + self.url_info.get('query_bank_info')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_myasset(self):
        url = self.url_info.get('server') + self.url_info.get('query_myasset')
        params = {'account' : self.account_info['account']}
        return web_http(url, params)

    def query_order_list(self):
        url = self.url_info.get('server') + self.url_info.get('query_order_list')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_mystock(self):
        url = self.url_info.get('server') + self.url_info.get('query_mystock')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_dayorder(self):
        url = self.url_info.get('server') + self.url_info.get('query_dayorder')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_daydeal(self):
        url = self.url_info.get('server') + self.url_info.get('query_daydeal')
        params = {'account': self.account_info['account']}
        return web_http(url, params)

    def query_history_order(self, days, day_offset):
        '''
        :param days: 获取几天的记录
        :param day_offset: 最后一天距离现在的天数
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('query_history_order')
        params = {'account': self.account_info['account'], 'days': days, 'day_offset': day_offset}
        return web_http(url, params)

    def query_history_deal(self, days, day_offset):
        '''
        :param days: 获取几天的记录
        :param day_offset: 最后一天距离现在的天数
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('query_history_deal')
        params = {'account': self.account_info['account'], 'days': days, 'day_offset': day_offset}
        return web_http(url, params)

    def query_history_delorder(self, days, day_offset):
        '''
        :param days: 获取几天的记录
        :param day_offset: 最后一天距离现在的天数
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('query_history_delorder')
        params = {'account': self.account_info['account'], 'days': days, 'day_offset': day_offset}
        return web_http(url, params)

    def query_history_jour(self, days, day_offset):
        '''
        :param days: 获取几天的记录
        :param day_offset: 最后一天距离现在的天数
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('query_history_jour')
        params = {'account': self.account_info['account'], 'days': days, 'day_offset': day_offset}
        return web_http(url, params)

    def buy_sell(self, buy_or_sell, trademode, stockcode, num, price):
        '''
        :param buy_or_sell: 买:1/卖:0
        :param trademode: 0:限价;1:对方最优;3:即时成交,剩余撤消委托4:五档即时成效,剩余撤消5:全额成效或撤消委托6:五档即时成效,剩余转限
        :param stockcode: 股票代码
        :param num: 股数
        :param price: 价格
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('buy_shell')
        params = {'account': self.account_info['account'], 'buy_or_sell': buy_or_sell,
                  'stockcode': stockcode, 'num':num, 'price':price, 'trademode': trademode }
        return web_http(url, params)

    def get_stock_quote(self, stockcode):
        url = self.url_info.get('server') + self.url_info.get('get_stock_quote')
        params = {'account': self.account_info['account'], 'stockcode': stockcode}
        return web_http(url, params)

    def cancel_order(self, order_id, market):
        '''
        :param order_id: 订单id
        :param market: 订单市场，0:深圳A股，1：上海A股，2深圳B股，3上海B股，12：新三板
        :return:
        '''
        url = self.url_info.get('server') + self.url_info.get('cancel_order')
        params = {'account': self.account_info['account'], 'order_id': order_id, 'market' : market}
        return web_http(url, params)


if __name__ == '__main__':
    api = LimApi()
    print('login', api.login())
    print('get_broker_count', api.get_broker_count())
    print('query_user_info', api.query_user_info())
    print('query_bank_info', api.query_bank_info())
    print('query_myasset', api.query_myasset())
    print('query_order_list', api.query_order_list())
    print('query_history_order', api.query_history_order(3,1))
    print('query_history_deal', api.query_history_deal(3,1))
    print('query_history_delorder', api.query_history_delorder(3,1))
    print('query_history_jour', api.query_history_jour(3,1))
    print('get_stock_quote', api.get_stock_quote('600993'))
    print('buy_sell', api.buy_sell(1, 0, '159901', 100, 4.600))
    #print('cancel_order', api.cancel_order(1, 0))
    #print('logout', api.logout())