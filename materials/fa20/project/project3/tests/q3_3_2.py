test = {
  'name': 'q3_3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> test_movie_correctness.num_rows == test_movies.num_rows
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that test_movie_correctness does not modify the original;
          >>> # test_movies table.;
          >>> print(test_movie_correctness.group('Genre'))
          Genre    | count
          comedy   | 20
          thriller | 36
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
