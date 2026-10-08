budget = float(input("Enter your monthly budget: "))
food = float(input("Food expense: "))
travel = float(input("Travel expense: "))
education = float(input("Education expense: "))

total = food + travel + education
remaining = budget - total

print("\n--- EXPENSE REPORT ---")
print("Total Expense:", total)
print("Remaining Budget:", remaining)

if remaining < 0:
    print("Warning: Budget exceeded!")
else:
    print("You are within your budget.")