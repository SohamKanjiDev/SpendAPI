from app.db.user import User 
from sqlalchemy.orm import Session

class UserRepository:
    """
    This is the repository class for performing
    CRUD operations on the users table.
    """

    def __init__(self, db : Session):
        self._db = db 

    def createUser(self, username: str, name: str, email: str, hashed_password: str) -> User:
        user = User(username = username, name = name, email=email, hashed_password=hashed_password)
        self._db.add(user)
        self._db.flush()
        self._db.refresh(user)
        return user
    
    def getUserByUsername(self, username: str) -> User:
        return self._db.query(User).filter(username==User.username).first()
    
    def getAllUsers(self) -> User:
        return self._db.query(User)