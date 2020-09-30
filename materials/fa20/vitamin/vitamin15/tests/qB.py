test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_B in [1, 2, 3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1,"Although Meghan does not have a say in who walks by, she also does not know the probability of each person entering the sample. This is something that must be known beforehand in order for the sample to be a *random* sample.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 3, "Deterministic samples result when we specify which elements of a set we want to choose. Does her sampling scheme involve chance?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 2, "Meghan does not know the probability of each person entering the sample and is merely gathering data from whoever happens to walk by. This is quite a *convenient* way to get a sample!")
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
