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

  def nextStop(self, startTime: Time) -> Tuple[Time, StopName]:
    return (startTime + self._timeToNextStop, self._nextStop.name)
