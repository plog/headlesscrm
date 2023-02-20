from database import Base, engine

def create_db():
    Base.metadata.create_all(bind=engine)
