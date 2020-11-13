test = {
  'name': 'q1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(lower_bound_pc) in set([float, np.float32, np.float64]), 
          ...     type(upper_bound_pc) in set([float, np.float32, np.float64]),
          ...     type(reject) == bool])
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
