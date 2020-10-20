test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(ab_test_order) == 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> correct_order = make_array(5, 1, 3, 2, 4, 6);
          >>> all(correct_order == ab_test_order)
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
