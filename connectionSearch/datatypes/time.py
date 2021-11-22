from dataclasses import dataclass

@dataclass
class Time:
  seconds: int

@dataclass
class TimeDiff(Time):
  pass
