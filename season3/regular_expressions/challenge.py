# Validate gmail addresses using regex
import re

pattern = "[a-zA-Z0-9]+@(gmail).(com)"

user_input = input("Enter your email address: ")

user_input = user_input.strip()
if re.search(pattern, user_input):
      print("Valid email address")
else:
      print("Invalid email address")
