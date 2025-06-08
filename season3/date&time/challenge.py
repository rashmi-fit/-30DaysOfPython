# Calculate the days between two dates

import datetime


today = datetime.date.today()
target_date = datetime.date(2025, 6, 12)
days_difference = (target_date - today).days
print(f"Days until target date: {days_difference}")
