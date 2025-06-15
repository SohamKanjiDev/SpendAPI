from app.unit_of_work.uow import UOW
from app.service.auth import AuthService
from app.service.token import JWTGenerator
from app.db.user import User
from typing import Callable

class UserService:
    """
    UserService deals with higher level logic related to 
    user manangement.
    """
    def __init__(self, uow_factory : Callable[[], UOW]):
        """
        Constructor for user service.

        :param uow_factory: Unit of work factory which we will use a context manager.
        """
        self._uow_factory = uow_factory

    def createUser(self, username: str, name: str, email: str, password: str) -> User:
        """
        Creates and returns the user object created.

        :param username: username for the new user.
        :param name: name for the user.
        :param email: email for the new user.
        :param password: password for the new user.
        """
        with self._uow_factory() as uow:
            auth_service = AuthService()
            return uow.user_repo.createUser(username, name, email, auth_service.hashPassword(password))
    
    def getUsers(self) -> list[User]:
        """
        Get all users.
        """
        with self._uow_factory() as uow:
            return uow.user_repo.getAllUsers()
    
    def getByUsername(self, username: str) -> User:
        """
        Get user by username.

        :param username: is the username.
        :return: the corresponding user object.
        """
        with self._uow_factory() as uow:
            user =  uow.user_repo.getUserByUsername(username)
            if user is None:
                raise ValueError("User not found.")
            return user
    
    def loginUser(self, username: str, password: str) -> str:
        """
        Creates a token for the user and returns it.

        :param username: username of the user we want to login as.
        :param password: password of the user we want to login as.
        """
        with self._uow_factory() as uow:
            user = uow.user_repo.getUserByUsername(username)
            if user is None:
                raise ValueError("User not found.")
            auth_service = AuthService()
            if not auth_service.verifyPassword(password, user.hashed_password):
                raise ValueError("Wrong password.")
            token_generator = JWTGenerator()
            return token_generator.getToken(username)

