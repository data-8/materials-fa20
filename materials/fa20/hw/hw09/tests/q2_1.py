test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simulate_resample(observations).num_rows
          212
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> simulate_resample(observations).labels[0] == observations.labels[0]
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
