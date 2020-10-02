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
          >>> feedback.check_ans(answer_B, 1, "Remember, we are comparing our statistic to the assumption we make in our model. Counting the number of days that churros are offered may not be the best statistic, for we are trying to see how far away our statistic is from 60%.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "Remember, we are comparing our statistic to the assumption we make in our model. Calculating the average number of days that churros are offered may not be the best statistic, for we are trying to see how far away our statistic is from 60%.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "Take a look at the textbook section that is linked in the hint above!")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 3, "The distance from 60% sounds like a valid statistic. After all, we are just trying to see how far our sample percent is from 60%. Large distances indicate that our model is not good.")
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
