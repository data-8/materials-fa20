test = {
  'name': 'q1_12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(career_length_slope) in set([float, np.float32, np.float64]),
          ...     type(career_length_intercept) in set([float, np.float32, np.float64]),
          ...     type(salary_slope) in set([float, np.float32, np.float64]),
          ...     type(salary_intercept) in set([float, np.float32, np.float64])])
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
