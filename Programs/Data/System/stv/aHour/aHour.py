import time


from datetime import datetime
now = datetime.now()
second = now.second
hour = now.hour
minute = now.minute


while True:   
        if second == 59:
            second = second - 59
            minute = minute + 1
        else:
            time.sleep(1)
            second = second + 1
        print(hour, minute, second)
        
while True:
        if minute == 59:
                minute = minute - 59
                hour + 1
        elif hour == 24:
                hour = hour - 24
        print(hour, minute, second)
                
                
