from app.db.database import Base 
from sqlalchemy import Column, Integer, Enum, ForeignKey
from app.enums.finance_type import ExpensesCategory
from sqlalchemy.orm import relationship

class Expense(Base):
    """
    DB model for storing information about expenses.
    """
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(ExpensesCategory, values_callable=lambda enum_class : [e.value for e in enum_class]))
    finance_id = Column(Integer, ForeignKey("finances.id"))

    finance = relationship("Finance", back_populates="expense")