from fastapi import APIRouter, Depends
from app.dependencies.user import get_current_user
from app.db.user import User
from app.service.finance import FinanceService
from app.unit_of_work.uow import UOW
from app.dependencies.uow import get_uow_factory
from app.schema.finance import FinanceReponse, CreateFinanceRequest
from fastapi.responses import StreamingResponse
from app.service.file_exporter import FileExporter
from typing import Callable

router = APIRouter()

@router.get("/", response_model=list[FinanceReponse])
def get_finances(user: User = Depends(get_current_user), uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API to get the finances for the current user.

    :param user: is the current user.
    :param uow_factory: is the UOW factory.
    """
    finance_service = FinanceService(uow_factory)
    finances = finance_service.getByUserID(user.id)
    return [FinanceReponse(name=finance.name, amount=finance.amount, type=finance.type, username=user.username) for finance in finances]

@router.get("/csv")
def get_finances_csv(user: User = Depends(get_current_user), uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API to get the finances for the current user in csv format.

    :param user: is the current user.
    :param uow_factory: is the UOW factory.
    """
    finance_service = FinanceService(uow_factory)
    finances = finance_service.getByUserID(user.id)
    data = [[finance.name, finance.amount, finance.type.value] for finance in finances]
    exporter = FileExporter(["Name", "Amount", "Type"], data)
    file_name = f"{user.username}_report.csv"
    return StreamingResponse(
        exporter.getCSVString(),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={file_name}"})

@router.get("/csv/expenses")
def get_expenses_csv(user: User = Depends(get_current_user), uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API to get the expenses for the current user in csv format.

    :param user: is the current user.
    :param uow_factory: is the UOW factory.
    """
    finance_service = FinanceService(uow_factory)
    expenses = finance_service.getDebitsByUserID(user.id)
    data = [[expense.name, expense.amount, expense.expense.type.value] for expense in expenses]
    exporter = FileExporter(["Name", "Amount", "Category"], data)
    file_name = f"{user.username}_expense_report.csv"
    return StreamingResponse(
        exporter.getCSVString(),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={file_name}"}
    )

@router.post("/", response_model=FinanceReponse)
def create_finance(request: CreateFinanceRequest, user: User = Depends(get_current_user), uow_factory : Callable[[], UOW] = Depends(get_uow_factory)):
    """
    API to create a finance entry for the current user.

    :param user: is the current user.
    :param uow_factory: is the UOW factory.
    """
    finance_service = FinanceService(uow_factory)
    finance = finance_service.create(name=request.name, amount=request.amount, type=request.type, user_id=user.id, expense_type=request.expense_type)
    return FinanceReponse(name=finance.name, amount=finance.amount, type=finance.type, username=user.username)
