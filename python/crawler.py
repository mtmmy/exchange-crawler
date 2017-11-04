import urllib.request
from bs4 import BeautifulSoup
import time, threading
import winsound

DURATION = 2000
FREQ = 440
URL = "http://www.taiwanrate.org/exchange_rate.php?c=USD#.Wf1rTltL-Ht"

BANKINFO = {}
def parseExchange():
    r = urllib.request.urlopen(URL).read().decode()
    soup = BeautifulSoup(r, 'html.parser')
    trs = soup.find('table', {'id': 'accounts2'}).find_all('tr')
    for row in trs:
        bankprice = {}
        name = ''
        tds = row.find_all('td')
        if not tds:
            continue
        for i, data in enumerate(tds):
            if i == 0:
                name = data.string
                if name != '玉山銀行':
                    continue
            elif i == 1:
                bankprice['buy'] = data.string
            else:
                bankprice['sell'] = data.string
        if any(bankprice) and name == '玉山銀行':
            if not BANKINFO:
                BANKINFO[name] = bankprice
            else:
                if (BANKINFO[name]['buy'] != bankprice['buy']
                        or BANKINFO[name]['sell'] != bankprice['sell']):
                    winsound.Beep(FREQ, DURATION)

    print(BANKINFO)
    threading.Timer(5, parseExchange).start()

parseExchange()
