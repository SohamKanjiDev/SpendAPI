from enum import Enum

class FinanceType(Enum):
    """
    Types of finances.
    """
    DEBIT = "debit"
    CREDIT = "credit"

class ExpensesCategory(Enum):
    """
    Categories of finances
    """
    MISCELLANEOUS = "miscellaneous"
    FOOD = "food"
    TRAVEL = "travel"
    RENT = "rent"
    OUTING = "outing"
