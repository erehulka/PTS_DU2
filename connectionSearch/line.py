from typing import List
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time
from connectionSearch.lineSegment import LineSegment

class LineInterface:

  _name: LineName
  _startingTimes: List[Time] # sorted
  _firstStop: StopName
  _lineSegments: List[LineSegment] # ordered
