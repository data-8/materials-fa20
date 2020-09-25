test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'did_cal_lose' in globals()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> did_cal_lose(final_scores.row(1))
          False
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
