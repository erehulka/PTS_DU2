from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import declarative_base, relationship, DeclarativeMeta
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table

engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)

Base: DeclarativeMeta = declarative_base()

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

  id = Column(Integer, primary_key=True)
  name = Column(String)
  first_stop = Column(String)
  dataset_id = Column(Integer, ForeignKey('datasets.id'))

  dataset = relationship('Dataset', back_populates='lines')

class StopDB(Base):

  __tablename__ = 'stops'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  lines = relationship("LineDB", secondary=association_table)
  dataset_id = Column(Integer, ForeignKey('datasets.id'))

  dataset = relationship('Dataset', back_populates='lines')
  
class StartTimeDB(Base):

  __tablename__ = 'start_times'

  id = Column(Integer, primary_key=True)
  time = Column(Integer)
  line_id = Column(Integer, ForeignKey("lines.id"))

  line = relationship("LineDB", back_populates='times')

class LineSegmentDB(Base):

  __tablename__ = 'lineSegments'

  id = Column(Integer, primary_key=True)
  timeToNext = Column(Integer)
  capacity = Column(Integer)
  line = Column(String)
  next = Column(String)
  line_id = Column(Integer, ForeignKey("lines.id"))

  line = relationship("LineDB", back_populates='line_segments')

class PassengerDB(Base):

  __tablename__ = 'passengers'
  
  id = Column(Integer, primary_key=True)
  time = Column(Integer)
  line_segment_id = Column(Integer, ForeignKey("lineSegments.id"))

  line_segment = relationship('LineSegmentDB', back_populates='passengers')

  def __repr__(self):
    return "<Passenger(time='%s')>" % (self.time)

LineSegmentDB.passengers = relationship('PassengerDB', order_by=PassengerDB.id, back_populates="line_segment")
LineDB.line_segments = relationship('LineSegmentDB', order_by=LineSegmentDB.id, back_populates='line')
LineDB.times = relationship('StartTimeDB', order_by=StartTimeDB.id, back_populates='line')
Dataset.lines = relationship('LineDB', order_by=LineDB.id, back_populates='dataset')
Dataset.stops = relationship('StopDB', order_by=StopDB.id, back_populates='dataset')

Base.metadata.create_all(engine)
