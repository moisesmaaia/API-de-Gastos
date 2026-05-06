from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Literal
from datetime import date
from database import SessionLocal
from services.transaction_service import (
    create_transaction,
    get_transactions,
    get_transaction_by_id,
    update_transaction,
    delete_transaction,
    get_dashboard
)

router = APIRouter()

# Schema 
class TransactionSchema(BaseModel):
    user_id: int
    amount: float
    transaction_type: Literal["income", "expense"]
    category: str
    date: date


# Conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/transactions")
def create_transaction_route(data: TransactionSchema, db: Session = Depends(get_db)):
    return create_transaction(db, data.model_dump())


# READ ALL
@router.get("/transactions")
def list_all(db: Session = Depends(get_db)):
    return get_transactions(db)


# READ BY ID
@router.get("/transactions/{transaction_id}")
def get_one(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_by_id(db, transaction_id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    return transaction


# UPDATE
@router.put("/transactions/{transaction_id}")
def update(transaction_id: int, data: TransactionSchema, db: Session = Depends(get_db)):
    transaction = update_transaction(db, transaction_id, data.model_dump())

    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    return transaction


# DELETE
@router.delete("/transactions/{transaction_id}")
def delete(transaction_id: int, db: Session = Depends(get_db)):
    result = delete_transaction(db, transaction_id)

    if not result:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    return result

#DASHBOARD
@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard(db)

