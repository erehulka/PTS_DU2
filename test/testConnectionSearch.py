from unittest import TestCase
from connectionSearch.datatypes.connectionData import ConnectionData
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time
from connectionSearch.config.stopConfigurations import easyConfig, crossConfig, pragueMetro

class TestConnectionSearcg(TestCase):

  def setUp(self):
    self.searchEasy = easyConfig()
    self.searchCross = crossConfig()
    self.searchPrague = pragueMetro()

  def test_easy(self): # tests easy configuration
    # only method is search, so we can test if search will return wanted result
    result: ConnectionData = self.searchEasy.search(StopName("A"), StopName("C"), Time(10))
    self.assertEqual(result.to, StopName("C"))
    self.assertEqual(result.arrivalTime, Time(15))
    self.assertEqual(result.fr, StopName("A"))
    self.assertEqual(len(result.stops), 3)

    # And let's try other stops
    result = self.searchEasy.search(StopName("C"), StopName("E"), Time(20))
    self.assertEqual(result.arrivalTime, Time(34))
    self.assertEqual(len(result.stops), 3)
    self.assertEqual(self.searchEasy._stops._stops[StopName("B")]._reachableAt, None) # B should be None, because of clean

    # So we have checked basically everything. Now if it takes capacity into account
    for i in range(10):
      result: ConnectionData = self.searchEasy.search(StopName("A"), StopName("C"), Time(10))
      # First possible should be fully booked
    self.assertEqual(result.arrivalTime, Time(25)) # So we will get second options

  def test_cross(self): # Tests if line changes are correct
    result: ConnectionData = self.searchCross.search(StopName("A"), StopName("F"), Time(0)) # No direct, but with change at B
    self.assertNotEqual(result, None)
    self.assertEqual(result.arrivalTime, Time(28))
    self.assertEqual(result.to, StopName("F"))
    # etc etc, same tests as in test_easy()

  def test_prague(self):
    result: ConnectionData = self.searchPrague.search(StopName("Malostranska"), StopName("Namesti Republiky"), Time(10)) # One change at Mustek
    self.assertTrue(StopName("Mustek") in result.stops)
    # Unfortunately the lines go only one way...

    self.assertEqual(result.arrivalTime, Time(30))