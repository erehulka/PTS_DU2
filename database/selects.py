from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.setup import LineDB, Dataset, StopDB

def select_line_by_name_dataset(name: str, dataset: str) -> LineDB:
  engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)

  Session = sessionmaker(bind=engine)
  session = Session()

  line: LineDB = session.query(LineDB).join(Dataset).filter(Dataset.name == dataset) \
    .filter(LineDB.name == name).first()

  session.close()

  return line

def select_stop_by_name_dataset(name: str, dataset: str) -> StopDB:
  engine = create_engine('sqlite:///database/data.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)

  Session = sessionmaker(bind=engine)
  session = Session()

  stop: StopDB = session.query(StopDB).join(Dataset).filter(Dataset.name == dataset) \
    .filter(StopDB.name == name).first()

  session.close()

  return stop
