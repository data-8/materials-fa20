test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column labels and spelling;
          >>> recent_poverty_total.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Careful, the population of Australia in 2010 was 22,154,687;
          >>> recent_poverty_total.where('geo', 'aus').column(2).item(0)
          22154687
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The number of people estimated to be living in extreme poverty;
          >>> # in Australia should be 301,304. That's 22,154,687 * 0.0136;
          >>> # rounded to the nearest integer.;
          >>> float(recent_poverty_total.where('geo', 'aus').column(3).item(0))
          301304.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
