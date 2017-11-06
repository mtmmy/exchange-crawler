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
    rate_table = soup.find('table', {'id': 'inteTable1'})
    cur_rows = rate_table.find('tr', {'class': 'tableContent-light'})
    usd_datas = cur_rows.find_all('td', {'class': ['odd', 'even']})
    for data in usd_datas:
        rate_type = data['data-name']
        E_SUN_RATE[rate_type] = data.text
    return E_SUN_RATE
