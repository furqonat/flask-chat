from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

env = dotenv_values(".env")

engine = create_engine(str(env["SQLALCHEMY_DATABASE_URI"]), echo=True)


BaseModel = declarative_base(bind=engine)
