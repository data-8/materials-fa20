test = {
  'name': 'q2_1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [most_common('Genre', close_movies.take(range(k))) for k in range(1, 6, 2)]
          ['thriller', 'thriller', 'thriller']
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
