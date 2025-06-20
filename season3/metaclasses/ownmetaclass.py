class Meta(type):
      def __new__(self, class_name, bases, attrs):
            print(attrs)
            a = {}
            for name, val in attrs.items():
                  if name.startswith("__"):
                        a[name] = val
                  else:
                        a[name.upper()] = val

            print(a)
            return type(class_name, bases, attrs)

class Dog(metaclass = Meta):
      X = 5
      Y = 8

      def HELLO(self):
            print("hi")

d = Dog()
print(d.X)
print(d.HELLO())
