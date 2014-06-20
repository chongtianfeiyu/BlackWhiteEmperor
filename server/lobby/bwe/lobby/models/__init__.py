from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///bwe.db')
Maker = sessionmaker(bind=engine)
def get_session():
    return Maker()
