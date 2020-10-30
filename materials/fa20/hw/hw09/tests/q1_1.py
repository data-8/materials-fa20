test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> V == "parameter" or V == "statistic"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> V_estimate == "parameter" or V_estimate == "statistic"
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
