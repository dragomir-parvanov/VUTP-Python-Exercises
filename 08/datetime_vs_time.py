# In python docs study for 'datetime' and 'time' modules regarding different
# features , formats , methods , etc.
# Write some example programs on this matter.

import time

import datetime


# module "time" is commonly used to measure time and deal with time stamps


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

# or blocking the application from execution for a period of time
print("before sleep")
time.sleep(2)
print("after sleep")

# some low level API
time.clock_settime_ns  # which does NOT work on windows

# also it can be used to actually print formatted dates!
t = time.time()
print(time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(t)))


print(time.strftime('%Y-%m-%d %H:%M %Z', time.gmtime(t)))


# datetime module

# The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
# While date and time arithmetic is supported, the focus of the "datetime"
# implementation is on efficient attribute extraction for output formatting and manipulation.

# "datetime" module greatly differs from "time" with being focused around manipulating dates, not mainly on time stamps
datetime.date(2000, 12, 3)

# but hey, "datetime" module uses "time" module on some of his functions.
datetime.datetime.today()  # Construct a date from time.time().

# so "datetime" module is built on top of some "time" module functions

# "datetime" can easily calculate time difference between dates
datetime.timedelta

d0 = datetime.date(2008, 8, 18)
d1 = datetime.date(2008, 9, 26)
delta = d1 - d0
print(delta.days)
