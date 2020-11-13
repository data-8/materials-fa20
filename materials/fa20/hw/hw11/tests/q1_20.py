test = {
  'name': 'q1_20',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(lower_bound_evan) in set([float, np.float32, np.float64]), 
          ...     type(upper_bound_evan) in set([float, np.float32, np.float64])])
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
