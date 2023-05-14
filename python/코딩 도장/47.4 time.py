import datetime
import time
time.time()  # 1526694734.1275969

# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=19, tm_hour=10, tm_min=54, tm_sec=25, tm_wday=5, tm_yday=139, tm_isdst=0), tm_isdst는 섬머타임 여부
time.localtime(time.time())

time.strftime('%Y-%m-%d', time.localtime(time.time()))  # '2018-05-19'
time.strftime('%c', time.localtime(time.time()))  # 'Sat May 19 11:14:27 2018'

datetime.datetime.today()  # datetime.datetime(2018, 5, 19, 13, 15, 15, 881617)

# pip install pytz 필요, datetime.datetime(2018, 5, 19, 4, 40, 12, 536110, tzinfo=<UTC>)
datetime.datetime.now(pytz.timezone('UTC'))
