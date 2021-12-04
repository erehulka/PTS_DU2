from connectionSearch.connection import ConnectionSearch
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.line import LineFactory
from connectionSearch.lines import LinesFactory
from connectionSearch.lineSegment import LineSegmentFactory
from connectionSearch.stop import StopFactory
from connectionSearch.stops import StopsFactory, StopsInterface

def easyConfig() -> ConnectionSearch:
  stops: StopsInterface = StopsFactory.create(
      {
        StopName("A"): StopFactory.create(StopName("A"), [LineName("1")]),
        StopName("B"): StopFactory.create(StopName("B"), [LineName("1")]),
        StopName("C"): StopFactory.create(StopName("C"), [LineName("1")]),
        StopName("D"): StopFactory.create(StopName("D"), [LineName("1")]),
        StopName("E"): StopFactory.create(StopName("E"), [LineName("1")]),
        StopName("F"): StopFactory.create(StopName("F"), [LineName("1")]),
      }
  )

  return ConnectionSearch(
    stops,
    LinesFactory.create(
      {
        LineName("1"): LineFactory.create(
          LineName("1"), 
          [Time(10), Time(20), Time(30)], 
          StopName("A"),
          [
            LineSegmentFactory.create(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
            LineSegmentFactory.create(TimeDiff(3), 10, LineName("1"), StopName("C"), stops),
            LineSegmentFactory.create(TimeDiff(4), 10, LineName("1"), StopName("D"), stops),
            LineSegmentFactory.create(TimeDiff(5), 10, LineName("1"), StopName("E"), stops),
            LineSegmentFactory.create(TimeDiff(6), 10, LineName("1"), StopName("F"), stops),
          ]
        )
      }
    )
  )


def crossConfig() -> ConnectionSearch:
  stops: StopsInterface = StopsFactory.create(
      {
        StopName("A"): StopFactory.create(StopName("A"), [LineName("1")]),
        StopName("B"): StopFactory.create(StopName("B"), [LineName(
            "1"), LineName("2")]),
        StopName("C"): StopFactory.create(StopName("C"), [LineName("1")]),
        StopName("D"): StopFactory.create(StopName("D"), [LineName("2")]),
        StopName("E"): StopFactory.create(StopName("E"), [LineName("2")]),
        StopName("F"): StopFactory.create(StopName("F"), [LineName("2")]),
      }
  )

  return ConnectionSearch(
      stops,
      LinesFactory.create(
          {
              LineName("1"): LineFactory.create(
                  LineName("1"),
                  [Time(10), Time(20), Time(30)],
                  StopName("A"),
                  [
                      LineSegmentFactory.create(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
                      LineSegmentFactory.create(TimeDiff(3), 10, LineName("1"), StopName("C"), stops)
                  ]
              ),
              LineName("2"): LineFactory.create(
                LineName("2"),
                [Time(13), Time(25), Time(40)],
                StopName("D"),
                [
                    LineSegmentFactory.create(TimeDiff(4), 10, LineName("2"), StopName("B"), stops),
                    LineSegmentFactory.create(TimeDiff(10), 10, LineName("2"), StopName("E"), stops),
                    LineSegmentFactory.create(TimeDiff(1), 10, LineName("2"), StopName("F"), stops)
                ]
              )
          }
      )
  )

def pragueMetro() -> ConnectionSearch:

  stops: StopsInterface = StopsFactory.create(
      {
        StopName("Hradcanska"): StopFactory.create(StopName("Hradcanska"), [LineName("A")]),
        StopName("Malostranska"): StopFactory.create(StopName("Malostranska"), [LineName("A")]),
        StopName("Staromestska"): StopFactory.create(StopName("Staromestska"), [LineName("A")]),
        StopName("Mustek"): StopFactory.create(StopName("Mustek"), [LineName("A"), LineName("B")]),
        StopName("Muzeum"): StopFactory.create(StopName("Muzeum"), [LineName("A"), LineName("C")]),
        StopName("Namesti Miru"): StopFactory.create(StopName("Namesti Miru"), [LineName("A")]),
        StopName("Jiriho z Podebrad"): StopFactory.create(StopName("Jiriho z Podebrad"), [LineName("A")]),
        StopName("Flora"): StopFactory.create(StopName("Flora"), [LineName("A")]),

        StopName("Andel"): StopFactory.create(StopName("Andel"), [LineName("B")]),
        StopName("Karlovo namesti"): StopFactory.create(StopName("Karlovo namesti"), [LineName("B")]),
        StopName("Narodni Trida"): StopFactory.create(StopName("Narodni Trida"), [LineName("B")]),
        StopName("Namesti Republiky"): StopFactory.create(StopName("Namesti Republiky"), [LineName("B")]),
        StopName("Florenc"): StopFactory.create(StopName("Florenc"), [LineName("B"), LineName("C")]),
        StopName("Krizikova"): StopFactory.create(StopName("Krizikova"), [LineName("B")]),
        StopName("Invalidovna"): StopFactory.create(StopName("Invalidovna"), [LineName("B")]),

        StopName("Vysehrad"): StopFactory.create(StopName("Vysehrad"), [LineName("C")]),
        StopName("IP Pavlova"): StopFactory.create(StopName("IP Pavlova"), [LineName("C")]),
        StopName("Hlavni nadrazi"): StopFactory.create(StopName("Hlavni nadrazi"), [LineName("C")]),
        StopName("Vltavska"): StopFactory.create(StopName("Vltavska"), [LineName("C")]),
        StopName("Nadrazi Holesovice"): StopFactory.create(StopName("Nadrazi Holesovice"), [LineName("C")]),
        StopName("Kobylisy"): StopFactory.create(StopName("Kobylisy"), [LineName("C")]),
        StopName("Ladvi"): StopFactory.create(StopName("Ladvi"), [LineName("C")]),
      }
  )

  return ConnectionSearch(
    stops,
    LinesFactory.create(
      {
        LineName("A"): LineFactory.create(
          LineName("A"),
          [Time(i) for i in range(0,200,10)],
          StopName("Hradcanska"),
          [
            LineSegmentFactory.create(
              TimeDiff(3),
              10,
              LineName("A"),
              StopName("Malostranska"),
              stops
            ),
            LineSegmentFactory.create(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Staromestska"),
                stops
            ),
            LineSegmentFactory.create(
                TimeDiff(2),
                10,
                LineName("A"),
                StopName("Mustek"),
                stops
            ),
            LineSegmentFactory.create(
                TimeDiff(8),
                10,
                LineName("A"),
                StopName("Muzeum"),
                stops
            ),
            LineSegmentFactory.create(
                TimeDiff(5),
                10,
                LineName("A"),
                StopName("Namesti Miru"),
                stops
            ),
            LineSegmentFactory.create(
                TimeDiff(3),
                10,
                LineName("A"),
                StopName("Jiriho z Podebrad"),
                stops
            ),
            LineSegmentFactory.create(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Flora"),
                stops
            ),
          ]
        ),
        LineName("B"): LineFactory.create(
            LineName("B"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Andel"),
            [
                LineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    StopName("Karlovo namesti"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(10),
                    10,
                    LineName("B"),
                    StopName("Narodni Trida"),
                stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("B"),
                    StopName("Mustek"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Namesti Republiky"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    StopName("Florenc"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Krizikova"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(9),
                    10,
                    LineName("B"),
                    StopName("Invalidovna"),
                    stops
                ),
            ]
        ),
        LineName("C"): LineFactory.create(
            LineName("C"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Vysehrad"),
            [
                LineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    StopName("IP Pavlova"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    StopName("Muzeum"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Hlavni nadrazi"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Florenc"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("C"),
                    StopName("Vltavska"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Nadrazi Holesovice"),
                    stops
                ),
                LineSegmentFactory.create(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Kobylisy"),
                    stops
                ),
                LineSegmentFactory.create(
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
