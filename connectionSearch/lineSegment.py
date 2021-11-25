from typing import Dict, Optional, Tuple
from connectionSearch.stop import Stop
from connectionSearch.datatypes.time import TimeDiff, Time
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName


class LineSegment:

  _timeToNextStop: TimeDiff
  _numberOfPassengers: Dict[Time, int]
  _capacity: int
  _lineName: LineName
  _nextStop: Stop

  def __init__(self, timeToNext: TimeDiff, capacity: int, line: LineName, next: Stop) -> None:
    self._timeToNextStop = timeToNext
    self._numberOfPassengers = {}
    self._capacity = capacity
    self._lineName = line
    self._nextStop = next

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    return (startTime + self._timeToNextStop, self._nextStop.name)

  def nextStopAndUpdateReachable(self, startTime: Time) -> Tuple[Time, StopName, bool]:
    if startTime not in self._numberOfPassengers:
      self._numberOfPassengers[startTime] = 0

    nextStopResult: Tuple[Time, StopName] = self.nextStop(startTime)
    if self._capacity - self._numberOfPassengers[startTime] == 0:
      return (nextStopResult[0], nextStopResult[1], False)
    self._nextStop.updateReachableAt(nextStopResult[0], self._lineName)
    return (nextStopResult[0], nextStopResult[1], True)
