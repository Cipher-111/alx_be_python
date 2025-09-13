# Personal Finance Calculator

# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings (with 5% interest)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output Results
print(f"Your monthly savings are ${monthly_savings:}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings: }.")
