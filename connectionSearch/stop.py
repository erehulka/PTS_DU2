from typing import List, Optional, Tuple

from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

from database.setup import StopDB

class StopInterface:

  _name: StopName
  _reachableAt: Optional[Time]
  _reachableVia: Optional[LineName]
  _lines: List[LineName]

  def updateReachableAt(self, time: Time, line: Optional[LineName]) -> None:
    raise NotImplementedError

  def clean(self) -> None:
    raise NotImplementedError

  @property
  def reachableAt(self) -> Tuple[Optional[Time], Optional[LineName]]:
    raise NotImplementedError

  @property
  def lines(self) -> List[LineName]:
    raise NotImplementedError

  @property
  def name(self) -> StopName:
    raise NotImplementedError

class StopFactory:

  @staticmethod
  def create(name: StopName, lines: List[LineName]) -> StopInterface:
    return Stop(name, lines)

  @staticmethod
  def createFromDB(stop: StopDB) -> StopInterface:
    lines: List[LineName] = [LineName(line.name) for line in stop.lines]
    return Stop(StopName(stop.name), lines)

class Stop(StopInterface):

  def __init__(self, name: StopName, lines: List[LineName]) -> None:
    self._name = name
    self._reachableAt = None
    self._reachableVia = None
    self._lines = lines

  def updateReachableAt(self, time: Time, line: Optional[LineName]) -> None:
    if self._reachableAt is None or time < self._reachableAt:
      self._reachableAt = time
      self._reachableVia = line

  def clean(self) -> None:
    self._reachableAt = None
    self._reachableVia = None

  @property
  def reachableAt(self) -> Tuple[Optional[Time], Optional[LineName]]:
    return (self._reachableAt, self._reachableVia)

  @property
  def lines(self) -> List[LineName]:
    return self._lines

  @property
  def name(self) -> StopName:
    return self._name
