from typing import List, Optional, Tuple
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

  def search(self, fr: StopName, to: StopName, time: Time):
    self._stops.setStartingStop(fr, time)
    linesFrom: List[LineName] = self._stops.getLines(fr)
    self._lines.updateReachable(linesFrom, fr, time)

    reachableAfter: Optional[ Tuple[StopName, Time] ] = self._stops.earliestReachableStopAfter(time)
    if reachableAfter is None: 
      print("Error") # TODO handling
      return
    while reachableAfter is not None and reachableAfter[0] != to:
      newTime: Time = reachableAfter[1]
      print(reachableAfter)
      linesFrom = self._stops.getLines(reachableAfter[0])
      self._lines.updateReachable(linesFrom, reachableAfter[0], newTime)
      reachableAfter = self._stops.earliestReachableStopAfter(newTime)
    
    if reachableAfter is not None:
      print(reachableAfter[1])
    
    print("Finished") # TODO Finish
