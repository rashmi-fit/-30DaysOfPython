try:
    # Simulate risky calculation: incorrect type operation
    res = "100" / 20

except ArithmeticError:
    print("Arithmetic problem.")

except:
    print("Something went wrong!")
