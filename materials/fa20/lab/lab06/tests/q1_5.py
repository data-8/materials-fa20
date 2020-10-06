test = {
  'name': 'q1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int(round(statistic(.5,.5) + statistic(.4,.1),1))
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(statistic(.4,.1) - statistic(.1,.4))
          0
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
