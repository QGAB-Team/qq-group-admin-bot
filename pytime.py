import time
import os
while True:
    time_now = time.strftime("%H%M", time.localtime())  # 刷新
    if time_now == "00:01": # 设置要执行的时间
        os.removedirs("chlist")
        time.sleep(60)