test = {
  'name': 'q3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> rate_means.num_rows
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> rate_means.where("Death Penalty", False).column(1).item(0)
          8.120454540452272
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> rate_means.where("Death Penalty", True).column(1).item(0)
          7.513636380386362
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
