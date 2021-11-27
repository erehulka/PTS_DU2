from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.line import Line
from connectionSearch.stop import StopFactory
from connectionSearch.stops import StopsFactory, StopsInterface
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.lineSegment import LineSegment


class TestLine(TestCase):

  def setUp(self):
    stopsFactory = StopsFactory()
    stopFactory = StopFactory()
    stops: StopsInterface = stopsFactory.create(
        {
            StopName("A"): stopFactory.create(StopName("A"), [LineName("1")]),
            StopName("B"): stopFactory.create(StopName("B"), [LineName(
                "1"), LineName("1")]),
            StopName("C"): stopFactory.create(StopName("C"), [LineName("1")]),
            StopName("D"): stopFactory.create(StopName("D"), [LineName("1")]),
            StopName("E"): stopFactory.create(StopName("E"), [LineName("1")]),
            StopName("F"): stopFactory.create(StopName("F"), [LineName("1")]),
        }
    )
    self.line = Line(
        LineName("1"),
        [Time(10), Time(20), Time(30)],
        StopName("A"),
        [
            LineSegment(TimeDiff(2), 10, LineName(
                "1"), StopName("B"), stops),
            LineSegment(TimeDiff(3), 10, LineName("1"), StopName("C"), stops),
            LineSegment(TimeDiff(4), 10, LineName("1"), StopName("D"), stops),
            LineSegment(TimeDiff(5), 10, LineName("1"), StopName("E"), stops),
            LineSegment(TimeDiff(6), 10, LineName("1"), StopName("F"), stops),
        ]
    )

  def test_update_reachables(self):
    self.line.updateReachable(Time(10), StopName("A"))
    self.assertEqual(self.line._firstStop, StopName("A"))
