from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.uow import get_uow_factory
from app.unit_of_work.uow import UOW
from app.service.user import UserService
from app.schema.user import CreateUserRequest, UserResponse, LoginUserRequest
from app.schema.token import LoginToken
from fastapi.security import OAuth2PasswordRequestForm
from typing import Callable

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user_request: CreateUserRequest, uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API route to create user.

    :param user_request: Request model for the API.
    :param uow_factory: UOW factory.
    """
    user_service = UserService(uow_factory)
    user_request_dict = user_request.model_dump()
    user = user_service.createUser(user_request_dict.get('username'), user_request_dict.get('name'), user_request_dict.get('email'), user_request_dict.get('password'))
    return UserResponse(username=user.username, name=user.name, email=user.email)

@router.post("/login", response_model=LoginToken)
def login_user(login_request: LoginUserRequest, uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API route to login as an user.

    :param login_request: Request model for the API.
    :param uow_factory: UOW factory.
    """
    try:
        user_service = UserService(uow_factory)
        token = user_service.loginUser(login_request.username, login_request.password)
        return LoginToken(access_token=token, token_type="bearer")
    except ValueError as ex:
        return HTTPException(
            status_code=401,
            detail=str(ex),
        )
    
@router.post('/login_form', response_model=LoginToken)
def login_user_form(form_data: OAuth2PasswordRequestForm = Depends(), uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API route to login as a user through form.

    :param form_data: is the form data.
    :param uow_factory: UOW factory.
    """
    try:
        user_service = UserService(uow_factory)
        token = user_service.loginUser(form_data.username, form_data.password)
        return LoginToken(access_token=token, token_type="bearer")
    except ValueError as ex:
        return HTTPException(
            status_code=401,
            detail=str(ex),
        )
    

@router.get("/", response_model=list[UserResponse])
def get_users(uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API route to get users.

    :param uow_factory: UOW factory.
    """
    user_service = UserService(uow_factory)
    users = user_service.getUsers()
    return [UserResponse(username=user.username, name=user.name, email=user.email) for user in users]

