from typing import Dict, List
from connectionSearch.connectionSearch import ConnectionSearch
from connectionSearch.datatypes.lineName import LineName
from connectionSearch.datatypes.stopName import StopName
from connectionSearch.datatypes.time import Time, TimeDiff
from connectionSearch.line import LineFactory
from connectionSearch.lines import LinesFactory
from connectionSearch.lineSegment import LineSegmentFactory
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

  linesFactory = LinesFactory()
  lineSegmentFactory = LineSegmentFactory()
  lineFactory = LineFactory()
  return ConnectionSearch(
    stops,
    linesFactory.create(
      {
        LineName("1"): lineFactory.create(
          LineName("1"), 
          [Time(10), Time(20), Time(30)], 
          StopName("A"),
          [
            lineSegmentFactory.create(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
            lineSegmentFactory.create(TimeDiff(3), 10, LineName("1"), StopName("C"), stops),
            lineSegmentFactory.create(TimeDiff(4), 10, LineName("1"), StopName("D"), stops),
            lineSegmentFactory.create(TimeDiff(5), 10, LineName("1"), StopName("E"), stops),
            lineSegmentFactory.create(TimeDiff(6), 10, LineName("1"), StopName("F"), stops),
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
  
  linesFactory = LinesFactory()
  lineSegmentFactory = LineSegmentFactory()
  lineFactory = LineFactory()
  return ConnectionSearch(
      stops,
      linesFactory.create(
          {
              LineName("1"): lineFactory.create(
                  LineName("1"),
                  [Time(10), Time(20), Time(30)],
                  StopName("A"),
                  [
                      lineSegmentFactory.create(TimeDiff(2), 10, LineName("1"), StopName("B"), stops),
                      lineSegmentFactory.create(TimeDiff(3), 10, LineName("1"), StopName("C"), stops)
                  ]
              ),
              LineName("2"): lineFactory.create(
                LineName("2"),
                [Time(13), Time(25), Time(40)],
                StopName("D"),
                [
                    lineSegmentFactory.create(TimeDiff(4), 10, LineName("2"), StopName("B"), stops),
                    lineSegmentFactory.create(TimeDiff(10), 10, LineName("2"), StopName("E"), stops),
                    lineSegmentFactory.create(TimeDiff(1), 10, LineName("2"), StopName("F"), stops)
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

  linesFactory = LinesFactory()
  lineSegmentFactory = LineSegmentFactory()
  lineFactory = LineFactory()
  return ConnectionSearch(
    stops,
    linesFactory.create(
      {
        LineName("A"): lineFactory.create(
          LineName("A"),
          [Time(i) for i in range(0,200,10)],
          StopName("Hradcanska"),
          [
            lineSegmentFactory.create(
              TimeDiff(3),
              10,
              LineName("A"),
              StopName("Malostranska"),
              stops
            ),
            lineSegmentFactory.create(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Staromestska"),
                stops
            ),
            lineSegmentFactory.create(
                TimeDiff(2),
                10,
                LineName("A"),
                StopName("Mustek"),
                stops
            ),
            lineSegmentFactory.create(
                TimeDiff(8),
                10,
                LineName("A"),
                StopName("Muzeum"),
                stops
            ),
            lineSegmentFactory.create(
                TimeDiff(5),
                10,
                LineName("A"),
                StopName("Namesti Miru"),
                stops
            ),
            lineSegmentFactory.create(
                TimeDiff(3),
                10,
                LineName("A"),
                StopName("Jiriho z Podebrad"),
                stops
            ),
            lineSegmentFactory.create(
                TimeDiff(4),
                10,
                LineName("A"),
                StopName("Flora"),
                stops
            ),
          ]
        ),
        LineName("B"): lineFactory.create(
            LineName("B"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Andel"),
            [
                lineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    StopName("Karlovo namesti"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(10),
                    10,
                    LineName("B"),
                    StopName("Narodni Trida"),
                stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("B"),
                    StopName("Mustek"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Namesti Republiky"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("B"),
                    StopName("Florenc"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("B"),
                    StopName("Krizikova"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(9),
                    10,
                    LineName("B"),
                    StopName("Invalidovna"),
                    stops
                ),
            ]
        ),
        LineName("C"): lineFactory.create(
            LineName("C"),
            [Time(i) for i in range(0, 200, 10)],
            StopName("Vysehrad"),
            [
                lineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    StopName("IP Pavlova"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(5),
                    10,
                    LineName("C"),
                    StopName("Muzeum"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Hlavni nadrazi"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Florenc"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(3),
                    10,
                    LineName("C"),
                    StopName("Vltavska"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(2),
                    10,
                    LineName("C"),
                    StopName("Nadrazi Holesovice"),
                    stops
                ),
                lineSegmentFactory.create(
                    TimeDiff(1),
                    10,
                    LineName("C"),
                    StopName("Kobylisy"),
                    stops
                ),
                lineSegmentFactory.create(
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
