from jose import jwt
from datetime import timedelta, timezone, datetime
import os
from jose.exceptions import ExpiredSignatureError

class TokenGenerator:
    """
    This is the general interface for generating tokens.
    Depends on base class on what strategy they want to use for 
    generating tokens. 
    """
    def getToken(self, to_encode: str) -> str:
        """
        Returns the token.

        :param to_encode: is the info we want to put in payload.
        :return: the generated token.
        """
        pass

    def decodeToken(self, token: str) -> str:
        """
        Return the decoded info.

        :param token: is the token.
        :return: the decoded info.
        """

class JWTGenerator(TokenGenerator):
    """
    This is the class for generating jwt tokens.
    """
    def getToken(self, to_encode: str) -> str:
        """
        Returns the token.

        :param username: is the info we want to put in payload.
        :return: the generated token.
        """
        SECRET = os.getenv("TOKEN_SECRET")
        DURATION = int(os.getenv("TOKEN_DURATION"))
        payload = {
            "sub": to_encode,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=DURATION)
        }
        return jwt.encode(payload, SECRET)
    
    def decodeToken(self, token: str) -> str:
        """
        Return the decoded info.

        :param token: is the token.
        :return: the decoded info.
        """
        SECRET = os.getenv("TOKEN_SECRET")
        try:
            payload = jwt.decode(token, SECRET)
        except ExpiredSignatureError:
            raise Exception("Token has expired")
        return payload.get("sub")


