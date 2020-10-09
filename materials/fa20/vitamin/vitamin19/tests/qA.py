test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2, 3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "What assumptions do we make about two samples when we conduct an A/B test? [Chapter 12.1](https://www.inferentialthinking.com/chapters/12/1/AB_Testing.html) is a good refresher on A/B testing.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "What assumptions do we make about two samples when we conduct an A/B test? [Chapter 12.1](https://www.inferentialthinking.com/chapters/12/1/AB_Testing.html) is a good refresher on A/B testing.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 3, "Under the null hypothesis, the distributions of baby birth weights are the same regardless of maternal smoking status. In other words, there is no association between a mother's smoking habits and her baby's birth weight.")
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
