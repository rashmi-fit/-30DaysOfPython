double = lambda x: x* 2
print(double(5))


add = lambda x, y: x + y
print(add(5, 10))

max_value = lambda x, y: x if x > y else y
print(max_value(5, 10))
min_value = lambda x, y: x if x < y else y
print(min_value(5, 10))
multiply = lambda x, y: x * y
print(multiply(5, 10))

full_name = lambda first, last: f"{first} {last}"
print(full_name("John", "Doe"))

is_even = lambda x: x% 2 == 0
print(is_even(10))

age_check = lambda age: "Adult" if age >= 18 else "Minor"
print(age_check(20))
