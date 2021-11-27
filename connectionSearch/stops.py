from typing import Dict, List, Optional, Tuple

from connectionSearch.datatypes.time import Time
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.lineName import LineName

from connectionSearch.stop import StopInterface

class StopsInterface:

  _stops: Dict[StopName, StopInterface]

  def earliestReachableStopAfter(self, time: Time) -> Optional[ Tuple[StopName, Time] ]:
    pass

  def getLines(self, stop: StopName) -> List[LineName]:
    pass

  def getReachableAt(self, stop: StopName) -> Tuple[Optional[Time], Optional[LineName]]:
    pass

  def setStartingStop(self, stop: StopName, time: Time) -> bool:
    pass

  def clean(self) -> None:
    pass

class StopsFactory:

  def create(self, stops: Dict[StopName, StopInterface]) -> StopsInterface:
    return Stops(stops)

  def createDB(self) -> StopsInterface:
    return StopsDB()

class Stops(StopsInterface):

  def __init__(self, stops: Dict[StopName, StopInterface]) -> None:
    self._stops = stops

  def earliestReachableStopAfter(self, time: Time) -> Optional[ Tuple[StopName, Time] ]:
    earliest: Optional[Time] = None
    earliestStop: Optional[StopName] = None

    for stopName in self._stops:
      stop: StopInterface = self._stops[stopName]
      reachableAt: Tuple[Optional[Time], Optional[LineName]] = stop.reachableAt
      if reachableAt[0] is not None:
        if (earliest is None or reachableAt[0] < earliest) and reachableAt[0] > time:
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

  def clean(self) -> None:
    for stop in self._stops.values():
      stop.clean()

class StopsDB(Stops):

  def __init__(self) -> None:
    self._stops = dict()

  def getLines(self, stop: StopName) -> List[LineName]:
    if stop not in self._stops:
      # TODO Vytiahni Stop z DB
      pass
    return self._stops[stop].lines

  def getReachableAt(self, stop: StopName) -> Tuple[Optional[Time], Optional[LineName]]:
    if stop not in self._stops:
      # TODO Vytiahni Stop z DB
      pass
    return self._stops[stop].reachableAt

  def setStartingStop(self, stop: StopName, time: Time) -> bool:
    if stop not in self._stops:
      # TODO Vytiahni Stop z DB
      pass
    self._stops[stop].updateReachableAt(time, None)
    return True

  def clean(self) -> None:
    self._stops = dict()
    # TODO Persist changes to DB
