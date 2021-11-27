from typing import Dict, Optional, Tuple

from connectionSearch.datatypes.time import TimeDiff, Time
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.stop import StopInterface

from connectionSearch.stops import StopsInterface

class LineSegmentInterface:

  _timeToNextStop: TimeDiff
  _numberOfPassengers: Dict[Time, int]
  _capacity: int
  _lineName: LineName
  _nextStop: StopName
  _stops: StopsInterface

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    pass

  def nextStopAndUpdateReachable(self, startTime: Time) -> Tuple[Time, StopName, bool]:
    pass

  def incrementCapacity(self, time: Time) -> None:
    pass

  @property
  def nextStopOnly(self) -> StopName:
    pass

class LineSegmentFactory:

  def create(self, timeToNext: TimeDiff, capacity: int, line: LineName, next: StopName, stops: StopsInterface) -> LineSegmentInterface:
    return LineSegment(timeToNext, capacity, line, next, stops)

class LineSegment(LineSegmentInterface):

  def __init__(self, timeToNext: TimeDiff, capacity: int, line: LineName, next: StopName, stops: StopsInterface) -> None:
    self._timeToNextStop = timeToNext
    self._numberOfPassengers = {}
    self._capacity = capacity
    self._lineName = line
    self._nextStop = next
    self._stops = stops

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    return (startTime + self._timeToNextStop, self._nextStop)

  def nextStopAndUpdateReachable(self, startTime: Time) -> Tuple[Time, StopName, bool]:
    if startTime not in self._numberOfPassengers:
      self._numberOfPassengers[startTime] = 0

    nextStopResult: Tuple[Time, StopName] = self.nextStop(startTime)
    if self._capacity - self._numberOfPassengers[startTime] == 0:
      return (nextStopResult[0], nextStopResult[1], False)
    nextStop: StopInterface = self._stops.getByName(self._nextStop)
    nextStop.updateReachableAt(nextStopResult[0], self._lineName)
    return (nextStopResult[0], nextStopResult[1], True)

  def incrementCapacity(self, time: Time) -> None:
    startTime: Time = time - self._timeToNextStop
    if startTime not in self._numberOfPassengers:
      self._numberOfPassengers[startTime] = 0

    self._numberOfPassengers[startTime] += 1

  @property
  def nextStopOnly(self) -> StopName:
    return self._nextStop
