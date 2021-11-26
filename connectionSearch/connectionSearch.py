from typing import List, Optional, Tuple
from connectionSearch.datatypes.connectionData import ConnectionData
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.stop import Stop
from connectionSearch.stops import Stops
from connectionSearch.lines import Lines
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

class ConnectionSearch:

  _stops: Stops
  _lines: Lines

  def __init__(self, stops: Stops, lines: Lines) -> None:
    self._stops = stops
    self._lines = lines

  def search(self, fr: StopName, to: StopName, time: Time) -> Optional[ConnectionData]:
    self._stops.setStartingStop(fr, time)
    linesFrom: List[LineName] = self._stops.getLines(fr)
    self._lines.updateReachable(linesFrom, fr, time)

    reachableAfter: Optional[ Tuple[StopName, Time] ] = self._stops.earliestReachableStopAfter(time)
    if reachableAfter is None:
      # TODO Logging
      return None
    while reachableAfter is not None and reachableAfter[0] != to:
      newTime: Time = reachableAfter[1]
      linesFrom = self._stops.getLines(reachableAfter[0])
      self._lines.updateReachable(linesFrom, reachableAfter[0], newTime)
      reachableAfter = self._stops.earliestReachableStopAfter(newTime)
    
    if reachableAfter is not None:
      result: ConnectionData = ConnectionData(fr, to, time, reachableAfter[1], list())
    else: 
      return None

    currentStop: StopName = to
    currentTime: Optional[Time]
    line: Optional[LineName]
    result.stops.append(currentStop)
    while currentStop != fr:
      currentTime, line = self._stops.getReachableAt(currentStop)
      if currentTime is None or line is None: break
      currentStop = self._lines.updateCapacityAndGetPreviousStop(line, currentStop, currentTime)
      result.stops.append(currentStop)

    self._stops.clean()
    result.stops.reverse()
    return result

    
