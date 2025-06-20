class FOO:
      def show(self):
            print("hi")

def add_attribute(self):
      self.z = 9

Test = type('Test', (FOO,), {"x":5,"add_attribute": add_attribute})
t = Test()
t.add_attribute()
print(t.z)
