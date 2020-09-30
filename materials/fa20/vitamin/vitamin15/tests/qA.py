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
          >>> feedback.check_ans(answer_A, 1, "A good way to remember the terminology is by looking at the first letters of these words. A **p**arameter comes from a **p**opulation, whereas a **s**tatistic comes from a **s**ample. A statistic is something we calculate using data from our random sample, so it is indeed random and variable.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "A good way to remember the terminology is by looking at the first letters of these words. A **p**arameter comes from a **p**opulation, whereas a **s**tatistic comes from a **s**ample. Remember, a statistic is something we calculate using data from our random sample. ")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 4, "Almost - a parameter comes from the population, and a statistic comes from a sample. However, a parameter is fixed because it comes from the population. A statistic is something we calculate using data from our random sample, so the value of the statistic may vary depending on the data in our sample.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 3, "A parameter is fixed because it comes from the population. A statistic is something we calculate using data from our random sample, so the value of the statistic may vary depending on the data in our sample.")
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
