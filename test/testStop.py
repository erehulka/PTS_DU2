from unittest import TestCase
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.stop import StopFactory
from connectionSearch.datatypes.time import Time


class TestStop(TestCase):

  def setUp(self):
    self.stop = StopFactory.create(StopName("Test stop"), [LineName("1"), LineName("2")])

  def test_reachable(self):
    self.assertEqual(self.stop.reachableAt, (None, None))
    self.stop.updateReachableAt(Time(10), LineName("2"))
    self.assertEqual(self.stop.reachableAt, (Time(10), LineName("2")))
    self.stop.updateReachableAt(Time(20), LineName("1"))
    self.assertEqual(self.stop.reachableAt, (Time(10), LineName("2")))
    self.stop.updateReachableAt(Time(5), LineName("1"))
    self.assertEqual(self.stop.reachableAt, (Time(5), LineName("1")))
    self.stop.updateReachableAt(Time(4), None)
    self.assertEqual(self.stop.reachableAt, (Time(4), None))

  def test_lines_and_name(self):
    self.assertEqual(self.stop.name, StopName("Test stop"))
    self.assertEqual(self.stop.lines, [LineName("1"), LineName("2")])

  def test_clean(self):
    self.stop.updateReachableAt(Time(5), LineName("1"))
    self.assertNotEqual(self.stop.reachableAt, (None, None))
    self.stop.clean()
    self.assertEqual(self.stop.reachableAt, (None, None))
