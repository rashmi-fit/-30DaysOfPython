import datetime

date =  datetime.date(2125, 6, 8)
today = datetime.date.today()
custom_time  = datetime.time(12, 30, 45)
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

print(date)

print(today)

print(custom_time)
print(now)

target_date = datetime.date (2025, 6, 12)
if target_date > today:
    print("Target date is in the future")
elif target_date < today:
    print("Target date is in the past")
else:
    print("Target date is today")
