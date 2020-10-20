test = {
  'name': 'q3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(postban_rates, Table)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> postban_rates.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(postban_rates.column("Death Penalty") == False)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(postban_rates.column("Year") == 1973)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(elem in postban_rates.column("State") for elem in preban_rates.column("State"))
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
