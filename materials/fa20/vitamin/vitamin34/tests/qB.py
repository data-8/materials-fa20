test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_B in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "In lecture, we saw that the absolute value of $r$ is equal to the ratio of SDs between the fitted and observed values. However, that is not the value that Gregory is trying to find!")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 3, "This answer would be valid if Gregory had $Var(residuals)$ in the numerator.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "Hint: recall that variance is the mean **squared** deviation from the average. Thus, this ratio cannot be negative.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 2, "Recall from lecture that this ratio is equal to $r^2$. Since we know $r = -0.732$, we can just square that to get 0.536.")
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
