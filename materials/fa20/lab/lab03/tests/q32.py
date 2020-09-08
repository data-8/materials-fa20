test = {
  'name': 'q32',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> imdb.num_rows == 250
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> imdb.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(2,5))
          Votes | Rating | Title                       | Year | Decade
          31003 | 8.1    | Le salaire de la peur       | 1953 | 1950
          32385 | 8      | La battaglia di Algeri      | 1966 | 1960
          35983 | 8.1    | The Best Years of Our Lives | 1946 | 1940
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
