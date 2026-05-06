from models.transaction import Transaction
from sqlalchemy import func

def get_transactions(db):
    return db.query(Transaction).all()

def get_transaction_by_id(db, transaction_id):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def create_transaction(db, data):
    transaction = Transaction(**data)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def update_transaction(db, transaction_id, data):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None

    for key, value in data.items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db, transaction_id):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()
    return {"message": "Transação deletada"}

#DASHBOARD
def get_expense_by_category(db):
    result = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(
        Transaction.transaction_type == "expense"
    ).group_by(
        Transaction.category
    ).all()

    return [
        {"category": c, "total": float(t)}
        for c, t in result
    ]

def get_dashboard(db):
    income = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.transaction_type == "income")\
        .scalar() or 0

    expense = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.transaction_type == "expense")\
        .scalar() or 0

    return {
        "summary": {
            "income": float(income),
            "expense": float(expense),
            "balance": float(income - expense)
        },
        "by_category": get_expense_by_category(db)
    }