from pydantic import BaseModel

class LoginToken(BaseModel):
    """
    This is the token data we get back when we login.
    """
    access_token: str 
    token_type: str