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
          >>> feedback.check_ans(answer_A, 2, "Take a look at the definitions of the null and alternative hypotheses in [Chapter 11.3](https://www.inferentialthinking.com/chapters/11/3/Decisions_and_Uncertainty.html). Which hypothesis is a well-defined chance model?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "The null hypothesis is a well-defined chance model that makes assumptions about the data. This means we can simulate data under these assumptions!")
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
