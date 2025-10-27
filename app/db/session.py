# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # MySQL connection URL (similar to your JDBC)
# # Format: mysql+pymysql://<username>:<password>@<host>/<database>
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root123@localhost:3306/bookify"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     echo=True,              # shows SQL like spring.jpa.show-sql=true
#     pool_pre_ping=True
# )
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
