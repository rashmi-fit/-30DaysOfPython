class Test:
      pass

print(Test)
print(Test())

print(type(Test()))

print(type(2))

# print(type())

print(type(Test))

Test = type('Test', (), {})

t = Test()
t.wy = "hello"
print(t.wy)
# t.show()
