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
          >>> feedback.check_ans(answer_A, 2, "What side is the tail on? Also, let's think of an example. Let's say the majority of this class scored 80% to 85% on the midterm, but there were five outliers who scored 100%. The median score is 83%, regardless of the five outliers. Would we expect these 5 high-scorers to pull the mean score up or drag it down? Remember, the mean is the distribution's 'balance point.' If there are outlying data on the right side, the mean would also shift to the right as well.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "Correct! Remember, the mean is the balance point of the distribution. This means that the tail of a distribution pulls the mean towards it. Thus, a distribution with a long, right tail would pull the mean to the right side. The mean would be greater than the median, and the distribution would be right-skewed.")
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
