test = {
  'name': 'q3_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0.0 <= distance_first_to_second <= 0.1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(distance(make_array(1, 2), make_array(1, 2)), 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(distance(make_array(1, 2, 3), make_array(2, 4, 5)), 3)
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
