test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> if answer_A not in [1, 2, 3]:
          ...     print("Please assign the varaible to an answer!")
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Making predictions involves using partial information to make guesses about the things we do not know yet.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 3, "Making predictions involves using data we know in order to make informed guesses about what will happen in the future.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> answer_A == 2
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
