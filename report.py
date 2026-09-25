print("================================")
print("       📊 SPENDING REPORT")
print("================================")

expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            name, amount, category = line.strip().split(",")
            expenses.append((name, float(amount), category))

except FileNotFoundError:
    print("No expense data found.")

if len(expenses) == 0:
    print("\nNo expenses available.")

else:
    total = sum(amount for name, amount, category in expenses)

    print("\n===== SUMMARY =====")
    print("Total Expenses: ₹", total)

    category_total = {}

    for name, amount, category in expenses:
        if category not in category_total:
            category_total[category] = 0

        category_total[category] += amount

    print("\n===== CATEGORY REPORT =====")

    for category, amount in category_total.items():

        percentage = (amount / total) * 100

        print("\n", category)
        print("Amount: ₹", amount)
        print("Percentage:", round(percentage, 2), "%")

        bars = int(percentage / 5)

        print("[" + "#" * bars + "]")
