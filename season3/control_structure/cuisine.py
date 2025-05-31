# write a program that asks the user to input a cuisine type and then prints a message based on the input

Itallian = ["pasta", "pizza", "risotto"]
Chinese = ["noodles", "dumplings", "fried rice"]
Indian = ["curry", "biryani", "samosa"]
cusione = input("Enter the cuisine type:").lower()
if cusione in Itallian:
    print(f'You liked this Itallian cuisone {cusione}')
elif cusione in Chinese:
    print(f'You liked this Chinese cuisone {cusione}')
elif cusione in Indian:
    print(f'You liked this Indian cuisone {cusione}')
else:
      print(f'You liked this cuisone {cusione}, but it is not in our list of cuisines.')
