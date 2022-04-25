import requests
import random as rn
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout


def read_proxylist(api_key):
    """
    Return proxy list from best-proxies.ru
    :return: proxy_list
    """
    link = f'https://api.best-proxies.ru/proxylist.txt?key={api_key}&type=socks5&limit=0'
    data = requests.get(link).text
    return [x.replace('\r', '') for x in data.split('\n') if x]


def check_proxy():
    """
    Check proxy
    :return: work_proxy_address
    """
    global proxy
    if proxy:
        pass
    proxy_address = rn.choice(PROXYLIST)
    proxies = {
        'http': f'socks5://{proxy_address}',
        'https': f'socks5://{proxy_address}'
    }
    try:
        requests.post('https://google.com/', proxies=proxies, timeout=2).json()
        proxy = proxy_address
    except (ConnectionError,
            ConnectTimeout,
            ReadTimeout):
        PROXYLIST.remove(proxy_address)
        check_proxy()


def find_work_proxy():
    """
    Return work proxy
    :return: work_proxy_adress
    """
    executor = ThreadPoolExecutor(max_workers=10)
    tasks = []
    for _ in range(10):
        tasks.append(executor.submit(check_proxy))
    while True:
        if proxy:
            return proxy


proxy = None
key = 'YOUR_KEY_HERE'
PROXYLIST = read_proxylist(key)
