from typing import List
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import declarative_base, relationship, DeclarativeMeta
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)
if config.get('APP', 'Debug') == 'True':
    engine.echo = True

Base: type = declarative_base()

class PassengerDB(Base):

  __tablename__ = 'passengers'
  
  id: int = Column(Integer, primary_key=True)
  time: int = Column(Integer)

  def __repr__(self):
    return "<Passenger(time='%s')>" % (self.time)

class LineSegmentDB(Base):

  __tablename__ = 'lineSegments'

  id: int = Column(Integer, primary_key=True)
  timeToNext: int = Column(Integer)
  capacity: int = Column(Integer)
  next: str = Column(String)
  passengers: List[PassengerDB] = relationship('PassengerDB', order_by=PassengerDB.id, back_populates="line_segment", lazy='subquery')

class StartTimeDB(Base):

  __tablename__ = 'start_times'

  id: int = Column(Integer, primary_key=True)
  time: int = Column(Integer)

class Dataset(Base):

  __tablename__ = 'datasets'

  id = Column(Integer, primary_key=True)
  name = Column(String, unique=True)

association_table = Table('association', Base.metadata,
    Column('line_id', ForeignKey('lines.id'), primary_key=True),
    Column('stop_id', ForeignKey('stops.id'), primary_key=True)
)

class LineDB(Base):

  __tablename__ = 'lines'

  id: int = Column(Integer, primary_key=True)
  name: str = Column(String)
  first_stop: str = Column(String)
  dataset_id: int = Column(Integer, ForeignKey('datasets.id'))
  times: List[StartTimeDB] = relationship('StartTimeDB', order_by=StartTimeDB.id, back_populates='line', lazy='subquery')
  line_segments: List[LineSegmentDB] = relationship('LineSegmentDB', order_by=LineSegmentDB.id, back_populates='line', lazy='subquery')

  dataset: Dataset = relationship('Dataset', back_populates='lines')

class StopDB(Base):

  __tablename__ = 'stops'

  id: int = Column(Integer, primary_key=True)
  name: str = Column(String)
  lines: List[LineDB] = relationship("LineDB", secondary=association_table, lazy='subquery', overlaps="stops")
  dataset_id: int = Column(Integer, ForeignKey('datasets.id'))

  dataset: Dataset = relationship('Dataset', back_populates='stops')

LineDB.stops = relationship("StopDB", secondary=association_table, lazy='subquery') # so pylance wont show errors
Dataset.lines = relationship('LineDB', order_by=LineDB.id, back_populates='dataset', lazy='subquery')
Dataset.stops = relationship('StopDB', order_by=StopDB.id, back_populates='dataset', lazy='subquery')

Base.metadata.create_all(engine)
