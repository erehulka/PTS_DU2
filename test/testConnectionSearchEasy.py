from unittest import TestCase
from connectionSearch.config.stopConfigurations import easyConfig
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time

class TestConnectionSearchEasy(TestCase):

  def test_factory(self):
    self.search = easyConfig()
    self.search.search(StopName("A"), StopName("C"), Time(12))
