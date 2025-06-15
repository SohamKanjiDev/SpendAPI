from app.db.database import Base 
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, REAL, Enum, ForeignKey
from app.enums.finance_type import FinanceType
from sqlalchemy.orm import relationship

class Finance(Base):
    """
    DB model for storing information about finances.
    """
    __tablename__ = "finances"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(REAL)
    type = Column(Enum(FinanceType, values_callable=lambda enum_class : [e.value for e in enum_class]))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    user = relationship("User", back_populates="finances")
    expense = relationship("Expense", back_populates="finance", uselist=False)