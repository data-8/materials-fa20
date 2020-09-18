test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Double check that your salary_range function is correct;
          >>> salary_range(make_array(5, 1, 20, 1000)) == 999
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that the table has departments as the rows and positions as the columns.;
          >>> set(["department", "assistant professor", "associate professor", "lecturer", "professor"]) == set(department_ranges.labels)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(department_ranges.column(1))
          2976273.0
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
