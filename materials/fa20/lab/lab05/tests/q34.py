test = {
  'name': 'q34',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> prob_third_given_declared > 0.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(prob_third_given_declared, .52, 2*.005)
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
