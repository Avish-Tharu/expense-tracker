import json


try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== All Expenses =====")

    for expense in expenses:
        print(
            f"Amount: Rs.{expense['amount']} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']}"
        )


def expense_summary():
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    categories = {}

    for expense in expenses:
        total += expense["amount"]

        category = expense["category"]

        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]

    print("\n===== Expense Summary =====")
    print(f"\nTotal Expenses: Rs.{total}")

    for category, amount in categories.items():
        print(f"{category}: Rs.{amount}")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        expense_summary()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")