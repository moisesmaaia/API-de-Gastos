from fastapi import FastAPI
from database import Base, engine
from routes.transaction_routes import router
from models.transaction import Transaction  # 👈 IMPORTANTE

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)