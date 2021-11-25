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

  def __hash__(self):
    return hash(self.name)

  def __eq__(self, other):
    return self.name == other.name
