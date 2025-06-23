# multiprocessing
'''
multiprocessing running tasks in parallel on different cpu cores.
multiprocessing is better for CPU bound tasks (heavy cpu usgae )
multithreading is better for io bound tasks (waiting around)
'''
import multiprocessing 

def counter(num):
      count = 0
      while count < num:
            count +=1

def main():
      a = Process(target = counter, args=(10000000,))

      b = Process(target = counter, args=(10000000,))

      a.start()
      a.start()

      a.join()
      b.join()

      print("finished in: ")

if __name__ == '__main__':
      main()
