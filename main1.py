
# Filename: main.py
# Author: mv559 & kx304
# Description:
# This file provides a simple text-based menu so that the user can
# interact with the FinanceTracker class from the terminal.

from models import Transaction
from commands import AddTransactionCommand, RemoveLastTransactionCommand
from tracker import FinanceTracker


def display_menu() -> None:
    print("\n=== Personal Finance Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. View summary")
    print("5. View expenses by category")
    print("6. Remove last transaction")
    print("7. Exit")


def get_transaction_input(transaction_type: str) -> Transaction:
    category = input("Enter category: ").strip()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ").strip()

    return Transaction(transaction_type, category, amount, description)


def print_transactions(tracker: FinanceTracker) -> None:
    transactions = tracker.list_transactions()

    if not transactions:
        print("No transactions recorded.")
        return

    print("\n--- Transactions ---")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t.transaction_type.title()} | {t.category} | £{t.amount:.2f} | {t.description}")


def print_summary(tracker: FinanceTracker) -> None:
    s = tracker.get_summary()
    print("\n--- Account Summary ---")
    print(f"Total Income:   £{s.total_income:.2f}")
    print(f"Total Expenses: £{s.total_expenses:.2f}")
    print(f"Balance:        £{s.balance:.2f}")


def print_expenses_by_category(tracker: FinanceTracker) -> None:
    data = tracker.get_expenses_by_category()

    if not data:
        print("No expense categories recorded.")
        return

    print("\n--- Expenses by Category ---")
    for cat, total in data.items():
        print(f"{cat}: £{total:.2f}")


def main() -> None:
    tracker = FinanceTracker()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                tx = get_transaction_input("income")
                tracker.run_command(AddTransactionCommand(tx))
                print("Income added.")

            elif choice == "2":
                tx = get_transaction_input("expense")
                tracker.run_command(AddTransactionCommand(tx))
                print("Expense added.")

            elif choice == "3":
                print_transactions(tracker)

            elif choice == "4":
                print_summary(tracker)

            elif choice == "5":
                print_expenses_by_category(tracker)

            elif choice == "6":
                tracker.run_command(RemoveLastTransactionCommand())
                print("Last removed.")

            elif choice == "7":
                print("Exiting.")
                break

            else:
                print("Invalid option.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
