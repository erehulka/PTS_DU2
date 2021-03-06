from dataclasses import dataclass

@dataclass
class Time:
  seconds: int

  def __add__(self, other):
    return Time(self.seconds + other.seconds)

  def __sub__(self, other):
    return Time(self.seconds - other.seconds)

  def __lt__(self, other):
    return self.seconds < other.seconds

  def __gt__(self, other):
    return self.seconds > other.seconds

  def __ge__(self, other):
    return self.seconds >= other.seconds

  def __hash__(self):
    return self.seconds

  def __eq__(self, other):
    if other is None: 
      return False
    return self.seconds == other.seconds

@dataclass
class TimeDiff(Time):
  pass
