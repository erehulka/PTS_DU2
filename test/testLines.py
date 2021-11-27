from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.lines import LinesFactory
from connectionSearch.line import LineFactory
from connectionSearch.datatypes.time import Time, TimeDiff

class FakeLine:

  _name: LineName
  _firstStop: StopName

  def __init__(self, name: LineName, firstStop: StopName) -> None:
    self._name = name
    self._firstStop = firstStop

  def updateReachable(self, time: Time, stop: StopName) -> None:
    pass

  def tryEarlier(self, time: Time, duration: TimeDiff, currentTimeI: int) -> bool:
    return False

  def updateReachables(self, i: int, time: Time) -> None:
    pass

class TestLines(TestCase):

  def setUp(self):
    factory = LinesFactory()
    self.lines = factory.create({
        LineName("Line A"): FakeLine(LineName("Line A"), StopName("First A")),
        LineName("Line B"): FakeLine(LineName("Line B"), StopName("First B")),
    })

  def test_update_reachable(self):
    # Test if there is no exception
    self.lines.updateReachable([LineName("Line A"), LineName("Fake Line")], StopName("First A"), Time(10))
    self.lines.updateReachable([LineName("Line A"), LineName("Fake Line")], StopName("First Fake"), Time(10))

  def test_update_capacity_and_get_previous_stop(self):
    pass
