test = {
  'name': 'q1_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(least_squares_order) == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> correct_order = make_array(4, 1, 3, 2);
          >>> all(correct_order == least_squares_order)
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
