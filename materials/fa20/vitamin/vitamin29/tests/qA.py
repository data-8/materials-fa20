test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2, 3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Recall the formula for the SD of sample averages in [Chapter 14.5](https://www.inferentialthinking.com/chapters/14/5/Variability_of_the_Sample_Mean.html).")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 3, "Recall the formula for the SD of sample averages in [Chapter 14.5](https://www.inferentialthinking.com/chapters/14/5/Variability_of_the_Sample_Mean.html).")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "Sample size is in the denominator of the formula, so increasing it should decrease the SD of sample averages. Intuitively, increasing sample size should decrease how variable our sample means are!")
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
