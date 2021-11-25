from typing import List, Optional, Tuple
from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.stops import Stops
from connectionSearch.datatypes.time import Time

class FakeStop:

  _name: StopName

  def __init__(self, name: StopName) -> None:
    self._name = name

  def updateReachableAt(self, time: Time, line: Optional[LineName]) -> None:
    pass

  @property
  def reachableAt(self) -> Tuple[Optional[Time], Optional[LineName]]:
    return (None, None)

  @property
  def lines(self) -> List[LineName]:
    return [LineName("Test " + self.name)]

  @property
  def name(self) -> StopName:
    return self._name

class TestStops(TestCase):

  def assert_exception(self, callable, *args, **kwargs):
    try:
      callable(args, kwargs)
      self.assertEqual(True, False)
    except:
      self.assertEqual(True, True)

  def setUp(self):
    self.stops = Stops(
      {
        StopName("A"): FakeStop(StopName("A")),
        StopName("B"): FakeStop(StopName("B")),
        StopName("C"): FakeStop(StopName("C"))
      }
    )

  def test_starting_stop(self):
    self.assertEqual(self.stops.setStartingStop(StopName("X"), Time(0)), False)
    self.assertEqual(self.stops.setStartingStop(StopName("A"), Time(2)), True)

  def test_get_reachable_at(self):
    self.assertEqual(self.stops.getReachableAt(StopName("A")), (None, None))
    self.assert_exception(self.stops.getReachableAt, StopName("X"))

  def test_get_lines(self):
    self.assertEqual(self.stops.getLines(StopName("A")), [LineName("Test A")])
    self.assert_exception(self.stops.getLines, StopName("X"))

  def test_earliest_reachable_stop_after(self):
    pass #TODO