test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_A in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "Let's take a closer look at the model. The model specifies the assumption that there is a 60% chance that there will be churros on any given day. Tam and Ananya can randomly sample many times from the distribution specified by the model and see how often churros were offered at the Taco Stand.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "The model seems valid; it specifies the assumption that there is a 60% chance that there will be churros on any given day. Tam and Ananya can randomly sample many times from the distribution specified by the model and see how often churros were offered at the Taco Stand.")
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
