import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def print_expense_table(expenses):
    print(f"\n{'ID':<4} | {'Date':<16} | {'Category':<12} | {'Amount':<8} | {'Description'}")
    print("-" * 65)
    for exp in expenses:
        print(f"{exp['id']:<4} | {exp['date']:<16} | {exp['category']:<12} | ${exp['amount']:<7.2f} | {exp['description']}")
    print("-" * 65)

def add_expense():
    expenses = load_expenses()
    
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
        
    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    if not category:
        category = "General"
        
    description = input("Enter description (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Successfully added expense of ${amount:.2f} under '{category}'.")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print_expense_table(expenses)

def search_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    query = input("Enter search keyword (description or category): ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
        
    results = [
        exp for exp in expenses 
        if query in exp['description'].lower() or query in exp['category'].lower()
    ]
    
    if not results:
        print(f"No expenses found matching '{query}'.")
        return
        
    print(f"\n--- Search Results for '{query}' ---")
    print_expense_table(results)

def filter_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    categories = sorted(list(set(exp['category'] for exp in expenses)))
    print("\nAvailable Categories:")
    for cat in categories:
        print(f"  - {cat}")
        
    cat_query = input("Enter category to filter by: ").strip().lower()
    results = [exp for exp in expenses if exp['category'].lower() == cat_query]
    
    if not results:
        print(f"No expenses found in category '{cat_query}'.")
        return
        
    print_expense_table(results)
    total = sum(exp['amount'] for exp in results)
    print(f"Total for category '{cat_query}': ${total:.2f}")

def view_monthly_totals():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    monthly_data = {}
    for exp in expenses:
        month_key = exp['date'][:7]  # Extracts "YYYY-MM"
        monthly_data[month_key] = monthly_data.get(month_key, 0) + exp['amount']
        
    print("\n--- Monthly Totals ---")
    for month in sorted(monthly_data.keys(), reverse=True):
        print(f"  {month}: ${monthly_data[month]:.2f}")
    print("-" * 25)

def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    list_expenses()
    try:
        exp_id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
        
    new_expenses = [exp for exp in expenses if exp['id'] != exp_id]
    
    if len(new_expenses) == len(expenses):
        print(f"No expense found with ID {exp_id}.")
        return
        
    for idx, exp in enumerate(new_expenses, start=1):
        exp['id'] = idx
        
    save_expenses(new_expenses)
    print(f"Expense ID {exp_id} deleted successfully.")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. List All Expenses")
        print("3. Search Expenses")
        print("4. Filter by Category")
        print("5. View Monthly Totals")
        print("6. Delete Expense")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            search_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            view_monthly_totals()
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()