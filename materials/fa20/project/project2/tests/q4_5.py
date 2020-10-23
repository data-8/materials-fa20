test = {
  'name': 'q4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> summed_mn_hazard_data.num_rows == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(summed_mn_hazard_data.labels) == 4
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
