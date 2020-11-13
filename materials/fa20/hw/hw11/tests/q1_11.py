test = {
  'name': 'q1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(lower_bound_sal) in set([float, np.float32, np.float64]), 
          ...     type(upper_bound_sal) in set([float, np.float32, np.float64]),
          ...     type(reject_sal) == bool])
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
