test = {
  'name': 'q2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure that the table has a column called department and a column called count.;
          >>> set(["department", "count"]) == set(department_and_counts.labels)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you do not include departments that don't have positions with average salary above 100k.;
          >>> department_and_counts.num_rows
          65
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
