test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "In lecture, we wanted to see whether the the distribution of ethnicities of the panels was close to that of the eligible jurors. The distribution of ethnicities is categorical! We use TVD to measure the distance between **categorical** distributions.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "TVD is useful when we want to measure the distance between categorical distributions. In lecture, the distribution of ethnicities of eligible jurors was categorical, so it was appropriate to use TVD as our statistic.")
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
