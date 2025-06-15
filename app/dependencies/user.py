from app.db.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.service.token import JWTGenerator
from app.service.user import UserService
from app.dependencies.uow import get_uow_factory
from app.unit_of_work.uow import UOW
from typing import Callable

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login_form")

def get_current_user(token : str = Depends(oauth2_scheme), uow_factory: Callable[[], UOW] = Depends(get_uow_factory)) -> User:
    """
    Get the current user based on the token data.
    
    :token: is the bearer token
    :db: is the UOW factory.
    :return: the current User object.
    """
    token_generator = JWTGenerator()
    username = token_generator.decodeToken(token)
    try :
        user_service = UserService(uow_factory)
        return user_service.getByUsername(username)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

