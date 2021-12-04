from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import TimeDiff, Time
from connectionSearch.lineSegment import LineSegmentFactory
from connectionSearch.stop import StopInterface, StopFactory

class FakeStops:

  # LineSegment uses only one method

  _stop: StopInterface

  def __init__(self):
    self._stop = StopFactory.create(StopName("Fake Stop"), [LineName("Fake Line")])

  def getByName(self, name: StopName) -> StopInterface:
    return self._stop


class TestLineSegment(TestCase):

  def setUp(self):
    self.segment = LineSegmentFactory.create(
      TimeDiff(10),
      2,
      LineName("Test Line"),
      StopName("Test Stop"),
      FakeStops()
    )

  def test_next_stop(self):
    self.assertTupleEqual(self.segment.nextStop(Time(10)), (Time(20), StopName("Test Stop"))) # straightforward...
  
  def test_increment_capacity(self):  # see how incrementCapacity works, it takes time as (time - timeToNext), so that is why
                                      # there is passenger at time 0 when we incremented at time 10
    self.segment.incrementCapacity(Time(10))
    self.assertEqual(self.segment._numberOfPassengers, {Time(0): 1})
    self.segment.incrementCapacity(Time(15))
    self.assertEqual(self.segment._numberOfPassengers, {Time(0): 1, Time(5): 1})
    self.segment.incrementCapacity(Time(15))
    self.assertEqual(self.segment._numberOfPassengers, {Time(0): 1, Time(5): 2})

  def test_next_stop_update_reachable(self):
    self.segment._numberOfPassengers = {} # clean
    self.assertTupleEqual(
      self.segment.nextStopAndUpdateReachable(Time(10)), 
      (Time(20), StopName("Test Stop"), True)
    )
    self.segment.incrementCapacity(Time(20))
    self.segment.incrementCapacity(Time(20))
    self.assertTupleEqual(
      self.segment.nextStopAndUpdateReachable(Time(10)), 
      (Time(20), StopName("Test Stop"), False)
    )
