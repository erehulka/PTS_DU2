from typing import Dict, List
from connectionSearch.connectionSearch import ConnectionSearch
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.line import Line
from connectionSearch.lines import Lines
from connectionSearch.lineSegment import LineSegment
from connectionSearch.stop import StopFactory
from connectionSearch.stops import StopsFactory, StopsInterface

def easyConfig() -> ConnectionSearch:
  #stops: List[Stop] = [Stop(StopName("A"), [LineName("1")]), Stop(StopName("B"), [LineName(
  #    "1")]), Stop(StopName("C"), [LineName("1")]), Stop(StopName("D"), [LineName("1")]), Stop(StopName("E"), [LineName("1")]), Stop(StopName("F"), [LineName("1")])]
  stopsFactory = StopsFactory()
  stopFactory = StopFactory()
  stops: StopsInterface = stopsFactory.create(
      {
        StopName("A"): stopFactory.create(StopName("A"), [LineName("1")]),
        StopName("B"): stopFactory.create(StopName("B"), [LineName("1")]),
        StopName("C"): stopFactory.create(StopName("C"), [LineName("1")]),
        StopName("D"): stopFactory.create(StopName("D"), [LineName("1")]),
        StopName("E"): stopFactory.create(StopName("E"), [LineName("1")]),
        StopName("F"): stopFactory.create(StopName("F"), [LineName("1")]),
      }
  )

  return ConnectionSearch(
    stops,
    Lines(
      {
        LineName("1"): Line(
          LineName("1"), 
          [Time(10), Time(20), Time(30)], 
          StopName("A"),
          [
            LineSegment(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
            LineSegment(TimeDiff(3), 10, LineName("1"), StopName("C"), stops),
            LineSegment(TimeDiff(4), 10, LineName("1"), StopName("D"), stops),
            LineSegment(TimeDiff(5), 10, LineName("1"), StopName("E"), stops),
            LineSegment(TimeDiff(6), 10, LineName("1"), StopName("F"), stops),
          ]
        )
      }
    )
  )


def crossConfig() -> ConnectionSearch:
  stopsFactory = StopsFactory()
  stopFactory = StopFactory()
  stops: StopsInterface = stopsFactory.create(
      {
        StopName("A"): stopFactory.create(StopName("A"), [LineName("1")]),
        StopName("B"): stopFactory.create(StopName("B"), [LineName(
            "1"), LineName("2")]),
        StopName("C"): stopFactory.create(StopName("C"), [LineName("1")]),
        StopName("D"): stopFactory.create(StopName("D"), [LineName("2")]),
        StopName("E"): stopFactory.create(StopName("E"), [LineName("2")]),
        StopName("F"): stopFactory.create(StopName("F"), [LineName("2")]),
      }
  )
  
  return ConnectionSearch(
      stops,
      Lines(
          {
              LineName("1"): Line(
                  LineName("1"),
                  [Time(10), Time(20), Time(30)],
                  StopName("A"),
                  [
                      LineSegment(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
                      LineSegment(TimeDiff(3), 10, LineName("1"), StopName("C"), stops)
                  ]
              ),
              LineName("2"): Line(
                LineName("2"),
                [Time(13), Time(25), Time(40)],
                StopName("D"),
                [
                    LineSegment(TimeDiff(4), 10, LineName("2"), StopName("B"), stops),
                    LineSegment(TimeDiff(10), 10, LineName("2"), StopName("E"), stops),
                    LineSegment(TimeDiff(1), 10, LineName("2"), StopName("F"), stops)
                ]
              )
          }
      )
  )

def pragueMetro() -> ConnectionSearch:

  stopsFactory = StopsFactory()
  stopFactory = StopFactory()
  stops: StopsInterface = stopsFactory.create(
      {
        StopName("Hradcanska"): stopFactory.create(StopName("Hradcanska"), [LineName("A")]),
        StopName("Malostranska"): stopFactory.create(StopName("Malostranska"), [LineName("A")]),
        StopName("Staromestska"): stopFactory.create(StopName("Staromestska"), [LineName("A")]),
        StopName("Mustek"): stopFactory.create(StopName("Mustek"), [LineName("A"), LineName("B")]),
        StopName("Muzeum"): stopFactory.create(StopName("Muzeum"), [LineName("A"), LineName("C")]),
        StopName("Namesti Miru"): stopFactory.create(StopName("Namesti Miru"), [LineName("A")]),
        StopName("Jiriho z Podebrad"): stopFactory.create(StopName("Jiriho z Podebrad"), [LineName("A")]),
        StopName("Flora"): stopFactory.create(StopName("Flora"), [LineName("A")]),

        StopName("Andel"): stopFactory.create(StopName("Andel"), [LineName("B")]),
        StopName("Karlovo namesti"): stopFactory.create(StopName("Karlovo namesti"), [LineName("B")]),
        StopName("Narodni Trida"): stopFactory.create(StopName("Narodni Trida"), [LineName("B")]),
        StopName("Namesti Republiky"): stopFactory.create(StopName("Namesti Republiky"), [LineName("B")]),
        StopName("Florenc"): stopFactory.create(StopName("Florenc"), [LineName("B"), LineName("C")]),
        StopName("Krizikova"): stopFactory.create(StopName("Krizikova"), [LineName("B")]),
        StopName("Invalidovna"): stopFactory.create(StopName("Invalidovna"), [LineName("B")]),

        StopName("Vysehrad"): stopFactory.create(StopName("Vysehrad"), [LineName("C")]),
        StopName("IP Pavlova"): stopFactory.create(StopName("IP Pavlova"), [LineName("C")]),
        StopName("Hlavni nadrazi"): stopFactory.create(StopName("Hlavni nadrazi"), [LineName("C")]),
        StopName("Vltavska"): stopFactory.create(StopName("Vltavska"), [LineName("C")]),
        StopName("Nadrazi Holesovice"): stopFactory.create(StopName("Nadrazi Holesovice"), [LineName("C")]),
        StopName("Kobylisy"): stopFactory.create(StopName("Kobylisy"), [LineName("C")]),
        StopName("Ladvi"): stopFactory.create(StopName("Ladvi"), [LineName("C")]),
      }
  )

  return ConnectionSearch(
    stops,
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
              StopName("Malostranska"),
              stops
            ),
            LineSegment(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Staromestska"),
                stops
            ),
            LineSegment(
                TimeDiff(2),
                10,
                LineName("A"),
                StopName("Mustek"),
                stops
            ),
            LineSegment(
                TimeDiff(8),
                10,
                LineName("A"),
                StopName("Muzeum"),
                stops
            ),
            LineSegment(
                TimeDiff(5),
                10,
                LineName("A"),
                StopName("Namesti Miru"),
                stops
            ),
            LineSegment(
                TimeDiff(3),
                10,
                LineName("A"),
                StopName("Jiriho z Podebrad"),
                stops
            ),
            LineSegment(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Flora"),
                stops
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
                    StopName("Karlovo namesti"),
                    stops
                ),
                LineSegment(
                    TimeDiff(10),
                    10,
                    LineName("B"),
                    StopName("Narodni Trida"),
                stops
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("B"),
                    StopName("Mustek"),
                    stops
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Namesti Republiky"),
                    stops
                ),
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    StopName("Florenc"),
                    stops
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Krizikova"),
                    stops
                ),
                LineSegment(
                    TimeDiff(9),
                    10,
                    LineName("B"),
                    StopName("Invalidovna"),
                    stops
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
                    StopName("IP Pavlova"),
                    stops
                ),
                LineSegment(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    StopName("Muzeum"),
                    stops
                ),
                LineSegment(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Hlavni nadrazi"),
                    stops
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Florenc"),
                    stops
                ),
                LineSegment(
                    TimeDiff(3),
                    10,
                    LineName("C"),
                    StopName("Vltavska"),
                    stops
                ),
                LineSegment(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Nadrazi Holesovice"),
                    stops
                ),
                LineSegment(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Kobylisy"),
                    stops
                ),
                LineSegment(
                    TimeDiff(9),
                    10,
                    LineName("C"),
                    StopName("Ladvi"),
                    stops
                ),
            ]
        )
      }
    )
  )
