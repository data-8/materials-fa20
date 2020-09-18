test = {
  'name': 'q1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you are using the date range 1970-2020;
          >>> post_1969_fertility_and_child_mortality.num_rows
          51
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check your column labels and spelling;
          >>> all([label in post_1969_fertility_and_child_mortality.labels for label in ['Children per woman', 'Child deaths per 1000 born']])
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
