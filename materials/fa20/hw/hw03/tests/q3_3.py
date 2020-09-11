test = {
  'name': 'q3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you assign histogram_column_y to either 1 or 2!;
          >>> type(histogram_column_y) == int
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> histogram_column_y == 1 or histogram_column_y == 2 or histogram_column_x == 3
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
