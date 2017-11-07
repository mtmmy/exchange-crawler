"""This script compares exchange rate between e_sun and xe"""
import threading
import winsound
import time
from datetime import datetime
import ESunBankUSDCrawler
import XECrawler

DURATION = 1000
FREQ = 340

OLD_E_SUN_TARGET_RATE = -1
def compare_rate():
    """to compare rate between e_sun and xe"""
    global OLD_E_SUN_TARGET_RATE
    e_sun_start = time.time()
    e_sun_rate = ESunBankUSDCrawler.parse_exchange()
    elapsed_e_sun = time.time() - e_sun_start
    xe_start = time.time()
    xe_rate = XECrawler.parse_exchange()
    elapsed_xe = time.time() - xe_start
    delay = 60
    if '即期賣出匯率' in e_sun_rate:
        e_sun_target_rate = float(e_sun_rate['即期賣出匯率'])
        now = datetime.now()
        hour = now.hour
        sec = now.second
        delay = (60 - sec if sec > 10 else 0) + 15
        print(now.strftime('%d %b %H:%M:%S'),
              "玉山即期賣出: %0.2f; XE rate: %0.3f" % (e_sun_target_rate, xe_rate),
              "; %f; %f" % (elapsed_e_sun, elapsed_xe))
        if OLD_E_SUN_TARGET_RATE != -1 and OLD_E_SUN_TARGET_RATE != e_sun_target_rate:
            winsound.Beep(FREQ + 100, DURATION + 1000)
        OLD_E_SUN_TARGET_RATE = e_sun_target_rate

    if hour > 8 and hour < 23:
        threading.Timer(delay, compare_rate).start()
compare_rate()
