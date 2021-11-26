from typing import Dict, List
from connectionSearch.line import Line
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

class Lines:

  _lines: Dict[LineName, Line]

  def __init__(self, lines: Dict[LineName, Line]) -> None:
    self._lines = lines

  def updateReachable(self, lines: List[LineName], stop: StopName, time: Time) -> None:
    for line in lines:
      if line not in self._lines: continue
      self._lines[line].updateReachable(time, stop)

  def updateCapacityAndGetPreviousStop(self, line: LineName, stop: StopName, time: Time) -> StopName:
    if line not in self._lines:
      raise Exception("Line " + line.name + " passed as an argument was not found.")

    return self._lines[line].updateCapacityAndGetPreviousStop(stop, time)
