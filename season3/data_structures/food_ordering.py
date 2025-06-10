import threading
import time
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def peek(self):
        return self.buffer[-1] if not self.is_empty() else None

food_order_queue = Queue()

def place_order(orders):
      for order in orders:
          food_order_queue.enqueue(order)
          print(f"Order placed: {order}")
def serve_orders():
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        if order:
            print(f"Processing order: {order}")
            time.sleep(1)
        else:
            print("No orders to process.")

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
