movie_quote = """One of my favorite lines from The Godfather is: 
"I'am goin gto make him an offer he can't refuse."
Do you know who said this?"""

print(movie_quote)

import sys
print(dir(sys))

help(sys.__stdout__)

print(100*'-')
k = 1#1L in python 2
print(k)
print(type(k))

complex_number = 3+5.8j
print(type(complex_number))
print(complex_number.real)
print(complex_number.imag)

print(100*'-')
print(dir())
print(dir(__builtins__))
print(help(pow))
print(pow(2,3))
print(pow(2,3,4))
print(help(hex))
print(hex(10))

print(100*'-')
# print(help('modules'))
import math
print(help(math.radians))
print(math.radians(180))

print(100*'-')
import datetime
print(dir(datetime))
help(datetime.date)
gvr = datetime.date(1956, 1, 31) #birth date of Python Founder - Guido van Rossum
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(dt+mill)
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVR was born on {:%A, %B %d, %Y}"
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_landing = "7/20/1969"
print(datetime.datetime.strptime(moon_landing, "%m/%d/%Y"))
print(type(datetime.datetime.strptime(moon_landing, "%m/%d/%Y")))
