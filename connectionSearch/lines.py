from typing import Dict, List

from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

from connectionSearch.line import LineFactory, LineInterface
from connectionSearch.stops import StopsInterface

from database.selects import select_line_by_name_dataset
from database.setup import LineDB

class LinesInterface:

  _lines: Dict[LineName, LineInterface]

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    pass

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    pass

class LinesFactory:

  def create(self, lines: Dict[LineName, LineInterface]) -> LinesInterface:
    return Lines(lines)

  def createDB(self, dataset: str, stops: StopsInterface) -> LinesInterface:
    return LinesDB(dataset, stops)

class Lines(LinesInterface):

  def __init__(self, lines: Dict[LineName, LineInterface]) -> None:
    self._lines = lines

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines: continue
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      raise Exception("Line " + line.name + " passed as an argument was not found.")

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time)

class LinesDB(LinesInterface):

  _dataset: str
  _stops: StopsInterface

  def __init__(self, dataset: str, stops: StopsInterface) -> None:
    self._lines = dict()
    self._dataset = dataset
    self._stops = stops

  def get_from_db(self, name: str) -> None:
    line: LineDB = select_line_by_name_dataset(name, self._dataset)
    lineFactory = LineFactory()
    self._lines[LineName(name)] = lineFactory.createFromDb(line, self._stops)

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines:
        self.get_from_db(line.name)
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      self.get_from_db(line.name)

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time)
