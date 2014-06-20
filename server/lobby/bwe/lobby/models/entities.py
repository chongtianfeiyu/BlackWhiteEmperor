from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Player(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    name = Column(String(30))
    password = Column(String(32))
    played_games = Column(Integer)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
