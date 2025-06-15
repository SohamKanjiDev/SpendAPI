from sqlalchemy.orm import Session
from app.enums.finance_type import ExpensesCategory
from app.db.expense import Expense


class ExpenseRepository:
    """
    This class handles db logic for Expenses table.
    """
    def __init__(self, db: Session):
        """
        Constructor.

        db: Session object.
        """
        self._db = db 

    def create(self, finance_id: int, category: ExpensesCategory) -> None:
        """
        Creates expense record with the given category.

        :param finance_id: is the finance id corresponding to this expense.
        :param category: is the expense category.
        """
        expense = Expense(type=category, finance_id=finance_id)
        self._db.add(expense)
        
    def filterByCategory(self, category: ExpensesCategory) -> list[Expense]:
        """
        Filter expenses by category.

        :param category: is the category we want to filter expense by.
        :return: the list of filtered expenses.
        """
        return self._db.query(Expense).filter(category == Expense.type)