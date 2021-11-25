from typing import Dict, List
from connectionSearch.connectionSearch import ConnectionSearch
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.line import Line
from connectionSearch.lines import Lines
from connectionSearch.lineSegment import LineSegment
from connectionSearch.stop import Stop
from connectionSearch.stops import Stops

def easyConfig() -> ConnectionSearch:
  stops: List[Stop] = [Stop(StopName("A"), [LineName("1")]), Stop(StopName("B"), [LineName(
      "1")]), Stop(StopName("C"), [LineName("1")]), Stop(StopName("D"), [LineName("1")]), Stop(StopName("E"), [LineName("1")]), Stop(StopName("F"), [LineName("1")])]
  return ConnectionSearch(
    Stops(
      {
        StopName("A"): stops[0],
        StopName("B"): stops[1],
        StopName("C"): stops[2],
        StopName("D"): stops[3],
        StopName("E"): stops[4],
        StopName("F"): stops[5],
      }
    ),
    Lines(
      {
        LineName("1"): Line(
          LineName("1"), 
          [Time(10), Time(20), Time(30)], 
          StopName("A"),
          [
            LineSegment(TimeDiff(2), 10, LineName("1"), stops[1]),
            LineSegment(TimeDiff(3), 10, LineName("1"), stops[2]),
            LineSegment(TimeDiff(4), 10, LineName("1"), stops[3]),
            LineSegment(TimeDiff(5), 10, LineName("1"), stops[4]),
            LineSegment(TimeDiff(6), 10, LineName("1"), stops[5]),
          ]
        )
      }
    )
  )


def crossConfig() -> ConnectionSearch:
  stops: List[Stop] = [Stop(StopName("A"), [LineName("1")]), Stop(StopName("B"), [LineName(
      "1"), LineName("2")]), Stop(StopName("C"), [LineName("1")]), Stop(StopName("D"), [LineName("2")]), Stop(StopName("E"), [LineName("2")]), Stop(StopName("F"), [LineName("2")])]
  return ConnectionSearch(
      Stops(
          {
              StopName("A"): stops[0],
              StopName("B"): stops[1],
              StopName("C"): stops[2],
              StopName("D"): stops[3],
              StopName("E"): stops[4],
              StopName("F"): stops[5],
          }
      ),
      Lines(
          {
              LineName("1"): Line(
                  LineName("1"),
                  [Time(10), Time(20), Time(30)],
                  StopName("A"),
                  [
                      LineSegment(TimeDiff(2), 10, LineName("1"), stops[1]),
                      LineSegment(TimeDiff(3), 10, LineName("1"), stops[2])
                  ]
              ),
              LineName("2"): Line(
                LineName("2"),
                [Time(13), Time(25), Time(40)],
                StopName("D"),
                [
                  LineSegment(TimeDiff(4), 10, LineName("2"), stops[1]),
                  LineSegment(TimeDiff(10), 10, LineName("2"), stops[4]),
                  LineSegment(TimeDiff(1), 10, LineName("2"), stops[5])
                ]
              )
          }
      )
  )

def pragueMetro() -> ConnectionSearch:
  stops: Dict[str, Stop] = {
    "Hradcanska": Stop(StopName("Hradcanska"), [LineName("A")]),
    "Malostranska": Stop(StopName("Malostranska"), [LineName("A")]),
    "Staromestska": Stop(StopName("Staromestska"), [LineName("A")]),
    "Mustek": Stop(StopName("Mustek"), [LineName("A"), LineName("B")]),
    "Muzeum": Stop(StopName("Muzeum"), [LineName("A"), LineName("C")]),
    "Namesti Miru": Stop(StopName("Namesti Miru"), [LineName("A")]),
    "Jiriho z Podebrad": Stop(StopName("Jiriho z Podebrad"), [LineName("A")]),
    "Flora": Stop(StopName("Flora"), [LineName("A")]),

    "Andel": Stop(StopName("Andel"), [LineName("B")]),
    "Karlovo namesti": Stop(StopName("Karlovo namesti"), [LineName("B")]),
    "Narodni Trida": Stop(StopName("Narodni Trida"), [LineName("B")]),
    "Namesti Republiky": Stop(StopName("Namesti Republiky"), [LineName("B")]),
    "Florenc": Stop(StopName("Florenc"), [LineName("B"), LineName("C")]),
    "Krizikova": Stop(StopName("Krizikova"), [LineName("B")]),
    "Invalidovna": Stop(StopName("Invalidovna"), [LineName("B")]),

    "Vysehrad": Stop(StopName("Vysehrad"), [LineName("C")]),
    "IP Pavlova": Stop(StopName("IP Pavlova"), [LineName("C")]),
    "Hlavni nadrazi": Stop(StopName("Hlavni nadrazi"), [LineName("C")]),
    "Vltavska": Stop(StopName("Vltavska"), [LineName("C")]),
    "Nadrazi Holesovice": Stop(StopName("Nadrazi Holesovice"), [LineName("C")]),
    "Kobylisy": Stop(StopName("Kobylisy"), [LineName("C")]),
    "Ladvi": Stop(StopName("Ladvi"), [LineName("C")]),
  }

  return ConnectionSearch(
    Stops(
      {StopName(key): value for key, value in stops.items()}
    ),
    Lines(
      {
        LineName("A"): Line(
          LineName("A"),
          [Time(i) for i in range(0,200,10)],
          StopName("Hradcanska"),
          [
            LineSegment(
              TimeDiff(3),
              10,
              LineName("A"),
              stops["Malostranska"]
            ),
            LineSegment(
                TimeDiff(4),
                10,
                LineName("A"),
                stops["Staromestska"]
            ),
            LineSegment(
                TimeDiff(2),
                10,
                LineName("A"),
                stops["Mustek"]
            ),
            LineSegment(
                TimeDiff(8),
                10,
                LineName("A"),
                stops["Muzeum"]
            ),
            LineSegment(
                TimeDiff(5),
                10,
                LineName("A"),
                stops["Namesti Miru"]
            ),
            LineSegment(
                TimeDiff(3),
                10,
                LineName("A"),
                stops["Jiriho z Podebrad"]
            ),
            LineSegment(
                TimeDiff(4),
                10,
                LineName("A"),
                stops["Flora"]
            ),
          ]
        ),
        LineName("B"): Line(
            LineName("B"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Andel"),
            [
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    stops["Karlovo namesti"]
                ),
                LineSegment(
                    TimeDiff(10),
                    10,
                    LineName("B"),
                    stops["Narodni Trida"]
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("B"),
                    stops["Mustek"]
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    stops["Namesti Republiky"]
                ),
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    stops["Florenc"]
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    stops["Krizikova"]
                ),
                LineSegment(
                    TimeDiff(9),
                    10,
                    LineName("B"),
                    stops["Invalidovna"]
                ),
            ]
        ),
        LineName("C"): Line(
            LineName("C"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Vysehrad"),
            [
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    stops["IP Pavlova"]
                ),
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    stops["Muzeum"]
                ),
                LineSegment(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    stops["Hlavni nadrazi"]
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    stops["Florenc"]
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("C"),
                    stops["Vltavska"]
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    stops["Nadrazi Holesovice"]
                ),
                LineSegment(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    stops["Kobylisy"]
                ),
                LineSegment(
                    TimeDiff(9),
                    10,
                    LineName("C"),
                    stops["Ladvi"]
                ),
            ]
        )
      }
    )
  )
