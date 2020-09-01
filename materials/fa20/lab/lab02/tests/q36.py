test = {
  'name': 'q36',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> berkeley_markets.num_rows == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(berkeley_markets.column('city')) == ['Berkeley', 'Berkeley', 'Berkeley']
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
