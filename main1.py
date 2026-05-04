from models import Transaction
from tracker import FinanceTracker


def display_menu() -> None:
    print("\n=== Personal Finance Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. View summary")
    print("5. Exit")


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
    summary = tracker.get_summary()

    print("\n--- Account Summary ---")
    print(f"Total Income: £{summary.total_income:.2f}")
    print(f"Total Expenses: £{summary.total_expenses:.2f}")
    print(f"Balance: £{summary.balance:.2f}")


def main() -> None:
    tracker = FinanceTracker()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            tx = get_transaction_input("income")
            tracker.add_transaction(tx)
            print("Income added.")

        elif choice == "2":
            tx = get_transaction_input("expense")
            tracker.add_transaction(tx)
            print("Expense added.")

        elif choice == "3":
            print_transactions(tracker)

        elif choice == "4":
            print_summary(tracker)

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()