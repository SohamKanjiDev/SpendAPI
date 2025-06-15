from pydantic import BaseModel, model_validator
from app.enums.finance_type import FinanceType, ExpensesCategory
from typing import Optional
from typing_extensions import Self

class CreateFinanceRequest(BaseModel):
    """
    Pydantic model for create request of a finance entry.
    """
    name : str
    amount : float
    type : FinanceType
    expense_type : Optional[ExpensesCategory] = None 

    @model_validator(mode='after')
    def validate_expense_type_if_debit(self) -> Self:
        if self.type == FinanceType.DEBIT and self.expense_type is None:
            raise ValueError("Expense Type is needed for debit type finance.")
        return self

class FinanceReponse(BaseModel):
    """
    Pydantic model for information about a particular finance.
    """
    name : str
    amount : float
    type : FinanceType
    username : str