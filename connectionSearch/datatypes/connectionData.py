from typing import List
from dataclasses import dataclass

from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

@dataclass
class ConnectionData:
  fr: StopName
  to: StopName
  startTime: Time
  arrivalTime: Time
  stops: List[StopName]
