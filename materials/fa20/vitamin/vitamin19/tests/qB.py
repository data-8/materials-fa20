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
          >>> feedback.check_ans(answer_B, 1, "In this class, total variation distance is used when we have a random sample with data in multiple categories (i.e. Did the Alameda County jury panels look like one random sample from the population of eligible jurors?). How many samples are involved in A/B testing?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 3, "In this class, total variation distance is used when we have one random sample with data in multiple categories (i.e. Did the Alameda County jury panels look like a random sample from the population of eligible jurors?). How many samples are involved in A/B testing?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "Notice how my alternative hypothesis does not indicate any sort of direction; it simply states that the samples do not come from the same underlying distribution. Sometimes, large values of the statistic may favor the alternative hypothesis, but that depends on the specific hypothesis and the way you calculate your test statistic. Sometimes, small values may favor the alternative hypothesis instead. This question asks about a general situation.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 2, "Under the null hypothesis, we expect the groups' averages to be identical; therefore, their samples' averages should be very similar. When the observed difference between these samples' averages is quite large or very small (that is, large negative values), it is inconsistent with the null hypothesis. This means that large absolute values of the statistic provide evidence in favor of the alternative hypothesis.")
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
