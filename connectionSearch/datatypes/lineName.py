from dataclasses import dataclass

@dataclass
class LineName:
  name: str

  def __str__(self):
    return self.name
