test = {
  'name': 'q32',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.count_nonzero(all_groups.column(1) - all_groups.column(2) == [0, 24]) is 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all_groups.column(0).item(0)[0] == "S"
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
