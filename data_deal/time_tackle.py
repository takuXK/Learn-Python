import datetime as dt
now = dt.datetime.now()
time_value = now + dt.timedelta(seconds=2)  #timedelta()函数直接做时间转换，用于改变日期，时间

print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(time_value.strftime('%Y-%m-%d %H:%M:%S'))
print(time_value - now)

import time
now_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",now_time))