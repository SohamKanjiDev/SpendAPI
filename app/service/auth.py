from passlib.context import CryptContext

class AuthService:
    """
    This is the auth service, responsible for creating hashed passwords, verifying, etc. 
    """

    def __init__(self) -> None:
        """
        Initialise auth service class.
        """
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def hashPassword(self, password: str) -> str:
        """
        Returns the hashed password for the passed password.

        :param password: The normal password that we want to hash.
        :return: The hashed password. 
        """
        return self._pwd_context.hash(password)
    
    def verifyPassword(self, password: str, hashed_password: str) -> bool:
        """
        Verifies the given password with the hashed password.

        :param password: The password we want to verify.
        :hashed_password: The hashed password we will verify against. 

        :return: True if the password is same.
        """ 
        return self._pwd_context.verify(password, hashed_password)
