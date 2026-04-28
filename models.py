# ============================================================
# Filename: models.py
# Author: Mike Vel
# Summary: Data models used by the personal finance tracker.
# Description:
# This file stores the grouped data classes used throughout the
# finance tracker project. These classes represent financial
# transactions and account summaries.
# ============================================================

from dataclasses import dataclass


@dataclass
class Transaction:
    transaction_type: str
    category: str
    amount: float
    description: str = ""


@dataclass
class AccountSummary:
    total_income: float
    total_expenses: float
    balance: float