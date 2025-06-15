from app.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship

class User(Base):
    """
    DB model for users.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    finances = relationship("Finance", back_populates="user")