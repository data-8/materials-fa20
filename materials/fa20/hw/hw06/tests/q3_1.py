test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> full_data.num_rows == 457
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Double check the way you're combining the two tables. Are you combining in the correct order;
          >>> # (in terms of the arguments)? The problem statement saying "except 'Name' column" is a hint;
          >>> # at the order in which you should combine the tables.;
          >>> list(full_data.labels)[0] == 'Player'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> full_data.select(sorted(full_data.labels)).sort(4).take(range(3))
          2P   | 3P   | PTS  | Player         | Salary
          0    | 0    | 0    | William Howard | 50000
          2    | 0    | 6    | Eric Mika      | 50752
          0    | 0    | 0    | Marques Bolden | 50752
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
