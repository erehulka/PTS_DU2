from dataclasses import dataclass

@dataclass
class StopName:
  name: str
  
  def __str__(self):
    return self.name

  def __add__(self, other):
    return str(self) + other
    
  def __radd__(self, other):
    return other + str(self)
