from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mycontacts.db', echo=True)
Base = declarative_base()


class Contact(Base):
    """"""
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    birthday = Column(String)
    email = Column(String)
    profession = Column(String)
    interests = Column(String)
    phone_number = Column(String)


class User(Base):
    """"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(80))


# create tables
Base.metadata.create_all(engine)
