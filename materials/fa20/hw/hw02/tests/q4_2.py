test = {
  'name': 'q4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(cumulative_sum_answer) == int
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 1 <= cumulative_sum_answer <= 3
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
