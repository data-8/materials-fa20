test = {
  'name': 'q3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(preban_rates, Table)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> preban_rates.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(preban_rates.column("Death Penalty") == True)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(preban_rates.column("Year") == 1971)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(elem in death_penalty.column("State") for elem in preban_rates.column("State"))
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
