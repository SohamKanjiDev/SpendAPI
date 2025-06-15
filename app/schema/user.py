from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    """
    Pydantic model for create user request.
    """
    username: str 
    name: str 
    email: str
    password: str

class LoginUserRequest(BaseModel):
    """
    Pydantic model for login user request.
    """
    username: str 
    password: str

class UserResponse(BaseModel):
    """
    Pydantic model for user response information.
    """
    username: str 
    name: str 
    email: str