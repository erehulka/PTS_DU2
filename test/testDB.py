from unittest import TestCase
from connectionSearch.connectionSearch import ConnectionSearchFactory
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time
from connectionSearch.stops import StopsFactory
from connectionSearch.lines import LinesFactory

class TestDB(TestCase): # test if database is working correctly

  def setUp(self) -> None:
    dataset = 'Basic'
    stops = StopsFactory().createDB(dataset)
    self.search = ConnectionSearchFactory().create(stops, LinesFactory().createDB(dataset, stops))

  """ 
  # WARNING - uncomment only after running 'make recreate_whole_db' and after testing run again
  def test_capacity(self):
    # Before running this test, be sure to recreate whole database

    result = self.search.search(StopName("A"), StopName("D"), Time(5))
    self.assertNotEqual(result, None)
    self.assertEqual(result.fr, StopName("A"))
    self.assertEqual(result.arrivalTime, Time(19))
    # fast checks if everyrhing works correctly
    # now saving to db

    for i in range(10):
      result = self.search.search(StopName("A"), StopName("C"), Time(10))
      # First possible should be fully booked
    self.assertEqual(result.arrivalTime, Time(25)) # So we will get second options

    # And now recreate search instance, to see that we will still have changes from db
    dataset = 'Basic'
    stops = StopsFactory().createDB(dataset)
    self.search = ConnectionSearchFactory().create(stops, LinesFactory().createDB(dataset, stops))

    result = self.search.search(StopName("A"), StopName("C"), Time(10))
    self.assertEqual(result.arrivalTime, Time(25)) # Still second option

    # Now let's book everything we've got...
    for i in range(100):
      result = self.search.search(StopName("A"), StopName("C"), Time(10))
    
    # Nothing left...
    self.assertEqual(result, None)

    # Try again
    dataset = 'Basic'
    stops = StopsFactory().createDB(dataset)
    self.search = ConnectionSearchFactory().create(stops, LinesFactory().createDB(dataset, stops))

    result = self.search.search(StopName("A"), StopName("C"), Time(10))
    self.assertEqual(result, None)
    # So sad

    # Congrats! Now the db is totally ruined. To fix it, simply reset data with 'make recreate_whole_db'
  """


