from collections import deque

stack = deque()

# stack.append("www.google.com")

# stack.append("www.yahoo.com")

class Stack:
      def __init__(self):
            self.container = deque()

      def push(self, val):
            self.container.append(val)

      def pop(self):
            return self.container.pop()

      def peek(self):
            return self.container[-1]

      def is_empty(self):
            return len(self.container)== 0

      def size(self):
            return len(self.container)

s = Stack()

s.push("www.google.com")
s.push("www.yahoo.com")
s.push("www.facebook.com")
s.push("www.youtube.com")

s.pop()

s.is_empty()
s.peek()
s.size()
