test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> elements_of_some_numbers.column(0).item(2) == "third"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> elements_of_some_numbers.column(0).item(3) == "fourth"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> elements_of_some_numbers.column(1).item(0) == 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> elements_of_some_numbers.column(1).item(3) == 3
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
