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
          >>> feedback.check_ans(answer_A, 1, "A high correlation indicates that the two variables have a strong, positive linear association. For this example, we expect observations with relatively large values of x to also possess relatively large values of y. However, it does not mean that an increase in one variable **causes** the other to increase! Correlation does not imply causation.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "A high correlation indicates that the two variables have a strong, positive linear association. This does not mean that an increase in one variable **causes** the other to increase! Correlation does not imply causation.")
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
