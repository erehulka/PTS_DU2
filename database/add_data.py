from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.setup import *

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)
if config.get('APP', 'Debug') == 'True':
  engine.echo = True

def create_dataset_basic():
  global engine
  try:
    Session = sessionmaker(bind=engine)
    session = Session()
    dataset_basic = Dataset(name='Basic')

    line1 = LineDB(name='1', first_stop='A')
    line1.line_segments = [
      LineSegmentDB(timeToNext=2, capacity=10, next='B'),
      LineSegmentDB(timeToNext=3, capacity=10, next='C'),
      LineSegmentDB(timeToNext=4, capacity=10, next='D'),
      LineSegmentDB(timeToNext=5, capacity=10, next='E'),
      LineSegmentDB(timeToNext=6, capacity=10, next='F')
    ]
    line1.times = [
      StartTimeDB(time=10),
      StartTimeDB(time=20),
      StartTimeDB(time=30),
    ]

    dataset_basic.lines = [line1]

    stop1 = StopDB(name='A')
    stop1.lines = [line1]
    stop2 = StopDB(name='B')
    stop2.lines = [line1]
    stop3 = StopDB(name='C')
    stop3.lines = [line1]
    stop4 = StopDB(name='D')
    stop4.lines = [line1]
    stop5 = StopDB(name='E')
    stop5.lines = [line1]
    stop6 = StopDB(name='F')
    stop6.lines = [line1]

    dataset_basic.stops = [
      stop1, stop2, stop3, stop4, stop5, stop6
    ]

    session.add(dataset_basic)
    session.commit()

    session.close()
  except:
    print(f'Error: This dataset (Basic) was already added')
