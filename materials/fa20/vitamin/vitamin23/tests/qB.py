test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_B in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "Please check it on Gradescope!")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 1, "If you'd like to, check out some of the links above if you haven't already.")
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
