# Exercise 2: Write a Python program to get the current time in hours, minutes, seconds and timezone
# and to display a message based on the time of day.

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print("Hours: ", timestamp)
timestamp = time.strftime('%M')
print('Minutes: ', timestamp)
timestamp = time.strftime('%S')
print("Seconds: ", timestamp)

a = int(input("Enter Hour: "))
if a < 7:
    print("Good Morning Sir")
elif a < 16:
    print ("Good Afternoon Sir")
elif a < 20:
    print("Good Night Sir")
else:
    print("Good Evening Sir")

# Another way to do this
import time
t = time.strftime('%H:%M:$S')
hour = int(time.strftime('%H'))

if(hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<16):
    print("Good Afternoon Sir")
elif(hours>=16 and hour<0):
    print("Good Evening Sir")

# This is bsed on real time clock with enteing the hour manually