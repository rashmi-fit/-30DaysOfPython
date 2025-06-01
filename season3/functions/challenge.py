# Write a function that computes the sum and average of a list of numbers
def sum_and_average(numbers):
      total = sum(numbers)
      average = total / len(numbers) if numbers else 0
      return total, average

numbers = [10, 20, 30, 40, 50]
total, average = sum_and_average(numbers)
print(f"Sum: {total}, Average: {average}")

    """
    This function takes a list of numbers and returns the sum and average.

    :param numbers: List of numbers
    :return: Tuple containing the sum and average
    """
