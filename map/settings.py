from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

path = 'postgresql://postgres:postgres@map-db:5432/postgres'
 
# Engine の作成
Engine = create_engine(
  path,
  encoding="utf-8",
  echo=False
)

# Session の作成
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=Engine
)

Base = declarative_base()