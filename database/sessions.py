from sqlalchemy.orm.session import Session
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def create_session() -> Session:
  engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)
  if config.get('APP', 'Debug') == 'True':
    engine.echo = True

  Session = sessionmaker(bind=engine)
  session = Session()

  return session
