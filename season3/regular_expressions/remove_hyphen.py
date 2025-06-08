import re

pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3"
user_input = input("Enter your phone number in the format xxx-xxx-xxxx: ")
user_input = user_input.strip()
if re.search(pattern, user_input):
      new_number = re.sub(pattern, new_pattern, user_input)
      print(f"Your phone number without hyphens is: {new_number}")
else:
      print("Invalid phone number format. Please use xxx-xxx-xxxx.")
