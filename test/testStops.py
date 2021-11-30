from typing import List, Optional, Tuple
from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.stops import StopsFactory
from connectionSearch.datatypes.time import Time

class MockStop: # Mock of stop class, so we know if it is cleaned by clean()

  _name: StopName
  _isCleaned: bool
  _reachableAt: Optional[Time]
  _reachableVia: Optional[LineName]

  def __init__(self, name: StopName) -> None:
    self._name = name
    self._isCleaned = False
    self._reachableAt = None
    self._reachableVia = None

  def updateReachableAt(self, time: Time, line: Optional[LineName]) -> None:
    self._reachableAt = time
    self._reachableVia = line

  def clean(self) -> None:
    self._isCleaned = True

  @property
  def reachableAt(self) -> Tuple[Optional[Time], Optional[LineName]]:
    return (self._reachableAt, self._reachableVia)

  @property
  def lines(self) -> List[LineName]:
    return [LineName("Test " + self.name)]

  @property
  def name(self) -> StopName:
    return self._name

  @property
  def cleaned(self) -> bool:
    return self._isCleaned

class TestStops(TestCase):

  def assert_exception(self, callable, *args, **kwargs): # Method to assert there will be exception
    try:
      callable(*args, **kwargs)
    except:
      self.assertEqual(True, True)
      return
    self.assertEqual(True, False)

  def setUp(self):
    factory = StopsFactory()
    self.stops = factory.create(
      {
        StopName("A"): MockStop(StopName("A")),
        StopName("B"): MockStop(StopName("B")),
        StopName("C"): MockStop(StopName("C"))
      }
    )

  def test_starting_stop(self): # Test if it possible to set starting stop with real and fake
    self.assertEqual(self.stops.setStartingStop(StopName("X"), Time(0)), False)
    self.assertEqual(self.stops.setStartingStop(StopName("A"), Time(2)), True)

  def test_get_reachable_at(self):
    self.assertEqual(self.stops.getReachableAt(StopName("A")), (None, None))
    self.assert_exception(self.stops.getReachableAt, StopName("X"))

  def test_get_lines(self):
    self.assertEqual(self.stops.getLines(StopName("A")), [LineName("Test A")])
    self.assert_exception(self.stops.getLines, StopName("X"))

  # until now straightforward testing

  def test_earliest_reachable_stop_after(self): # Testing earliest reachable stop by changing reachableAt of MockStops
    self.assertEqual(self.stops.earliestReachableStopAfter(Time(0)), None)
    self.assertEqual(self.stops.earliestReachableStopAfter(Time(10)), None)

    self.stops._stops[StopName("A")].updateReachableAt(Time(5), None)

    self.assertEqual(self.stops.earliestReachableStopAfter(Time(10)), None)
    self.assertEqual(self.stops.earliestReachableStopAfter(Time(5)), None)
    self.assertEqual(self.stops.earliestReachableStopAfter(Time(0)), (StopName("A"), Time(5)))

    self.stops._stops[StopName("B")].updateReachableAt(Time(10), LineName("Line"))

    self.assertEqual(self.stops.earliestReachableStopAfter(Time(10)), None)
    self.assertEqual(self.stops.earliestReachableStopAfter(Time(9)), (StopName("B"), Time(10)))

  def testClean(self): # Only test if clean() method of MockStop was accessed (works as Stop)
    for stop in self.stops._stops.values():
      self.assertEqual(stop.cleaned, False)
    self.stops.clean()
    for stop in self.stops._stops.values():
      self.assertEqual(stop.cleaned, True)
