from typing import List, Optional, Tuple
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

class Stop:

  _name: StopName
  _reachableAt: Optional[Time]
  _reachableVia: Optional[LineName]
  _lines: List[LineName]

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
