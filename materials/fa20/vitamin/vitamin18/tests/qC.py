test = {
  'name': 'qC',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_C in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_C, 2, "If the observed statistic or values more extreme than the observed statistic are likely to have occurred under the null hypothesis, the data are probably consistent with the assumptions made by the null hypothesis.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_C, 1, "Right! If the observed statistic or values more extreme than the observed statistics are unlikely to have occurred under the null hypothesis, the data are probably inconsistent with the assumptions made by the null hypothesis.")
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
