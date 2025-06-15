from app.db.finance import Finance
from sqlalchemy.orm import Session
from app.enums.finance_type import FinanceType

class FinanceRepository:
    """
    Class to interact with finances db table.
    """
    
    def __init__(self, db: Session):
        """
        Constructor.

        :param db: the db session object.
        """
        self._db = db 
    
    def createFinance(self, name: str, type: FinanceType, amount: float, user_id: int) -> Finance:
        """
        Creates an entry in the finance table with the given specs.

        :param name: Name of the entry.
        :param type: Type of finance.
        :param amount: Amount.
        :param user_id: Id of the user who is creating this finance entry.
        :return: The created Finance object.
        """
        finance = Finance(name=name, type=type, amount=amount, user_id=user_id)
        self._db.add(finance)
        self._db.flush()
        self._db.refresh(finance)
        return finance
    
    def getFinancesByUserID(self, user_id:int) -> list[Finance]:
        """
        Get the finance entries for a particular user.

        :param user_id: ID of the concerned user.
        :return: List of finance objects.
        """
        return self._db.query(Finance).filter(user_id == Finance.user_id)
    
    def getDebitsByUserID(self, user_id:int) -> list[Finance]:
        """
        Get the finance entries for a particular user which are debits.

        :param user_id: ID of the concerned user.
        :return: List of finance objects.
        """
        return self._db.query(Finance).filter((user_id == Finance.user_id) & (Finance.type==FinanceType.DEBIT))