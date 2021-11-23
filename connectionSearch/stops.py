from typing import Dict, List, Optional, Tuple
from connectionSearch.stop import Stop
from connectionSearch.datatypes.time import Time
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.lineName import LineName

class Stops:

  _stops: Dict[StopName, Stop]

  def earliestReachableStopAfter(self, time: Time) -> Optional[ Tuple[StopName, Time] ]:
    earliest: Optional[Time] = None
    earliestStop: Optional[StopName] = None

    for stopName in self._stops:
      stop: Stop = self._stops[stopName]
      reachableAt: Tuple[Optional[Time], Optional[LineName]] = stop.reachableAt
      if reachableAt[0] is not None:
        if earliest is None or reachableAt[0] < earliest:
          earliest = reachableAt[0]
          earliestStop = stop.name

    if earliest is None or earliestStop is None: return None
    
    return (earliestStop, earliest)

  def getLines(self, stop: StopName) -> List[LineName]:
    if stop not in self._stops:
      raise Exception("This stop name is not in dictionary of stops (name of stop: " + stop + ")")
    return self._stops[stop].lines

  def getReachableAt(self, stop: StopName) -> Tuple[Optional[Time], Optional[LineName]]:
    if stop not in self._stops:
      raise Exception("This stop name is not in dictionary of stops (name of stop: " + stop + ")")
    return self._stops[stop].reachableAt

  def setStartingStop(self, stop: StopName, time: Time) -> bool:
    if stop not in self._stops: return False
    self._stops[stop].updateReachableAt(time, None)
    return True