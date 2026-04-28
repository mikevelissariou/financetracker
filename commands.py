# ============================================================
# Filename: commands.py
# Author: Mike Vel
# Summary: Command classes for finance tracker actions.
# Description:
# This file implements the Command Pattern for adding and removing
# transactions. Commands are passed to the tracker so that actions
# are decoupled from the tracker itself.
# ============================================================

from abc import ABC, abstractmethod
from models import Transaction


class FinanceCommand(ABC):
    @abstractmethod
    def execute(self, tracker) -> None:
        pass


class AddTransactionCommand(FinanceCommand):
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    def execute(self, tracker) -> None:
        tracker._add_transaction(self.transaction)  # add tx


class RemoveLastTransactionCommand(FinanceCommand):
    def execute(self, tracker) -> None:
        tracker._remove_last_transaction()  # remove last