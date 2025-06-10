from collections import deque

class Queue:
      def __init__(self):
            self.buffer = deque()

      def enqueue(self, val):
            self.buffer.appendleft(val)

      def dequeue(self):
            return self.buffer.pop()
      def is_empty(self):
            return len(self.buffer) == 0
      def size(self):
            return len(self.buffer)
      def peek(self):
            return self.buffer[-1] if not self.is_empty() else None

pq = Queue()

pq.enqueue({
            'company' :'Wal mart',
            'price': 135
            'timestamp' : '10:00 AM'
            })
