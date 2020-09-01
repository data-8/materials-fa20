test = {
  'name': 'q41',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(above_eight) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> above_eight.num_rows == 20
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure your columns are in the right order!;
          >>> # First column should be 'Title', second column should be 'Rating';
          >>> print(above_eight.sort(0).take([17]))
          Title       | Rating
          Toy Story 3 | 8.3
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
