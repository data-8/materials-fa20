test = {
  'name': 'q3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> distribution_1 in ['empirical', 'probability']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> distribution_2 in ['empirical', 'probability']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(player_count_1) == int and type(player_count_2) == int
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(area_total_1) == int and type(area_total_2) == int
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
