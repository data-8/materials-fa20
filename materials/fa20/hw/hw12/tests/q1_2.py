test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Double check that you have the correct number of rows for the `train` table.;
          >>> train.num_rows == 75
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Double check that you have the correct number of rows for the `test` table.;
          >>> test.num_rows == 25
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> train.num_rows + test.num_rows == coordinates.num_rows
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
