def even_numbers():
      for num in range(2,11,2):  # Start at 2, go up to 10, step by 2
            yield num

for even in even_numbers():
      print(even)


# create a generator to yield even numbers from 2 to 10 using the yield keyword:
