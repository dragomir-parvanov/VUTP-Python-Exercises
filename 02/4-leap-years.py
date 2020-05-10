# Write a program that prints the next 20 leap years.

import datetime
import calendar
currentYear = datetime.datetime.now().year

for year in range(currentYear, currentYear + 21):
    if calendar.isleap(year):
        print("{0} is leap".format(year))
