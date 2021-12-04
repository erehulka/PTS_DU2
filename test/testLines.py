from typing import Optional
from unittest import TestCase

from sqlalchemy.orm.session import Session
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.lines import LinesFactory
from connectionSearch.datatypes.time import Time

class FakeLine:

  _name: LineName
  _firstStop: StopName

  def __init__(self, name: LineName, firstStop: StopName) -> None:
    self._name = name
    self._firstStop = firstStop

  def updateReachable(self, time: Time, stop: StopName) -> None:
    pass

  @staticmethod
  def tryEarlier() -> bool:
    return False

  def updateReachables(self, i: int, time: Time) -> None:
    pass

  def updateCapacityAndGetPreviousStop(self, stop: StopName, time: Time, session: Optional[Session] = None) -> StopName:
    pass

class TestLines(TestCase):

  def setUp(self):
    self.lines = LinesFactory.create({
        LineName("Line A"): FakeLine(LineName("Line A"), StopName("First A")),
        LineName("Line B"): FakeLine(LineName("Line B"), StopName("First B")),
    })

  def test_update_reachable(self):
    # Test if there is no exception
    self.lines.updateReachable([LineName("Line A"), LineName("Line A")], StopName("First A"), Time(10))
    with self.assertRaises(Exception):
      self.lines.updateReachable([LineName("Line A"), LineName("Line X Fake")], StopName("First Fake"), Time(10))

  def test_update_capacity_and_get_previous_stop(self):
    # We are testing update capacity in testLine.py, so only checking exceptions
    with self.assertRaises(Exception):
      self.lines.updateCapacityAndGetPreviousStop(LineName("Line C"), StopName("First X"), Time(10))

  # MOST of Lines class works with Line class, which we tested in testLine.py
