from typing import Dict, Optional, Tuple

from sqlalchemy.orm.session import Session

from connectionSearch.datatypes.time import TimeDiff, Time
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.stop import StopInterface

from connectionSearch.stops import StopsInterface

from database.setup import LineSegmentDB, PassengerDB

class LineSegmentInterface:

  _timeToNextStop: TimeDiff
  _numberOfPassengers: Dict[Time, int]
  _capacity: int
  _lineName: LineName
  _nextStop: StopName
  _stops: StopsInterface
  _dbObj: Optional[LineSegmentDB]

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    pass

  def nextStopAndUpdateReachable(self, startTime: Time) -> Tuple[Time, StopName, bool]:
    pass

  def incrementCapacity(self, time: Time, session: Optional[Session] = None) -> None:
    pass

  @property
  def nextStopOnly(self) -> StopName:
    pass

  def setPassengers(self, passengers: Dict[Time, int]) -> None:
    pass

  def setDBObj(self, dbObj: LineSegmentDB) -> None:
    pass

class LineSegmentFactory:

  @staticmethod
  def create(timeToNext: TimeDiff, capacity: int, line: LineName, nextStop: StopName, stops: StopsInterface) -> LineSegmentInterface:
    return LineSegment(timeToNext, capacity, line, nextStop, stops)

class LineSegment(LineSegmentInterface):

  def __init__(self, timeToNext: TimeDiff, capacity: int, line: LineName, nextStop: StopName, stops: StopsInterface) -> None:
    self._timeToNextStop = timeToNext
    self._numberOfPassengers = {}
    self._capacity = capacity
    self._lineName = line
    self._nextStop = nextStop
    self._stops = stops
    self._dbObj = None

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    return (startTime + self._timeToNextStop, self._nextStop)

  def nextStopAndUpdateReachable(self, startTime: Time) -> Tuple[Time, StopName, bool]:
    if startTime not in self._numberOfPassengers:
      self._numberOfPassengers[startTime] = 0

    nextStopResult: Tuple[Time, StopName] = self.nextStop(startTime)
    if self._capacity - self._numberOfPassengers[startTime] <= 0:
      return (nextStopResult[0], nextStopResult[1], False)
    nextStop: StopInterface = self._stops.getByName(self._nextStop)
    nextStop.updateReachableAt(nextStopResult[0], self._lineName)
    return (nextStopResult[0], nextStopResult[1], True)

  def incrementCapacity(self, time: Time, session: Optional[Session] = None) -> None:
    if self._dbObj is not None:
      self._dbObj.passengers.append(PassengerDB(time=(time - self._timeToNextStop).seconds))
      if session is not None:
        session.add(self._dbObj)
        return
      raise Exception("Session is None")
    startTime: Time = time - self._timeToNextStop
    if startTime not in self._numberOfPassengers:
      self._numberOfPassengers[startTime] = 0

    self._numberOfPassengers[startTime] += 1

  @property
  def nextStopOnly(self) -> StopName:
    return self._nextStop

  def setPassengers(self, passengers: Dict[Time, int]) -> None:
    self._numberOfPassengers = passengers

  def setDBObj(self, dbObj: LineSegmentDB) -> None:
    self._dbObj = dbObj
