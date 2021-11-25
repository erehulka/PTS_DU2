from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.line import Line
from connectionSearch.lines import Lines
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.lineSegment import LineSegment

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
    self.lines = Lines({
        LineName("Line A"): FakeLine(LineName("Line A"), StopName("First A")),
        LineName("Line B"): FakeLine(LineName("Line B"), StopName("First B")),
    })

  def test_update_reachable(self):
    self.lines.updateReachable([LineName("Line A"), LineName("Fake Line")], StopName("First A"), Time(10))
    self.lines.updateReachable([LineName("Line A"), LineName("Fake Line")], StopName("First Fake"), Time(10))
