from typing import Dict, List, Optional, Tuple

from connectionSearch.datatypes.time import Time
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.lineName import LineName

from connectionSearch.stop import StopFactory, StopInterface

from database.queries import select_stop_by_name_dataset
from database.setup import StopDB

class StopsInterface:

  _stops: Dict[StopName, StopInterface]

  def earliestReachableStopAfter(self, time: Time) -> Optional[ Tuple[StopName, Time] ]:
    raise NotImplementedError

  def getLines(self, stop: StopName) -> List[LineName]:
    raise NotImplementedError

  def getReachableAt(self, stop: StopName) -> Tuple[Optional[Time], Optional[LineName]]:
    raise NotImplementedError

  def setStartingStop(self, stop: StopName, time: Time) -> bool:
    raise NotImplementedError

  def clean(self) -> None:
    raise NotImplementedError

  def getByName(self, name: StopName) -> StopInterface:
    raise NotImplementedError

class StopsFactory:

  @staticmethod
  def create(stops: Dict[StopName, StopInterface]) -> StopsInterface:
    return Stops(stops)

  @staticmethod
  def createDB(dataset: str) -> StopsInterface:
    return StopsDB(dataset)

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

    if earliest is None or earliestStop is None: 
      return None
    
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
    if stop not in self._stops: 
      return False
    self._stops[stop].updateReachableAt(time, None)
    return True

  def clean(self) -> None:
    for stop in self._stops.values():
      stop.clean()

  def getByName(self, name: StopName) -> StopInterface:
    if name not in self._stops:
      raise Exception("This stop name is not in dictionary of stops (name of stop: " + name + ")")
    return self._stops[name]

class StopsDB(Stops):

  _dataset: str

  def __init__(self, dataset: str) -> None:
    super().__init__({})
    self._dataset = dataset

  def get_from_db(self, name: str) -> None:
    stop: Optional[StopDB] = select_stop_by_name_dataset(name, self._dataset)
    if stop is None:
      raise ValueError(f"Stop {name} is not in database.")
    self._stops[StopName(name)] = StopFactory.createFromDB(stop)

  def getLines(self, stop: StopName) -> List[LineName]:
    if stop not in self._stops:
      self.get_from_db(stop.name)
    return self._stops[stop].lines

  def getReachableAt(self, stop: StopName) -> Tuple[Optional[Time], Optional[LineName]]:
    if stop not in self._stops:
      self.get_from_db(stop.name)
    return self._stops[stop].reachableAt

  def setStartingStop(self, stop: StopName, time: Time) -> bool:
    if stop not in self._stops:
      self.get_from_db(stop.name)
    self._stops[stop].updateReachableAt(time, None)
    return True

  def clean(self) -> None:
    self._stops = {}

  def getByName(self, name: StopName) -> StopInterface:
    if name not in self._stops:
      self.get_from_db(name.name)
    return self._stops[name]
