from app.unit_of_work.uow import UOW
from app.enums.finance_type import FinanceType, ExpensesCategory
from app.db.finance import Finance
from typing import Callable

class FinanceService:
    """
    Higher level interface which interacts with FinanceRepository
    """
    def __init__(self, uow_factory: Callable[[], UOW]):
        """
        Constructor for FinanceService class.

        :param uow_factory: Unit of work factory which we will use a context manager.
        """
        self._uow_factory = uow_factory

    def create(self, name: str, type: FinanceType, amount: float, user_id: int, expense_type: ExpensesCategory = None) -> Finance:
        """
        Creates an entry in the finance table with the given specs.

        :param name: Name of the entry.
        :param type: Type of finance.
        :param amount: Amount.
        :param user_id: Id of the user who is creating this finance entry.
        :param expense_type: Expense type if it's a debit type finance.
        :return: The created Finance object.
        """
        with self._uow_factory() as uow:
            result = uow.finance_repo.createFinance(name, type, amount, user_id)
            if type == FinanceType.DEBIT:
                uow.expense_repo.create(result.id, expense_type.value)
            return result
    
    def getByUserID(self, user_id: int) -> list[Finance]:
        """
        Get the finance entries for a particular user.

        :param user_id: ID of the concerned user.
        :return: List of finance objects.
        """
        with self._uow_factory() as uow:
            return uow.finance_repo.getFinancesByUserID(user_id)
    
    def getDebitsByUserID(self, user_id: int) -> list[Finance]:
        """
        Get the finance entries for a particular user which are debits.

        :param user_id: ID of the concerned user.
        :return: List of finance objects.
        """
        with self._uow_factory() as uow:
            return uow.finance_repo.getDebitsByUserID(user_id)
    
        