from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time
from dataclasses import dataclass

@dataclass
class ConnectionData:
  fr: StopName
  to: StopName
  startTime: Time
  arrivalTime: Time
