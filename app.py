from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact, event, lead
from models.base import Base
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from utils import create_db


app = FastAPI()
create_db()
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router)
app.include_router(event.router)
app.include_router(lead.router)

# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base.metadata.create_all(engine)
