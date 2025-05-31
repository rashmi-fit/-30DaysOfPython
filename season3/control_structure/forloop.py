# store monthly expenses in a list and find the total expenses

monthly_expenses = [200, 300, 150, 400, 250, 350]
total_expenses = 0
for expenses in monthly_expenses:
    total_expenses = total_expenses + expenses
print(f"Total monthly expenses: {total_expenses}")
