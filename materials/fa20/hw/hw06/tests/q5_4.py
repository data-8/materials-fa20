test = {
  'name': 'q5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # There should be exactly as many elements in deck_statistics;
          >>> # as the number 'repetitions';
          >>> len(deck_statistics) == repetitions
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Each element of deck_statistics should be between 0;
          >>> # and 13 inclusive;
          >>> all([0 <= k <= 13 for k in deck_statistics])
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
