test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_B in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "Recall the equation of the regression line: `y = slope * x + intercept`. Are each of these components in standard or original units? While the correlation coefficient is not dependent on the units of a variable, the mean and standard deviation are. Since these values are used to calculate the slope and intercept of a line, the regression line will change if we convert the units of our variables to standard units. You can read more about it in [this section of the textbook](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html)")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 1, "Right! While the correlation coefficient is not dependent on the units of a variable, the mean and standard deviation are. Since these values are used to calculate the slope and intercept of a line, the regression line will change if we convert the units of our variables to standard units. You can read more about it in [this section of the textbook](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html)")
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
