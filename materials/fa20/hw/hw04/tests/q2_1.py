test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> prof_names.num_columns
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> prof_names.num_rows
          71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that you have the correct column labels!;
          >>> np.asarray(prof_names.labels).item(1) != "name identity"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that you have the correct column labels!;
          >>> np.asarray(prof_names.labels).item(1) == "faculty"
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
