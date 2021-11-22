from dataclasses import dataclass

@dataclass
class Time:
  seconds: int

  def __add__(self, other):
    return Time(self.seconds + other.seconds)

@dataclass
class TimeDiff(Time):
  pass
