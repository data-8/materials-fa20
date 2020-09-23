test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your answer is not a number-- make sure you assigned answer_A to one of the numbers above. ;
          >>> type(answer_A) is int
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
