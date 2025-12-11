import csv
from datetime import datetime

# CSV file to store expenses
FILE_NAME = "expenses.csv"

# Initialize file if it does not exist
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "amount", "category", "description"])
    except FileExistsError:
        pass

# Add a new expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, Rent, etc.): ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

# View expenses by category
def view_by_category():
    category = input("Enter category name: ")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        found = False
        for row in reader:
            if row[2].lower() == category.lower():
                print(row)
                found = True
        if not found:
            print(f"No expenses found for category '{category}'")
    print()

# View total spending
def total_spending():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[1])
    print("Total Spending: ₹", total, "\n")

# Main menu
def main():
    initialize_file()
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Total Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            total_spending()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!\n")

if __name__ == "__main__":
    main()

