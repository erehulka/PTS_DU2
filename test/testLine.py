from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.line import LineFactory
from connectionSearch.stop import StopFactory
from connectionSearch.stops import StopsFactory, StopsInterface
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.lineSegment import LineSegmentFactory


class TestLines(TestCase):

  def assert_exception(self, callable, *args, **kwargs):
    try:
      callable(*args, **kwargs)
    except:
      self.assertEqual(True, True)
      return
    self.assertEqual(True, False)


  def setUp(self):
    stops: StopsInterface = StopsFactory.create(
        {
            StopName("A"): StopFactory.create(StopName("A"), [LineName("1")]),
            StopName("B"): StopFactory.create(StopName("B"), [LineName(
                "1"), LineName("1")]),
            StopName("C"): StopFactory.create(StopName("C"), [LineName("1")]),
            StopName("D"): StopFactory.create(StopName("D"), [LineName("1")]),
            StopName("E"): StopFactory.create(StopName("E"), [LineName("1")]),
            StopName("F"): StopFactory.create(StopName("F"), [LineName("1")]),
        }
    )
    
    self.line = LineFactory.create(
        LineName("1"),
        [Time(10), Time(20), Time(30), Time(40)],
        StopName("A"),
        [
            LineSegmentFactory.create(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
            LineSegmentFactory.create(TimeDiff(3), 10, LineName("1"), StopName("C"), stops),
            LineSegmentFactory.create(TimeDiff(4), 10, LineName("1"), StopName("D"), stops),
            LineSegmentFactory.create(TimeDiff(5), 10, LineName("1"), StopName("E"), stops),
            LineSegmentFactory.create(TimeDiff(6), 10, LineName("1"), StopName("F"), stops),
        ]
    )

  def test_update_reachable(self):
    self.assert_exception(self.line.updateReachable, Time(1000), StopName("A")) # No such time
    self.line.updateReachable(Time(15), StopName("A")) # Should take time 20
    self.assertTupleEqual(
      self.line._lineSegments[2]._stops.getByName(self.line._lineSegments[2]._nextStop).reachableAt,
      (Time(29), LineName("1"))
    ) # not good looking I know...
    self.line.updateReachable(Time(10), StopName("B")) # B should stay untouched
    self.assertTupleEqual(
      self.line._lineSegments[0]._stops.getByName(self.line._lineSegments[0]._nextStop).reachableAt,
      (Time(22), LineName("1"))
    )
    # and C, D etc. changed
    self.assertTupleEqual(
      self.line._lineSegments[1]._stops.getByName(self.line._lineSegments[1]._nextStop).reachableAt,
      (Time(15), LineName("1"))
    )

  def test_update_reachables(self):
    # Test if it will change correctly
    self.line._lineSegments[4]._stops.getByName(self.line._lineSegments[4]._nextStop).updateReachableAt(Time(1000), None)
    # Info - we must use reachableAt very big so it will change when we call it with real values
    self.line.updateReachable(Time(15), StopName("A"))  # Should take time 20
    self.assertTupleEqual(
      self.line._lineSegments[4]._stops.getByName(self.line._lineSegments[4]._nextStop).reachableAt,
      (Time(40), LineName("1"))
    )

  # We have also tested the try_earlier method, because the starting times 30 and 40 were not used

  def test_update_capacity(self):
    self.assertEqual(self.line.updateCapacityAndGetPreviousStop(StopName("B"), Time(2)), StopName("A"))
    self.assertEqual(self.line.updateCapacityAndGetPreviousStop(StopName("D"), Time(4)), StopName("C"))
    self.assertEqual(self.line._lineSegments[0]._numberOfPassengers, {Time(0): 1})
    self.assertEqual(self.line._lineSegments[2]._numberOfPassengers, {Time(0): 1})
