from typing import List, Tuple
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.lineSegment import LineSegment

class Line:

  _name: LineName
  _startingTimes: List[Time] # sorted
  _firstStop: StopName
  _lineSegments: List[LineSegment] # ordered

  def updateReachable(self, time: Time, stop: StopName) -> None:
    startingTime: Time = self._startingTimes[-1]
    currentStop: StopName = self._firstStop
    currentTime: Time
    i: int = 0
    while currentStop != stop:
      nextStopResult: Tuple[Time, StopName] = self._lineSegments[i].nextStop(startingTime)
      currentStop = nextStopResult[1]
      currentTime = nextStopResult[0]
      i += 1

    stopIndex: int = i

    if currentTime < time:
      raise Exception("There is no connection")

    self.updateReachables(stopIndex, currentTime)

    startingTimesIndex: int = len(self._startingTimes) - 1
    while(self.tryEarlier(time, currentTime - startingTime, startingTimesIndex)):
      self.updateReachables(stopIndex, self._startingTimes[startingTimesIndex - 1] + currentTime - startingTime)
      startingTimesIndex -= 1


  def tryEarlier(self, time: Time, duration: TimeDiff, currentTimeI: int) -> bool:
    if currentTimeI == 0: return False

    return (self._startingTimes[currentTimeI - 1] + duration) >= time

  def updateReachables(self, i: int, time: Time) -> None:
    while i < len(self._lineSegments):
      nextStopResult: Tuple[Time, StopName, bool] = self._lineSegments[i].nextStopAndUpdateReachable(time)
      time = nextStopResult[0]
      if not nextStopResult[2]:
        break
      i += 1
