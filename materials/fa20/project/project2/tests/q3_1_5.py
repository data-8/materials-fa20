test = {
  'name': 'q3_1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < min(bootstrap_rrs) <= max(bootstrap_rrs) < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.random.seed(123);
          >>> np.isclose(round(one_bootstrap_rr(), 3), 0.451)
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
