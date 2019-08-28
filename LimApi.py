import configparser


def ini2json(ini_file):
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
    return res


account_info = ini2json('LimAccount.ini')
url_info = ini2json('LimConfig.ini')


class LimApi(object):

    def login(self):
        url = url_info.get('server') + url_info.get('login')
        params = account_info
        res = web_http(url, params)
        return res


api = LimApi()
res = api.login()
print(res)