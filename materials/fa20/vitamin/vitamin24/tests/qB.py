test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_B in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "The parameter is either in our confidence interval, or it is not. It is not random and there is no chance involved. We cannot say that there is a 90% chance it will fall into the interval.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "The 90% confidence interval captures the middle 90% of our bootstrapped estimates, which are based off our resamples. We're estimating that their *average weight* is in this interval. The confidence interval does not directly tell us about the weights of 90% of babies.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "Revisit [Chapter 13.3](https://www.inferentialthinking.com/chapters/13/3/Confidence_Intervals.html) for a refresher on confidence intervals.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 3, "Correct! The 'confidence' references our trust in the process that we use in order to generate intervals. We would expect 90% of the intervals we generate to be 'good' ones. For example, if we generated 100 intervals, we would expect 90 of them to contain the true parameter.")
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
