print("================================")
print("     💰 STUDENT EXPENSE TRACKER")
print("================================")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Categories")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        print("\nCategories:")
        print("1. Food")
        print("2. Travel")
        print("3. Education")
        print("4. Shopping")
        print("5. Other")

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Education",
            "4": "Shopping",
            "5": "Other"
        }

        category = categories.get(category_choice, "Other")

        expenses.append((name, amount, category))

        print("✅ Expense added!")

    elif choice == "2":
        print("\n===== YOUR EXPENSES =====")

        if len(expenses) == 0:
            print("No expenses added.")
        else:
            for name, amount, category in expenses:
                print(name, "- ₹", amount, "-", category)

    elif choice == "3":
        total = 0

        for name, amount, category in expenses:
            total += amount

        print("\n💰 Total Spending: ₹", total)

    elif choice == "4":
        print("\n===== CATEGORY SUMMARY =====")

        category_total = {}

        for name, amount, category in expenses:
            if category not in category_total:
                category_total[category] = 0

            category_total[category] += amount

        for category, total in category_total.items():
            print(category, "- ₹", total)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid choice!")
