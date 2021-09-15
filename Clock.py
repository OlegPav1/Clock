#Clock
from time import sleep
import datetime
from datetime import timedelta
date = datetime.datetime.now()
for h in range(25):
    if h<25:
        for m in range(61):
                for my_time in range(61):
                        date = date + timedelta(seconds=1)
                        print(date.strftime('%H:%M:%S'), end='')
                        sleep(1)
                        my_time +=1
                        print('\r', end='')
        m +=1
    else:
        h=-1
h +=1
#12365465
#1234
#555