#Expense Tracker App in Python

import csv
import os

FILENAME = 'expenses.csv'

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Note'])

def add_expense():
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    note = input("Enter a note (optional): ")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added.")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print(f"{'Date':20s} | {'Category':10s} | {'Amount':8s} | Note")
        print('-' * 60)
        for row in reader:
            print(f"{row[0]:20s} | {row[1]:10s} | {row[2]:8s} | {row[3]}")

def total_expenses():
    total = 0.0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                total += float(row[2])
            except ValueError:
                pass
    print(f"Total expenses: ${total:.2f}")

def filter_by_category():
    category = input("Enter category to filter: ").strip().lower()
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        print(f"{'Date':20s} | {'Category':10s} | {'Amount':8s} | Note")
        print('-' * 60)
        for row in reader:
            if row[1].strip().lower() == category:
                print(f"{row[0]:20s} | {row[1]:10s} | {row[2]:8s} | {row[3]}")

def menu():
    initialize_file()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
