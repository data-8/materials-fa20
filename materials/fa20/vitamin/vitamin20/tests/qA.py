test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Recall from lecture that the p-value cutoff is an error probability. Take a look at [Ch. 11.4](https://www.inferentialthinking.com/chapters/11/4/Error_Probabilities.html)")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 3, "Recall from lecture that the p-value cutoff is an error probability. Take a look at [Ch. 11.4](https://www.inferentialthinking.com/chapters/11/4/Error_Probabilities.html)")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 4, "Recall from lecture that the p-value cutoff is an error probability. Take a look at [Ch. 11.4](https://www.inferentialthinking.com/chapters/11/4/Error_Probabilities.html)")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "Recall from lecture that the p-value cutoff is an error probability. There is a 10% chance that her test will incorrectly reject the null hypothesis, when in reality, the null hypothesis shouldn't be rejected.")
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
