test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(example_estimates)
          500
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 12 <= np.mean(example_estimates) <= 16
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.count_nonzero(np.diff(example_estimates)) >= 1
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
