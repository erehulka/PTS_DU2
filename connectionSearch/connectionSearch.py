from typing import List, Tuple
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.stop import Stop
from connectionSearch.stops import Stops
from connectionSearch.lines import Lines
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

class ConnectionSearch:

  _stops: Stops
  _lines: Lines

  def search(self, fr: StopName, to: StopName, time: Time):
    self._stops.setStartingStop(fr, time)
    linesFrom: List[LineName] = self._stops.getLines(fr)
    self._lines.updateReachable(linesFrom, fr, time)

    reachableAfter: Tuple[StopName, Time] = self._stops.earliestReachableStopAfter(time)
    newTime: Time = reachableAfter[1]
    while reachableAfter[0] != to and reachableAfter is not None:
      linesFrom = self._stops.getLines(reachableAfter[0])
      self._lines.updateReachable(linesFrom, fr, newTime)
      reachableAfter = self._stops.earliestReachableStopAfter(newTime)

    print(reachableAfter[1]) # TODO Finish