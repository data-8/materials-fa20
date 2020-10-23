test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2, 3,4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Although the 95% confidence interval is often mentioned in class, the method she should use here is to construct a confidence interval based off the p-value. Check out the 'Using a CI for Testing' slide in lecture.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 3, "The p-value cutoff is 8%. This means that 8% of the data will lie outside of our confidence interval. Knowing this, how much data will lie *inside* of the interval?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 4, "The p-value cutoff is all you need to figure this out! Check out the 'Using a CI for Testing' slide in lecture.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "Melissa should construct a (100-p)% confidence interval for the population average. Thus, it should be a (100-8)% = 92% confidence interval.")
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
