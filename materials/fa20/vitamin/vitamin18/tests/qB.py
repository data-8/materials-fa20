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
          >>> feedback.check_ans(answer_B, 2, "Remember, the p-value is the chance, under the *null hypothesis*, that the test statistic is equal to the observed value or is even further in the direction of the alternative. If the area of the tail past the observed statistic is small, then the observed statistic lies far in the tail and is far from what the null predicts.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 3, "Remember, the p-value is the chance, under the *null hypothesis*, that the test statistic is equal to the observed value or is even further in the direction of the alternative. If the tail area past the observed statistic is small, then the observed statistic lies far in the tail and is far from what the null predicts.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "Remember, the p-value is the chance, under the *null hypothesis*, that the test statistic is equal to the observed value or is even further in the direction of the alternative. If the tail area past the observed statistic is small, then the observed statistic lies far in the tail and is far from what the null predicts.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 1, "Right! If the tail area past the observed statistic is small, then the observed statistic lies far in the tail and is unlikely under the null hypothesis.")
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
