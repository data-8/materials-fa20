test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Tip: the 90% confidence interval captures the middle 90% of the data. This leaves 10% of uncaptured data on the left and right ends. Assuming that the distribution is normal, what percentage of data should lie on each end?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "Tip: the 90% confidence interval captures the middle 90% of the data. This leaves 10% of uncaptured data on the left and right ends. Assuming that the distribution is normal, what percentage of data should lie on each end?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 4, "Tip: the 90% confidence interval captures the middle 90% of the data. This leaves 10% of uncaptured data on the left and right ends. Assuming that the distribution is normal, what percentage of data should lie on each end?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 3, "Right! The 90% confidence interval captures the middle 90% of the data. This leaves 10% of uncaptured data on the left and right ends. Assuming that the distribution is normal, 5% of data should be left on each end. Thus, the interval would start from the 5th percentile and go to the 95th percentile.")
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
