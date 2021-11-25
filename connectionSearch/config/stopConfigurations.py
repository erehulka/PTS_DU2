from typing import List
from connectionSearch.connectionSearch import ConnectionSearch
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.line import Line
from connectionSearch.lines import Lines
from connectionSearch.lineSegment import LineSegment
from connectionSearch.stop import Stop
from connectionSearch.stops import Stops

def easyConfig() -> ConnectionSearch:
  stops: List[Stop] = [Stop(StopName("A"), [LineName("1")]), Stop(StopName("B"), [LineName(
      "1")]), Stop(StopName("C"), [LineName("1")]), Stop(StopName("D"), [LineName("1")]), Stop(StopName("E"), [LineName("1")]), Stop(StopName("F"), [LineName("1")])]
  return ConnectionSearch(
    Stops(
      {
        StopName("A"): stops[0],
        StopName("B"): stops[1],
        StopName("C"): stops[2],
        StopName("D"): stops[3],
        StopName("E"): stops[4],
        StopName("F"): stops[5],
      }
    ),
    Lines(
      {
        LineName("1"): Line(
          LineName("1"), 
          [Time(10), Time(20), Time(30)], 
          StopName("A"),
          [
            LineSegment(TimeDiff(2), 10, LineName("1"), stops[1]),
            LineSegment(TimeDiff(3), 10, LineName("1"), stops[2]),
            LineSegment(TimeDiff(4), 10, LineName("1"), stops[3]),
            LineSegment(TimeDiff(5), 10, LineName("1"), stops[4]),
            LineSegment(TimeDiff(6), 10, LineName("1"), stops[5]),
          ]
        )
      }
    )
  )
