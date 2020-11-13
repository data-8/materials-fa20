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
          >>> feedback.check_ans(answer_B, 1, "Take a look at the tip provided in the question!")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 2, "There seems to be a pattern in our residual plot; the vertical spread of the plot is greater for low values of acceleration than for high values. Since the residual plot shows uneven vertical spread about the horizontal line at 0, the regression estimates are not equally accurate across the range of the predictor variable, and linear regression is not a great model for this situation. This plot exemplifies heteroscedasticity, which you can read about [here](https://www.inferentialthinking.com/chapters/15/5/Visual_Diagnostics.html).")
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
