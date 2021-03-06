from sqlalchemy import Column, BigInteger, String, sql

from src.utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    language = Column(String(2))
    apples = Column(BigInteger)
    query: sql.Select
