test = {
  'name': 'qC',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_C in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_C, 1, "Remember, `area of bar = % in bin = height * width of bin`. The width of each bin in this histogram is 10 years.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_C, 2, "Remember, `area of bar = % in bin = height * width of bin`. The width of each bin in this histogram is 10 years.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_C, 4, "Remember, `area of bar = % in bin = height * width of bin`. The width of each bin in this histogram is 10 years.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_C, 3, "Right! The area of the bar represents the percent of individuals in that bin. The height of the bar from 30 to 40 is approximately 1.5, and the width is 10. When we multiply these together, we get 15%.")
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
