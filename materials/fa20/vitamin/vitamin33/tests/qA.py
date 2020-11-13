test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1,2,3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "A correlation coefficient of 1 means that the predicted and observed values have a perfect linear relationship; they fall on the same line. If the predicted and observed fall on the same line, then all of the residuals are equal to 0. Thus, what should the standard deviation of the residuals be?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 3, "A correlation coefficient of 1 means that the predicted and observed values have a perfect linear relationship; they fall on the same line. If the predicted and observed fall on the same line, then all of the residuals are equal to 0. Thus, what should the standard deviation of the residuals be?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "Right! The standard deviation of the residuals would be 0. When we have a perfect linear relationship, the predicted and observed values all fall on the same line. All the residuals are equal to 0, so there's no variation in their values. Thus, the standard deviation of the residuals is 0.")
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
