import time
import sys

total_seconds = 3600 # 专注时钟总秒数,默认1小时
seconds_passed = 0

while seconds_passed < total_seconds:
    
    # 打印倒计时
    sys.stdout.write("\r") 
    sys.stdout.write("{:2d}:{:02d}".format((total_seconds-seconds_passed)//60, (total_seconds-seconds_passed)%60))
    sys.stdout.flush()

    time.sleep(1)
    seconds_passed += 1

print("\n时间到!")
