test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "Would it make sense to perform arithmetic operations with these numbers?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "Right! Even though values in the `SEX` column are numbers, they do not have any mathematical value and only serve as indicators.")
          <IPython.core.display.Markdown object>
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
