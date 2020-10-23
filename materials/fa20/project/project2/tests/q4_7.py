test = {
  'name': 'q4_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(our_p_value) in set([float, np.float64])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 < our_p_value < 1
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
