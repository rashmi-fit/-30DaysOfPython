def decorator_function(original_function):
    def wrapper_function():
        print("Before the function runs")
        original_function()
        print("After the function runs")
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
