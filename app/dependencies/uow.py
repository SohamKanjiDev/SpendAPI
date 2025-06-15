from app.db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.unit_of_work.uow import UOW
from typing import Callable

def get_uow_factory(session : Session = Depends(get_db)) -> Callable[[], UOW]:
    """
    Gets a UOW object instance.

    :param session: is the corresponding session object.
    """
    return lambda : UOW(session)