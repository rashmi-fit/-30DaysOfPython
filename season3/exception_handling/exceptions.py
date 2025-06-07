while True:
      number1 = int(input('first number (division):'))
      number2 = int(input('second number (division):'))

try:
      result :int = number1 / number2
except ZeroDivisionError as e:
      print(f'Error: {e}')
      result = None
else:
      print(f'result: {result}')
