# Calculate factorial recursively

def factorial(n):
      if n== 0 or n == 1:
          return 1
      else:
          return n * factorial(n - 1)
def main():
      number = int(input("Enter a number to calculate its factorial: "))
      if number < 0:
            print("Factorial is not defined for negative numbers.")
      else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
