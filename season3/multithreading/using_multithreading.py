import time
import threading

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

t = time.time()

t1 = threading.Thread(target = cal_square, args= (arr,))

t2 = threading.Thread(target = calc_cube, args= (arr,))

t1.start()
t2.start()

t1.join()
t2.join()

# cal_square(arr)
# calc_cube(arr)

print(f'done in : { time.time() - t} seconds')
print(f'done with my work now!')
