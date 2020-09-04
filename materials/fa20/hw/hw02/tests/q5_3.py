test = {
  'name': 'q5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> difference_from_expected.size
          272
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> difference_from_expected.item(271) == abs(60 * 272 - sum(waiting_times))
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
