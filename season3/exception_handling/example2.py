try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")

"""
try block asks for user input and tries to divide 100 by the input number.
except blocks handle ZeroDivisionError and ValueError.
else block runs if no exception occurs, displaying the result.
finally block runs regardless of the outcome, indicating the completion of execution.
"""
