from fastapi import FastAPI
from app.db.user import Base
from app.db.database import engine
from app.api.user import router as user_router
from app.api.finance import router as finance_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(finance_router, prefix="/finances", tags=["finances"])

@app.get("/")
def root():
    return {"message" : "Hello"}