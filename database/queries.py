from typing import Optional
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.setup import LineDB, Dataset, StopDB

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def select_line_by_name_dataset(name: str, dataset: str) -> Optional[LineDB]:
  engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)
  if config.get('APP', 'Debug') == 'True':
    engine.echo = True

  Session = sessionmaker(bind=engine)
  session = Session()

  line: Optional[LineDB] = session.query(LineDB).join(Dataset).filter(Dataset.name == dataset) \
    .filter(LineDB.name == name).first()

  session.close()

  return line

def select_stop_by_name_dataset(name: str, dataset: str) -> Optional[StopDB]:
  engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)
  if config.get('APP', 'Debug') == 'True':
    engine.echo = True

  Session = sessionmaker(bind=engine)
  session = Session()

  stop: Optional[StopDB] = session.query(StopDB).join(Dataset).filter(Dataset.name == dataset) \
    .filter(StopDB.name == name).first()

  session.close()

  return stop
