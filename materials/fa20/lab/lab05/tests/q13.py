test = {
  'name': 'q13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> nacho_reaction('salsa')
          'Spicy!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('cheese')
          'Cheesy!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('both')
          'Wow!'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> nacho_reaction('neither')
          'Meh.'
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
