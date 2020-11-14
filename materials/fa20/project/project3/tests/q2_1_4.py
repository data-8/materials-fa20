test = {
  'name': 'q2_1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(close_movies.labels) >= {'Genre', 'Title', 'feel', 'water'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> close_movies.num_rows == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> close_movies.column("Title").item(0) != "monty python and the holy grail"
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
