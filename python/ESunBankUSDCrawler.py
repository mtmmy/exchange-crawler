"""This script grab exchange rates from web and parse them"""
import threading
import winsound
import requests
from bs4 import BeautifulSoup

DURATION = 2000
FREQ = 440

URL = "https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates"
E_SUN_RATE = {}
def parse_exchange():
    """get usd exchage rate from e-sun bank"""
    resp1 = requests.post(URL)
    resp2 = requests.post(URL, cookies=resp1.cookies)
    soup = BeautifulSoup(resp2.text, 'html.parser')
    usd_datas = (soup.find('table', {'id': 'inteTable1'}).
                 find('tr', {'class': 'tableContent-light'}).
                 find_all('td', {'class': ['odd', 'even']}))
    for data in usd_datas:
        rate_type = data['data-name']
        if (rate_type in E_SUN_RATE and rate_type == '即期賣出匯率'
                and E_SUN_RATE[rate_type] != data.string):
            winsound.Beep(FREQ, DURATION)
        E_SUN_RATE[rate_type] = data.text
    print(E_SUN_RATE)
    threading.Timer(5, parse_exchange).start()

parse_exchange()
