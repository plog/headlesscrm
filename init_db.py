from models import Base
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from models import Base

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.drop_all(engine, checkfirst=True)
Base.metadata.create_all(engine, checkfirst=True)