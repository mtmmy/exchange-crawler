"""This script grab exchange rates from web and parse them"""
import requests
from bs4 import BeautifulSoup

DURATION = 2000
FREQ = 440

URL = "http://www.xe.com/zh-HK/currencyconverter/convert/?Amount=1&From=USD&To=TWD"
def parse_exchange():
    """get usd exchage rate from e-sun bank"""
    resp = requests.post(URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    rate = soup.find('span', {'class': 'uccResultAmount'})
    return float(rate.text)