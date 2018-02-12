#########################################################
# Basic Enumeration for different TransactionTypes#

from enum import Enum

class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
