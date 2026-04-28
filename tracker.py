# ============================================================
# Filename: tracker.py
# Author: Mike Vel
# Summary: Core logic for the personal finance tracker.
# Description:
# This file contains the FinanceTracker class, which stores,
# validates, manages, and summarises all financial transactions.
# It uses helper methods to keep responsibilities separated and
# code readable.
# ============================================================

from typing import List, Dict
from models import Transaction, AccountSummary
from commands import FinanceCommand


class FinanceTracker:
    """
    A personal finance tracker for storing income and expenses.

    The tracker supports:
    - adding transactions
    - removing the last transaction
    - viewing all transactions
    - calculating summaries
    - grouping expenses by category

    Example:
        >>> tracker = FinanceTracker()
        >>> tracker._add_transaction(Transaction("income", "Salary", 1000.0, "Weekly pay"))
        >>> tracker._add_transaction(Transaction("expense", "Food", 50.0, "Groceries"))
        >>> summary = tracker.get_summary()
        >>> summary.balance
        950.0
    """

    def __init__(self):
        """
        Initialise an empty finance tracker.
        """
        self.transactions: List[Transaction] = []

    def run_command(self, command: FinanceCommand) -> None:
        """
        Execute a command object on this tracker.

        Args:
            command (FinanceCommand): A command that performs an action
                on the tracker.
        """
        command.execute(self)

    def _validate_transaction(self, transaction: Transaction) -> None:
        """
        Validate a transaction before adding it.

        Args:
            transaction (Transaction): The transaction to validate.

        Raises:
            ValueError: If the transaction type is invalid or the amount
                is not positive.
        """
        if transaction.transaction_type not in ("income", "expense"):
            raise ValueError("Transaction type must be 'income' or 'expense'.")

        if transaction.amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        if transaction.category.strip() == "":
            raise ValueError("Transaction category cannot be blank.")

    def _add_transaction(self, transaction: Transaction) -> None:
        """
        Add a validated transaction to the tracker.

        Args:
            transaction (Transaction): The transaction to add.
        """
        self._validate_transaction(transaction)
        self.transactions.append(transaction)

    def _remove_last_transaction(self) -> None:
        """
        Remove the most recent transaction from the tracker.

        Raises:
            ValueError: If there are no transactions to remove.
        """
        if not self.transactions:
            raise ValueError("There are no transactions to remove.")

        self.transactions.pop()

    def get_summary(self) -> AccountSummary:
        """
        Calculate the current financial summary.

        Returns:
            AccountSummary: Totals for income, expenses, and balance.

        Example:
            >>> tracker = FinanceTracker()
            >>> tracker._add_transaction(Transaction("income", "Salary", 1000.0, "Job"))
            >>> tracker._add_transaction(Transaction("expense", "Travel", 100.0, "Bus pass"))
            >>> tracker.get_summary().balance
            900.0
        """
        total_income = 0.0
        total_expenses = 0.0

        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                total_income += transaction.amount
            else:
                total_expenses += transaction.amount

        balance = total_income - total_expenses
        return AccountSummary(total_income, total_expenses, balance)

    def get_expenses_by_category(self) -> Dict[str, float]:
        """
        Calculate total expenses for each category.

        Returns:
            dict[str, float]: A dictionary mapping each expense category
            to its total amount.

        Example:
            >>> tracker = FinanceTracker()
            >>> tracker._add_transaction(Transaction("expense", "Food", 10.0, "Lunch"))
            >>> tracker._add_transaction(Transaction("expense", "Food", 15.0, "Dinner"))
            >>> tracker.get_expenses_by_category()["Food"]
            25.0
        """
        category_totals: Dict[str, float] = {}

        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                if transaction.category not in category_totals:
                    category_totals[transaction.category] = 0.0

                category_totals[transaction.category] += transaction.amount

        return category_totals

    def list_transactions(self) -> List[Transaction]:
        """
        Return a copy of the transaction list.

        Returns:
            list[Transaction]: All stored transactions.
        """
        return self.transactions.copy()