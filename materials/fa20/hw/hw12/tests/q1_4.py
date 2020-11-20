test = {
  'name': 'q1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(first_test) == str or type(first_test) == np.str_
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sorted_coordinates = coordinates.sort("school");
          >>> classify(sorted_coordinates.row(85), 3, sorted_coordinates.take(np.arange(50, 100))) == 'Stanford'
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
