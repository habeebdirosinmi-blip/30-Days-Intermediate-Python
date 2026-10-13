from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Timestamp: {timestamp}")
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Formatted date:", formatted_date)
from datetime import datetime

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
from datetime import datetime

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1) 
time_difference = new_year - now

print("Time left for new year:", time_difference)
from datetime import datetime

epoch = datetime(1970, 1, 1)
now = datetime.now()
time_difference = now - epoch

print("Time difference between 1 January 1970 and now:", time_difference)