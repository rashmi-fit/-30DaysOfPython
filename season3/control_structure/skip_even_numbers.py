# find square of numbers between 1-5 and skip the even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    square = i ** 2
    print(f"The square of {i} is {square}")
