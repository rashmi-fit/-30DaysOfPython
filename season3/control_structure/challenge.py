# 🎯 Challenge
# - Check if a user-entered number is prime

def is_prime(num):
      if num <= 1:
          return False
      for i in range(2,int(num**.5)+1):
            if num % i == 0:
                return False
      return True

is_prime_number = int(input("Enter a number to check if it is prime: "))
if is_prime(is_prime_number):
    print(f"{is_prime_number} is a prime number.")
else:
    print(f"{is_prime_number} is not a prime number.")
