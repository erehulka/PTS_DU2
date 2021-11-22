from dataclasses import dataclass

@dataclass
class StopName:
  name: str
  
  def __str__(self):
    return self.name
