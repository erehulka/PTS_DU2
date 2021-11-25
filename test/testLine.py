from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.line import Line
from connectionSearch.stop import Stop
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.lineSegment import LineSegment


class TestLine(TestCase):

  def setUp(self):
    self.line = Line(LineName("Line A"), [Time(10), Time(20)], StopName("First"), [
      LineSegment(
        TimeDiff(2),
        10,
        LineName("Line A"),
        Stop(StopName("Second"), [LineName("Line A")])
      ),
      LineSegment(
          TimeDiff(3),
          10,
          LineName("Line A"),
          Stop(StopName("Third"), [LineName("Line A")])
      ),
    ])

  def test_update_reachables(self):
    self.line.updateReachable(Time(10), StopName("First"))
    self.assertEqual(self.line._firstStop, StopName("First"))