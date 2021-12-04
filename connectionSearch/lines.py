from typing import Dict, List

from sqlalchemy.orm.session import Session

from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

from connectionSearch.line import LineFactory, LineInterface
from connectionSearch.stops import StopsInterface

from database.queries import select_line_by_name_dataset
from database.setup import LineDB
from database.sessions import create_session

class LinesInterface:

  _lines: Dict[LineName, LineInterface]

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    pass

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    pass

  def clean(self) -> None:
    pass

class LinesFactory:

  @staticmethod
  def create(lines: Dict[LineName, LineInterface]) -> LinesInterface:
    return Lines(lines)

  @staticmethod
  def createDB(dataset: str, stops: StopsInterface) -> LinesInterface:
    return LinesDB(dataset, stops)

class Lines(LinesInterface):

  def __init__(self, lines: Dict[LineName, LineInterface]) -> None:
    self._lines = lines

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines:
        raise Exception("Line " + line.name + " passed as an argument was not found.")
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      raise Exception("Line " + line.name + " passed as an argument was not found.")

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time)

class LinesDB(LinesInterface):

  _dataset: str
  _stops: StopsInterface
  _session: Session

  def __init__(self, dataset: str, stops: StopsInterface) -> None:
    self._lines = dict()
    self._dataset = dataset
    self._stops = stops
    self._session = create_session()

  def get_from_db(self, name: str) -> None:
    line: LineDB = select_line_by_name_dataset(name, self._dataset)
    self._lines[LineName(name)] = LineFactory.createFromDb(line, self._stops)

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines:
        self.get_from_db(line.name)
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      self.get_from_db(line.name)

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time, self._session)

  def clean(self) -> None:
    self._session.commit()
    self._lines = dict()
