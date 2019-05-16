from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, Boolean, SmallInteger, DateTime
from config import config


a = "mysql+mysqlconnector://{}:{}@{}:{}/TEST?charset=utf8".format(*config['company_config'].sql())
print(a)

engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/TEST".format(*config['company_config'].sql()))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

Base.metadata.create_all(engine)