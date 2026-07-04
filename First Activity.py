import datetime
import calendar

now = datetime.datetime.now()
print("Time now:", now)

print(calendar.calendar(now.year))