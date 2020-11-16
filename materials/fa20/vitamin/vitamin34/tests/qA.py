test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2, 3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Remember, residuals do not vary as much as the observed values of $y$. Thus, the SD of the residuals should not be greater.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "Remember, the residuals do not vary as much as the observed values of $y$.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 3, "The residuals do not vary as much as the observed values of $y$. Thus, the SD of the fitted values should only be a fraction of, and thus less than or equal to, the SD of the observed values of $y$. The SD of the residuals and the SD of y are only equal when r=0.")
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
