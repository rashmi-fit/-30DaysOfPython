import time

def cal_square(numbers):
      print("calculate square numbers")
      for i in numbers:
            time.sleep(0.2)
            print(f'square :({i}*{i}) = {i*i}')


def calc_cube(numbers):
      print("calculate square numbers")
      for i in numbers:
            time.sleep(0.2)
            print(f'cube :({i}*{i}*{i}) = {i*i*i}')

arr = [2,4,8,9]

t= time.time()
cal_square(arr)
calc_cube(arr)
