from sqlalchemy.ext.declarative import declarative_base

from app.settings import Session

base = declarative_base()

session = Session()
