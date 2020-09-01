test = {
  'name': 'q35',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(farmers_markets_locations_by_latitude) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(farmers_markets_locations_by_latitude.column('y').take(range(3)))
          [64.86275, 64.8459, 64.844414]
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
