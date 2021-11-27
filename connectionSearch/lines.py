from typing import Dict, List

from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

from connectionSearch.line import LineInterface

class LinesInterface:

  _lines: Dict[LineName, LineInterface]

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    pass

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    pass

class LinesFactory:

  def create(self, lines: Dict[LineName, LineInterface]) -> LinesInterface:
    return Lines(lines)

  def createDB(self) -> LinesInterface:
    return LinesDB()

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

  def __init__(self) -> None:
    self._lines = dict()

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines:
        # TODO Vyber z DB
        pass
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      # TODO Vyber z DB
      pass

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time)
