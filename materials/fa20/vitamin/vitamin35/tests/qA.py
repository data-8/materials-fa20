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
          >>> feedback.check_ans(answer_A, 1, "Make sure to double-check the units on the x-axis and the y-axis; which distance would be greater considering the larger magnitude of the x-axis units?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "Correct! The three nearest points have a majority of the blue no-Anemia class. It is important when doing k-nearest neighbors to check the units-- since the x-axis has units that are much larger in magnitude, even a small difference in White Blood Cell Count would lead to a large distance calculation between two points.")
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
