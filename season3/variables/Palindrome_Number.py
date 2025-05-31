#  Given an integer x, return true if x is a

# , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def palindrome():
    num = int(input("Enter a number to check if it's a palindrome: "))
    original = num
    reverse = 0

    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10  # Integer division

    return original == reverse

if palindrome():
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
