from sqlalchemy import Column, Integer, Float, String, Date
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    transaction_type = Column(String(50))
    category = Column(String(100))
    date = Column(Date)