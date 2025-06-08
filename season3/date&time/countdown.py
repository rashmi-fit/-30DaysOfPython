import datetime
from datetime import date, time, datetime as dt

today = date.today()
next_year = today.year + 1
print(next_year)

jan_first_next_year = date(next_year, 1, 1)
difference = jan_first_next_year - today
print(f"Days until next year: {difference.days}")

my_time = time.fromisoformat("15:33:08")
my_date = date(1990, 7, 14)
my_bday = dt.combine(my_date, my_time)
print(f"My birthday is on {my_bday.strftime('%Y-%m-%d %H:%M:%S')}")
