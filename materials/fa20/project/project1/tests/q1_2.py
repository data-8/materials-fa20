test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> first = round(h_decade_growth.sort(0).column(2).item(0), 8);
          >>> 0.005 <= first <= 0.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Compute the annual exponential growth rate;
          >>> max(h_decade_growth.column(2)) < 0.03
          True
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
