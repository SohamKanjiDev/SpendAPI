from app.repository.expense import ExpenseRepository
from app.repository.finance import FinanceRepository
from app.repository.user import UserRepository
from sqlalchemy.orm import Session

class UOW:
    """
    This sits between the repository layer and the service layer to ease out executing 
    transactions.
    """
    def __init__(self, session: Session):
        """
        Constructor for the UOW class.

        :param session: is the session object.
        """
        self._session = session
        self._user_repo = UserRepository(self._session)
        self._finance_repo = FinanceRepository(self._session)
        self._expense_repo = ExpenseRepository(self._session)

    @property
    def user_repo(self):
        return self._user_repo
    
    @property
    def finance_repo(self):
        return self._finance_repo
    
    @property
    def expense_repo(self):
        return self._expense_repo
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._session.rollback()
        else:
            self._session.commit()
        return False
        