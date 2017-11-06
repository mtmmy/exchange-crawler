"""This script compares exchange rate between e_sun and xe"""
import threading
import winsound
from datetime import datetime
from random import randint
import ESunBankUSDCrawler
import XECrawler

DURATION = 2000
FREQ = 440

OLD_E_SUN_TARGET_RATE = -1
def compare_rate():
    """to compare rate between e_sun and xe"""
    global OLD_E_SUN_TARGET_RATE
    e_sun_rate = ESunBankUSDCrawler.parse_exchange()
    xe_rate = XECrawler.parse_exchange()
    e_sun_target_rate = float(e_sun_rate['即期賣出匯率'])
    print("玉山即期賣出: %0.3f; XE rate: %0.3f" % (e_sun_target_rate, xe_rate))
    if OLD_E_SUN_TARGET_RATE != -1 and OLD_E_SUN_TARGET_RATE != e_sun_target_rate:
        winsound.Beep(FREQ, DURATION)
    if (e_sun_target_rate - xe_rate) < 0.04 or (e_sun_target_rate - xe_rate) > 0.06:
        winsound.Beep(FREQ, DURATION)
    OLD_E_SUN_TARGET_RATE = e_sun_target_rate

    now = datetime.now()
    hour = now.hour
    if hour > 9 and hour < 16:
        threading.Timer(randint(30, 60), compare_rate).start()
    elif hour > 16 and hour < 23:
        threading.Timer(randint(180, 300), compare_rate).start()
    else:
        threading.Timer(randint(1800, 3600), compare_rate).start()
compare_rate()
