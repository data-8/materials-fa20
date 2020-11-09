test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_B in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "Remember, no matter what the shape of the scatter plot is, there is a unique line that minimizes the mean squared error of estimation. It is called the regression line. `slope` = $r*\\frac{SD_y}{SD_x}$ and `intercept` = `average of y` - `slope` * `average of x`")
          False
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
